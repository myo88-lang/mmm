import pandas as pd
import requests
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import streamlit as st
import pickle
import os

# -----------------------------
# 1. Download all Premier League historical data
# -----------------------------
@st.cache_data
def load_all_epl_data():
    seasons = [
        "9394", "9495", "9596", "9697", "9798", "9899", "9900",
        "0001", "0102", "0203", "0304", "0405", "0506", "0607", "0708", "0809", "0910",
        "1011", "1112", "1213", "1314", "1415", "1516", "1617", "1718", "1819", "1920",
        "2021", "2122", "2223", "2324", "2425"  # goes up to current 2024/25 season
    ]
    dfs = []
    for season in seasons:
        url = f"https://www.football-data.co.uk/mmz4281/{season}/E0.csv"
        try:
            r = requests.get(url)
            if r.status_code == 200:
                data = StringIO(r.text)
                df = pd.read_csv(data)
                df['Season'] = season
                dfs.append(df)
        except:
            continue
    return pd.concat(dfs, ignore_index=True)

# -----------------------------
# 2. Prepare Manchester United only dataset
# -----------------------------
def prepare_man_utd_data(df):
    # Standardise team names
    man_utd_names = ['Man United', 'Manchester Utd', 'Man Utd', 'Manchester United']
    df['HomeTeam'] = df['HomeTeam'].replace({'Man United': 'Manchester United', 'Man Utd': 'Manchester United'})
    df['AwayTeam'] = df['AwayTeam'].replace({'Man United': 'Manchester United', 'Man Utd': 'Manchester United'})

    # Create rows where Man United is playing
    home = df[df['HomeTeam'] == 'Manchester United'].copy()
    away = df[df['AwayTeam'] == 'Manchester United'].copy()

    home['IsHome'] = 1
    home['Opponent'] = home['AwayTeam']
    home['MU_Goals'] = home['FTHG']
    home['Opp_Goals'] = home['FTAG']

    away['IsHome'] = 0
    away['Opponent'] = away['HomeTeam']
    away['MU_Goals'] = away['FTAG']
    away['Opp_Goals'] = away['FTHG']

    data = pd.concat([home, away], ignore_index=True)

    # Result from Man United perspective: 1 = Win, 0 = Draw, -1 = Loss
    data['Result'] = np.where(data['MU_Goals'] > data['Opp_Goals'], 1,
                              np.where(data['MU_Goals'] == data['Opp_Goals'], 0, -1))

    return data

# -----------------------------
# 3. Feature engineering
# -----------------------------
def add_features(data):
    # Sort by date
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    data = data.sort_values('Date')

    # Rolling stats last 5 matches for Man United
    data['MU_Form_Pts'] = 0
    data['MU_Goals_Scored_Last5'] = 0
    data['MU_Goals_Conceded_Last5'] = 0
    data['Opp_Form_Pts'] = 0  # we'll approximate

    mu_matches = []
    for idx, row in data.iterrows():
        # Man United recent form
        recent = [m for m in mu_matches[-5:] ]
        if recent:
            pts = sum(3 if r['Result']==1 else 1 if r['Result']==0 else 0 for r in recent)
            data.at[idx, 'MU_Form_Pts'] = pts
            data.at[idx, 'MU_Goals_Scored_Last5'] = sum(r['MU_Goals'] for r in recent)
            data.at[idx, 'MU_Goals_Conceded_Last5'] = sum(r['Opp_Goals'] for r in recent)

        mu_matches.append(row)

    # Simple opponent strength (average points opponent earned against others - very rough but works)
    # For real project you could pre-compute league tables per season

    features = ['IsHome', 'MU_Form_Pts', 'MU_Goals_Scored_Last5', 'MU_Goals_Conceded_Last5']
    return data.dropna(subset=features), features

# -----------------------------
# 4. Train / load model
# -----------------------------
MODEL_FILE = "man_utd_model.pkl"

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    clf = RandomForestClassifier(n_estimators=300, random_state=42)
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    st.write(f"Model accuracy on test set: {accuracy_score(y_test, pred):.1%}")
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(clf, f)
    return clf

def get_model():
    if os.path.exists(MODEL_FILE):
        with open(MODEL_FILE, "rb") as f:
            return pickle.load(f)
    else:
        st.write("Training new model...")
        df = load_all_epl_data()
        data = prepare_man_utd_data(df)
        data, features = add_features(data)
        X = data[features]
        y = data['Result']
        return train_model(X, y)

# -----------------------------
# 5. Streamlit Web App
# -----------------------------
st.title("🔴 Manchester United Match Result Predictor")
st.markdown("""
Predict the outcome of any upcoming Manchester United Premier League fixture  
using historical data + machine learning (Random Forest).
""")

clf = get_model()

st.subheader("Predict a new match")
col1, col2 = st.columns(2)
with col1:
    is_home = st.radio("Manchester United playing at:", ["Home (Old Trafford)", "Away"], index=0)
    is_home_val = 1 if is_home.startswith("Home") else 0

with col2:
    opponent = st.text_input("Opponent (e.g. Liverpool, Arsenal, Man City)", "Liverpool")

if st.button("Predict Result"):
    # For a real prediction we would need recent form - we use average recent form as fallback
    # In production you would pull the last 5 MU results automatically
    input_data = [[
        is_home_val,
        10,   # assume decent recent form (10/15 pts)
        12,   # goals scored last 5
        5     # goals conceded last 5
    ]]
    prob = clf.predict_proba(input_data)[0]
    pred = clf.predict(input_data)[0]

    result_map = {1: "Win 🏆", 0: "Draw 🤝", -1: "Loss 😢"}
    st.metric("Predicted Result", result_map[pred])
    st.bar_chart({"Win": prob[2], "Draw": prob[1], "Loss": prob[0]}, height=300)  # order Loss/Draw/Win because classes are -1,0,1

st.caption("Data source: football-data.co.uk | Model trained on all Man United PL matches since 1993")
