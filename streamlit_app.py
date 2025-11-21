# app.py
# app.py
!pip install streamlit
!mkdir -p data

# Write mu_win_probability_2025_2026_by_opponent.csv
mu_prob_csv_content = """Opponent,Is_Home,Prob_Avg,Prob_Avg_pct
Arsenal,1,0.505,50.5
Aston Villa,1,0.613,61.3
Bournemouth,1,0.767,76.7
Brentford,1,0.686,68.6
Brighton,1,0.669,66.9
Burnley,1,0.83,83.0
Chelsea,1,0.598,59.8
Crystal Palace,1,0.688,68.8
Everton,1,0.71,71.0
Fulham,1,0.71,71.0
Leeds,1,0.803,80.3
Leicester,1,0.793,79.3
Liverpool,1,0.395,39.5
Luton,1,0.84,84.0
Man City,1,0.387,38.7
Newcastle,1,0.636,63.6
"Nott'm Forest",1,0.75,75.0
Southampton,1,0.78,78.0
Tottenham,1,0.585,58.5
West Ham,1,0.683,68.3
Wolves,1,0.723,72.3
Arsenal,0,0.47,47.0
Aston Villa,0,0.559,55.9
Bournemouth,0,0.702,70.2
Brentford,0,0.62,62.0
Brighton,0,0.603,60.3
Burnley,0,0.776,77.6
Chelsea,0,0.544,54.4
Crystal Palace,0,0.622,62.2
Everton,0,0.655,65.5
Fulham,0,0.655,65.5
Leeds,0,0.748,74.8
Leicester,0,0.738,73.8
Liverpool,0,0.36,36.0
Luton,0,0.787,78.7
Man City,0,0.352,35.2
Newcastle,0,0.579,57.9
"Nott'm Forest",0,0.694,69.4
Southampton,0,0.726,72.6
Tottenham,0,0.531,53.1
West Ham,0,0.617,61.7
Wolves,0,0.668,66.8"""
with open("data/mu_win_probability_2025_2026_by_opponent.csv", "w") as f:
    f.write(mu_prob_csv_content)

# Write predicted_2025_2026_season_results.csv
predicted_results_csv_content = """HomeTeam,AwayTeam,Predicted_Result
Arsenal,Chelsea,Draw
Aston Villa,West Ham,Win
Bournemouth,Fulham,Draw
Brentford,Crystal Palace,Win
Brighton,Tottenham,Draw
Burnley,Everton,Win
Liverpool,Man United,Draw
Man City,Newcastle,Win
Sheff United,Wolves,Win
"Nott'm Forest",Leeds,Win
Southampton,Leicester,Win
Man United,Arsenal,Win
West Ham,Bournemouth,Draw
Fulham,Brentford,Loss
Crystal Palace,Brighton,Win
Everton,Aston Villa,Draw
Newcastle,Burnley,Win
Tottenham,Liverpool,Loss
Wolves,Man City,Loss
Leeds,Sheff United,Draw
Leicester,Southampton,Draw
Chelsea,"Nott'm Forest",Win
Arsenal,Aston Villa,Win
Bournemouth,Crystal Palace,Win
Brentford,Everton,Draw
Brighton,Newcastle,Loss
Burnley,Fulham,Draw
Liverpool,West Ham,Win
Man City,Tottenham,Win
Sheff United,Man United,Loss
"Nott'm Forest",Southampton,Win
Southampton,Leeds,Draw
Leicester,Chelsea,Loss
Man United,Bournemouth,Win
West Ham,Brentford,Loss
Fulham,Crystal Palace,Win
Crystal Palace,Everton,Win
Everton,Newcastle,Draw
Newcastle,Tottenham,Draw
Tottenham,Wolves,Win
Wolves,Leeds,Draw
Leeds,Leicester,Draw
Chelsea,Southampton,Win
Arsenal,Bournemouth,Win
Aston Villa,Brentford,Draw
Brighton,Burnley,Win
Crystal Palace,Liverpool,Draw
Everton,Man City,Loss
Fulham,Sheff United,Win
Leicester,"Nott'm Forest",Win
Liverpool,Man United,Win
Man City,West Ham,Win
Man United,Brighton,Win
Newcastle,Crystal Palace,Win
"Nott'm Forest",Arsenal,Loss
Sheff United,Chelsea,Loss
Southampton,Aston Villa,Draw
Tottenham,Bournemouth,Win
West Ham,Burnley,Draw
Wolves,Everton,Win
Brentford,Fulham,Win
Burnley,Leicester,Loss
Chelsea,Liverpool,Draw
Arsenal,Crystal Palace,Win
Aston Villa,Everton,Win
Bournemouth,Newcastle,Draw
Brentford,Tottenham,Loss
Brighton,Wolves,Win
Crystal Palace,Leicester,Win
Everton,Man City,Loss
Fulham,Man City,Loss
Leeds,Man United,Loss
Leicester,West Ham,Draw
Liverpool,"Nott'm Forest",Win
Man City,Southampton,Win
Man United,Burnley,Win
Newcastle,Arsenal,Loss
"Nott'm Forest",Aston Villa,Draw
Sheff United,Brentford,Loss
Southampton,Bournemouth,Win
Tottenham,Chelsea,Draw
West Ham,Crystal Palace,Win
Wolves,Fulham,Draw
Arsenal,Everton,Win
Aston Villa,Fulham,Win
Bournemouth,Liverpool,Loss
Brentford,Man City,Loss
Brighton,Man United,Loss
Burnley,Newcastle,Loss
Chelsea,Tottenham,Win
Crystal Palace,Southampton,Draw
Everton,"Nott'm Forest",Draw
Fulham,Leeds,Win
Leeds,Arsenal,Loss
Leicester,Aston Villa,Win
Liverpool,Brentford,Win
Man City,Brighton,Win
Man United,Chelsea,Win
Newcastle,West Ham,Win
"Nott'm Forest",Wolves,Draw
Sheff United,Crystal Palace,Loss
Southampton,Everton,Win
Tottenham,Leicester,Win
West Ham,Man United,Loss
Wolves,Bournemouth,Draw
Arsenal,Fulham,Win
Aston Villa,Crystal Palace,Win
Bournemouth,Everton,Draw
Brentford,Newcastle,Draw
Brighton,Leeds,Win
Burnley,Southampton,Draw
Chelsea,Man United,Draw
Crystal Palace,Tottenham,Loss
Everton,Liverpool,Loss
Fulham,Leicester,Draw
Leeds,Man City,Loss
Leicester,Man United,Loss
Liverpool,Arsenal,Win
Man City,Brentford,Win
Man United,West Ham,Win
Newcastle,Brighton,Draw
"Nott'm Forest",Burnley,Win
Sheff United,Tottenham,Loss
Southampton,Wolves,Win
Tottenham,Aston Villa,Win
West Ham,Everton,Win
Wolves,Crystal Palace,Draw
Arsenal,Man United,Draw
Aston Villa,Brighton,Draw
Bournemouth,Burnley,Win
Brentford,Chelsea,Loss
Brighton,Tottenham,Draw
Burnley,Crystal Palace,Win
Chelsea,Leeds,Win
Crystal Palace,Aston Villa,Draw
Everton,Southampton,Win
Fulham,"Nott'm Forest",Win
Leeds,Bournemouth,Win
Leicester,Man City,Loss
Liverpool,Wolves,Win
Man City,Everton,Win
Man United,Arsenal,Draw
Newcastle,Brentford,Win
"Nott'm Forest",Fulham,Draw
Sheff United,Liverpool,Loss
Southampton,Burnley,Draw
Tottenham,West Ham,Win
West Ham,Leicester,Loss
Wolves,Chelsea,Loss
Arsenal,West Ham,Win
Aston Villa,Man City,Loss
Bournemouth,"Nott'm Forest",Win
Brentford,Man United,Draw
Brighton,Everton,Win
Burnley,Aston Villa,Draw
Chelsea,Brighton,Win
Crystal Palace,Brentford,Draw
Everton,Burnley,Draw
Fulham,Southampton,Win
Leeds,Tottenham,Loss
Leicester,Arsenal,Loss
Liverpool,Newcastle,Win
Man City,Tottenham,Win
Man United,Liverpool,Draw
Newcastle,Sheff United,Win
"Nott'm Forest",Crystal Palace,Win
Sheff United,Fulham,Loss
Southampton,Man United,Draw
Tottenham,Leeds,Win
West Ham,Wolves,Draw
Wolves,Leicester,Win
Arsenal,Tottenham,Win
Aston Villa,Leeds,Win
Bournemouth,Brighton,Win
Brentford,Southampton,Win
Brighton,Fulham,Draw
Burnley,Man City,Loss
Chelsea,Everton,Win
Crystal Palace,Sheff United,Win
Everton,Crystal Palace,Win
Fulham,Burnley,Draw
Leeds,West Ham,Win
Leicester,Tottenham,Draw
Liverpool,Aston Villa,Win
Man City,Man United,Win
Man United,Newcastle,Draw
Newcastle,Leicester,Win
"Nott'm Forest",Bournemouth,Draw
Sheff United,Arsenal,Loss
Southampton,Brighton,Draw
Tottenham,Brentford,Win
West Ham,Chelsea,Draw
Wolves,Liverpool,Loss
Arsenal,Leicester,Win
Aston Villa,Burnley,Win
Bournemouth,Brentford,Draw
Brentford,Brighton,Win
Brighton,Southampton,Draw
Burnley,Man United,Loss
Chelsea,Wolves,Win
Crystal Palace,Fulham,Win
Everton,Leeds,Draw
Fulham,Aston Villa,Loss
Leeds,Crystal Palace,Loss
Leicester,Everton,Draw
Liverpool,Chelsea,Win
Man City,"Nott'm Forest",Win
Man United,Man City,Loss
Newcastle,Tottenham,Win
"Nott'm Forest",Tottenham,Draw
Sheff United,Bournemouth,Loss
Southampton,Arsenal,Draw
Tottenham,Man United,Draw
West Ham,Liverpool,Loss
Wolves,Newcastle,Loss
Arsenal,Brighton,Win
Aston Villa,Tottenham,Draw
Bournemouth,Chelsea,Loss
Brentford,Burnley,Win
Brighton,Aston Villa,Draw
Burnley,Leeds,Draw
Chelsea,Fulham,Win
Crystal Palace,West Ham,Draw
Everton,Bournemouth,Win
Fulham,Brentford,Win
Leeds,"Nott'm Forest",Win
Leicester,Crystal Palace,Draw
Liverpool,Man City,Draw
Man City,Arsenal,Win
Man United,Southampton,Win
Newcastle,Everton,Draw
"Nott'm Forest",Leicester,Win
Sheff United,Man United,Loss
Southampton,Newcastle,Draw
Tottenham,Sheff United,Win
West Ham,Brighton,Draw
Wolves,Burnley,Win
Arsenal,Crystal Palace,Win
Aston Villa,Southampton,Draw
Bournemouth,Aston Villa,Loss
Brentford,Wolves,Draw
Brighton,Liverpool,Loss
Burnley,Tottenham,Loss
Chelsea,Newcastle,Win
Crystal Palace,Man United,Loss
Everton,Brentford,Draw
Fulham,Everton,Win
Leeds,Leicester,Draw
Leicester,Brighton,Draw
Liverpool,Arsenal,Win
Man City,Chelsea,Draw
Man United,Man City,Draw
Newcastle,Fulham,Win
"Nott'm Forest",West Ham,Win
Sheff United,"Nott'm Forest",Loss
Southampton,Sheff United,Win
Tottenham,Crystal Palace,Win
West Ham,Leeds,Win
Wolves,Bournemouth,Win
Arsenal,Everton,Win
Aston Villa,Newcastle,Win
Bournemouth,Fulham,Win
Brentford,Leeds,Win
Brighton,Chelsea,Draw
Burnley,Arsenal,Loss
Chelsea,Brentford,Win
Crystal Palace,Bournemouth,Win
Everton,Aston Villa,Loss
Fulham,Liverpool,Loss
Leeds,Tottenham,Loss
Leicester,Southampton,Win
Liverpool,Burnley,Win
Man City,Wolves,Win
Man United,Crystal Palace,Win
Newcastle,Man City,Loss
"Nott'm Forest",Man United,Draw
Sheff United,Leicester,Loss
Southampton,Everton,Draw
Tottenham,Brighton,Win
West Ham,"Nott'm Forest",Draw
Wolves,West Ham,Draw
Arsenal,Bournemouth,Win
Aston Villa,Man United,Loss
Bournemouth,Chelsea,Loss
Brentford,Tottenham,Loss
Brighton,Burnley,Win
Burnley,Aston Villa,Loss
Chelsea,Liverpool,Draw
Crystal Palace,Fulham,Draw
Everton,Man City,Loss
Fulham,Arsenal,Loss
Leeds,Brentford,Draw
Leicester,Newcastle,Draw
Liverpool,Everton,Win
Man City,Sheff United,Win
Man United,Leicester,Win
Newcastle,"Nott'm Forest",Win
"Nott'm Forest",Southampton,Win
Sheff United,West Ham,Loss
Southampton,Crystal Palace,Loss
Tottenham,Chelsea,Win
West Ham,Brighton,Draw
Wolves,Leeds,Draw
Arsenal,Man City,Loss
Aston Villa,Everton,Win
Bournemouth,Tottenham,Loss
Brentford,Leicester,Draw
Brighton,Crystal Palace,Draw
Burnley,Wolves,Draw
Chelsea,Aston Villa,Win
Crystal Palace,"Nott'm Forest",Draw
Everton,Arsenal,Loss
Fulham,Man United,Loss
Leeds,Southampton,Win
Leicester,Burnley,Win
Liverpool,Fulham,Win
Man City,Brighton,Win
Man United,Brentford,Win
Newcastle,Leeds,Draw
"Nott'm Forest",Sheff United,Win
Sheff United,Bournemouth,Loss
Southampton,Tottenham,Loss
Tottenham,Newcastle,Draw
West Ham,Arsenal,Loss
Wolves,Everton,Draw
Arsenal,"Nott'm Forest",Win
Aston Villa,Sheff United,Win
Bournemouth,Southampton,Win
Brentford,West Ham,Win
Brighton,Man United,Loss
Burnley,Chelsea,Loss
Chelsea,Fulham,Win
Crystal Palace,Leeds,Draw
Everton,Man United,Loss
Fulham,Liverpool,Loss
Leeds,Burnley,Win
Leicester,Brighton,Draw
Liverpool,Tottenham,Win
Man City,Aston Villa,Win
Man United,Everton,Win
Newcastle,Brentford,Win
"Nott'm Forest",Man City,Loss
Sheff United,Crystal Palace,Draw
Southampton,Leicester,Loss
Tottenham,Bournemouth,Win
West Ham,Arsenal,Loss
Wolves,Man United,Loss
Arsenal,Wolves,Win
Aston Villa,Chelsea,Draw
Bournemouth,Man City,Loss
Brentford,Liverpool,Loss
Brighton,Sheff United,Win
Burnley,"Nott'm Forest",Draw
Chelsea,Crystal Palace,Win
Crystal Palace,Everton,Draw
Everton,Brentford,Draw
Fulham,West Ham,Draw
Leeds,Bournemouth,Win
Leicester,Tottenham,Draw
Liverpool,Aston Villa,Win
Man City,Leeds,Win
Man United,Fulham,Win
Newcastle,Arsenal,Loss
"Nott'm Forest",Burnley,Draw
Sheff United,Southampton,Loss
Southampton,Man City,Loss
Tottenham,Man United,Draw
West Ham,Leicester,Win
Wolves,Brighton,Win
Arsenal,Southampton,Win
Aston Villa,Liverpool,Loss
Bournemouth,Leicester,Win
Brentford,Brighton,Draw
Brighton,Brentford,Draw
Burnley,Wolves,Loss
Chelsea,Aston Villa,Win
Crystal Palace,Arsenal,Loss
Everton,Newcastle,Win
Fulham,Sheff United,Win
Leeds,Everton,Draw
Leicester,Man City,Loss
Liverpool,Man United,Draw
Man City,Tottenham,Win
Man United,Chelsea,Draw
Newcastle,Crystal Palace,Win
"Nott'm Forest",Bournemouth,Win
Sheff United,Burnley,Win
Southampton,Fulham,Win
Tottenham,Leeds,Win
West Ham,Brentford,Draw
Wolves,"Nott'm Forest",Win
Arsenal,West Ham,Win
Aston Villa,Burnley,Win
Bournemouth,Brentford,Win
Brentford,Crystal Palace,Win
Brighton,Newcastle,Draw
Burnley,Brighton,Draw
Chelsea,Man City,Draw
Crystal Palace,Southampton,Win
Everton,Fulham,Draw
Fulham,Aston Villa,Draw
Leeds,Man United,Loss
Leicester,Wolves,Win
Liverpool,Everton,Win
Man City,Bournemouth,Win
Man United,Tottenham,Win
Newcastle,Tottenham,Draw
"Nott'm Forest",Arsenal,Loss
Sheff United,Chelsea,Loss
Southampton,Brentford,Draw
Tottenham,Liverpool,Loss
West Ham,Man United,Loss
Wolves,Crystal Palace,Win
Arsenal,Man United,Win
Aston Villa,Brighton,Win
Bournemouth,Everton,Draw
Brentford,Fulham,Draw
Brighton,Wolves,Draw
Burnley,Southampton,Draw
Chelsea,Leicester,Win
Crystal Palace,"Nott'm Forest",Draw
Everton,Burnley,Draw
Fulham,Chelsea,Loss
Leeds,Arsenal,Loss
Leicester,Aston Villa,Draw
Liverpool,Sheff United,Win
Man City,Man United,Win
Man United,Newcastle,Win
Newcastle,Man City,Loss
"Nott'm Forest",Leeds,Win
Sheff United,Tottenham,Loss
Southampton,Liverpool,Loss
Tottenham,Brentford,Win
West Ham,Crystal Palace,Draw
Wolves,Bournemouth,Draw
Arsenal,Brentford,Win
Aston Villa,Tottenham,Win
Bournemouth,Brighton,Win
Brentford,Everton,Draw
Brighton,Man United,Loss
Burnley,Fulham,Draw
Chelsea,Arsenal,Draw
Crystal Palace,Leeds,Win
Everton,Southampton,Win
Fulham,Leicester,Draw
Leeds,Newcastle,Win
Leicester,Sheff United,Win
Liverpool,"Nott'm Forest",Win
Man City,Wolves,Win
Man United,Aston Villa,Win
Newcastle,Burnley,Win
"Nott'm Forest",Crystal Palace,Win
Sheff United,Everton,Loss
Southampton,West Ham,Draw
Tottenham,Chelsea,Draw
West Ham,Liverpool,Loss
Wolves,Brentford,Draw
Arsenal,Chelsea,Win
Aston Villa,Man United,Draw
Bournemouth,Burnley,Win
Brentford,Newcastle,Draw
Brighton,Arsenal,Loss
Burnley,Brighton,Draw
Chelsea,Tottenham,Draw
Crystal Palace,Everton,Draw
Everton,Wolves,Win
Fulham,Leicester,Draw
Leeds,Aston Villa,Loss
Leicester,Fulham,Win
Liverpool,Leeds,Win
Man City,"Nott'm Forest",Win
Man United,Liverpool,Loss
Newcastle,Southampton,Draw
"Nott'm Forest",Brentford,Win
Sheff United,Man City,Loss
Southampton,Burnley,Win
Tottenham,Aston Villa,Draw
West Ham,Bournemouth,Win
Wolves,Sheff United,Win
Arsenal,Aston Villa,Win
Bournemouth,Man United,Loss
Brentford,Burnley,Win
Brighton,Fulham,Win
Burnley,Arsenal,Loss
Chelsea,Crystal Palace,Win
Crystal Palace,Brentford,Draw
Everton,Leeds,Win
Fulham,Man City,Loss
Leeds,Leicester,Win
Leicester,Tottenham,Draw
Liverpool,Newcastle,Win
Man City,Chelsea,Win
Man United,Everton,Win
Newcastle,Tottenham,Draw
"Nott'm Forest",Southampton,Draw
Sheff United,Aston Villa,Loss
Southampton,Man United,Draw
Tottenham,Wolves,Draw
West Ham,Bournemouth,Win
Wolves,Brighton,Draw
Arsenal,Man United,Win
Aston Villa,Bournemouth,Win
Bournemouth,Brentford,Draw
Brentford,Brighton,Draw
Brighton,Leicester,Win
Burnley,Liverpool,Loss
Chelsea,Everton,Win
Crystal Palace,Tottenham,Loss
Everton,Southampton,Win
Fulham,"Nott'm Forest",Win
Leeds,Man City,Loss
Leicester,Arsenal,Loss
Liverpool,Aston Villa,Win
Man City,Fulham,Win
Man United,West Ham,Win
Newcastle,Wolves,Win
"Nott'm Forest",Crystal Palace,Draw
Sheff United,Leeds,Win
Southampton,Burnley,Win
Tottenham,Chelsea,Draw
West Ham,Newcastle,Draw
Wolves,Sheff United,Win
Arsenal,Aston Villa,Win
Bournemouth,Brighton,Win
Brentford,Chelsea,Loss
Brighton,Everton,Win
Burnley,Leeds,Win
Chelsea,West Ham,Win
Crystal Palace,Fulham,Draw
Everton,Man United,Loss
Fulham,"Nott'm Forest",Draw
Leeds,Southampton,Win
Leicester,Tottenham,Draw
Liverpool,Burnley,Win
Man City,Arsenal,Draw
Man United,Tottenham,Win
Newcastle,Man City,Loss
"Nott'm Forest",Leicester,Win
Sheff United,Wolves,Win
Southampton,Brentford,Win
Tottenham,Crystal Palace,Win
West Ham,Aston Villa,Draw
Wolves,Newcastle,Draw
Arsenal,Liverpool,Loss
Aston Villa,Brighton,Win
Bournemouth,Man City,Loss
Brentford,Chelsea,Loss
Brighton,Burnley,Win
Burnley,Tottenham,Loss
Chelsea,Crystal Palace,Win
Crystal Palace,Southampton,Draw
Everton,Leicester,Win
Fulham,Leeds,Draw
Leeds,West Ham,Win
Leicester,Man United,Loss
Liverpool,Tottenham,Win
Man City,Everton,Win
Man United,Arsenal,Draw
Newcastle,Fulham,Draw
"Nott'm Forest",Aston Villa,Draw
Sheff United,Newcastle,Draw
Southampton,Bournemouth,Win
Tottenham,Brentford,Draw
West Ham,Man City,Loss
Wolves,"Nott'm Forest",Win
Arsenal,Tottenham,Win
Aston Villa,Everton,Win
Bournemouth,Crystal Palace,Draw
Brentford,Leicester,Draw
Brighton,Southampton,Win
Burnley,Man United,Loss
Chelsea,Leeds,Win
Crystal Palace,Newcastle,Draw
Everton,Wolves,Draw
Fulham,Brighton,Draw
Leeds,Man United,Loss
Leicester,Liverpool,Loss
Liverpool,Man City,Loss
Man City,Chelsea,Win
Man United,Crystal Palace,Win
Newcastle,Aston Villa,Win
"Nott'm Forest",Burnley,Win
Sheff United,Arsenal,Loss
Southampton,West Ham,Draw
Tottenham,Fulham,Win
West Ham,Brentford,Win
Wolves,Bournemouth,Win
Arsenal,Fulham,Win
Aston Villa,Burnley,Draw
Bournemouth,West Ham,Draw
Brentford,Brighton,Draw
Brighton,Chelsea,Draw
Burnley,"Nott'm Forest",Win
Chelsea,Southampton,Win
Crystal Palace,Leeds,Win
Everton,Tottenham,Draw
Fulham,Man United,Loss
Leeds,Leicester,Draw
Leicester,Crystal Palace,Draw
Liverpool,Everton,Win
Man City,Newcastle,Win
Man United,Man City,Loss
Newcastle,Brentford,Win
"Nott'm Forest",Wolves,Draw
Sheff United,Aston Villa,Loss
Southampton,Tottenham,Loss
Tottenham,Arsenal,Loss
West Ham,Liverpool,Loss
Wolves,Sheff United,Win
Arsenal,Liverpool,Win
Aston Villa,Southampton,Win
Bournemouth,Leicester,Win
Brentford,Man City,Loss
Brighton,Leeds,Draw
Burnley,Everton,Draw
Chelsea,Man United,Draw
Crystal Palace,Aston Villa,Draw
Everton,Brighton,Draw
Fulham,Wolves,Win
Leeds,Burnley,Win
Leicester,"Nott'm Forest",Draw
Liverpool,Chelsea,Win
Man City,Tottenham,Win
Man United,Bournemouth,Win
Newcastle,Sheffield United,Win
"Nott'm Forest",West Ham,Draw
Sheff United,Brentford,Loss
Southampton,Arsenal,Draw
Tottenham,Newcastle,Draw
West Ham,Fulham,Draw
Wolves,Crystal Palace,Draw
Arsenal,Man City,Loss
Aston Villa,Fulham,Win
Bournemouth,Leeds,Win
Brentford,Man United,Draw
Brighton,Crystal Palace,Draw
Burnley,West Ham,Draw
Chelsea,"Nott'm Forest",Win
Crystal Palace,Everton,Draw
Everton,Leicester,Win
Fulham,Tottenham,Loss
Leeds,Brighton,Draw
Leicester,Newcastle,Draw
Liverpool,Southampton,Win
Man City,Aston Villa,Win
Man United,Burnley,Win
Newcastle,Man United,Loss
"Nott'm Forest",Liverpool,Loss
Sheff United,Everton,Draw
Southampton,Arsenal,Draw
Tottenham,Man City,Loss
West Ham,Leeds,Win
Wolves,Chelsea,Loss
Arsenal,Everton,Win
Aston Villa,Leicester,Win
Bournemouth,Arsenal,Loss
Brentford,Sheff United,Win
Brighton,Man City,Loss
Burnley,Chelsea,Loss
Chelsea,Southampton,Win
Crystal Palace,Tottenham,Draw
Everton,Brighton,Draw
Fulham,Brentford,Draw
Leeds,Wolves,Win
Leicester,Bournemouth,Win
Liverpool,Crystal Palace,Win
Man City,Man United,Draw
Man United,"Nott'm Forest",Win
Newcastle,Liverpool,Draw
"Nott'm Forest",West Ham,Draw
Sheff United,Tottenham,Loss
Southampton,Aston Villa,Loss
Tottenham,Burnley,Win
West Ham,Fulham,Draw
Wolves,Leeds,Win
Arsenal,Burnley,Win
Aston Villa,Liverpool,Loss
Bournemouth,Southampton,Win
Brentford,Fulham,Win
Brighton,Man City,Loss
Burnley,Leicester,Draw
Chelsea,Bournemouth,Win
Crystal Palace,Aston Villa,Draw
Everton,Newcastle,Win
Fulham,Brighton,Draw
Leeds,Crystal Palace,Win
Leicester,Tottenham,Draw
Liverpool,Everton,Win
Man City,West Ham,Win
Man United,Leeds,Win
Newcastle,Arsenal,Draw
"Nott'm Forest",Man United,Draw
Sheff United,"Nott'm Forest",Draw
Southampton,Man City,Loss
Tottenham,Southampton,Win
West Ham,Burnley,Draw
Wolves,Brentford,Draw"""
with open("data/predicted_2025_2026_season_results.csv", "w") as f:
    f.write(predicted_results_csv_content)

streamlit_app_content = """import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Man United 2025-26 Season Predictor",
    page_icon="🔴",
    layout="wide"
)

# Title
st.title("🔴 Manchester United 2025-26 Season Predictor")
st.markdown(f"**Today:** {datetime.now().strftime('%B %d, %Y')} | A 50-Team Super Premier League Simulation")

# Load data
@st.cache_data
def load_data():
    prob = pd.read_csv("data/mu_win_probability_2025_2026_by_opponent.csv")
    results = pd.read_csv("data/predicted_2025_2026_season_results.csv")

    # Fix team names
    name_fix = {"Nott'm Forest": "Nottingham Forest", "Man United": "Manchester United", "Man City": "Manchester City"}
    prob["Opponent"] = prob["Opponent"].replace(name_fix)
    results["HomeTeam"] = results["HomeTeam"].replace(name_fix)
    results["AwayTeam"] = results["AwayTeam"].replace(name_fix)

    return prob, results

prob_df, results_df = load_data()

# ====================== SIDEBAR ======================
st.sidebar.header("🔍 Explore")
view_mode = st.sidebar.radio("View Mode", ["Manchester United Focus", "Full League Table", "Any Team", "Monte Carlo"])

# ====================== 1. MAN UNITED FOCUS ======================
if view_mode == "Manchester United Focus":
    st.header("🔴 Manchester United 2025-26 Fixtures & Probabilities")

    # Get MU home & away games
    mu_home = results_df[results_df["HomeTeam"] == "Manchester United"].copy()
    mu_away = results_df[results_df["AwayTeam"] == "Manchester United"].copy()

    # Merge probabilities
    mu_home = mu_home.merge(
        prob_df[prob_df["Is_Home"] == 1],
        left_on="AwayTeam", right_on="Opponent", how="left"
    )
    mu_away = mu_away.merge(
        prob_df[prob_df["Is_Home"] == 0],
        left_on="HomeTeam", right_on="Opponent", how="left"
    )

    # Combine
    fixtures = pd.concat([
        mu_home[["HomeTeam", "AwayTeam", "Predicted_Result", "Prob_Avg_pct"]].rename(
            columns={"HomeTeam": "Venue", "AwayTeam": "Opponent", "Prob_Avg_pct": "Win_Prob_%"}
        ),
        mu_away[["AwayTeam", "HomeTeam", "Predicted_Result", "Prob_Avg_pct"]].rename(
            columns={"AwayTeam": "Venue", "HomeTeam": "Opponent", "Prob_Avg_pct": "Win_Prob_%"}
        )
    ]).reset_index(drop=True)

    fixtures["Venue"] = fixtures["Venue"].apply(lambda x: "Home" if x == "Manchester United" else "Away")
    fixtures = fixtures[["Venue", "Opponent", "Win_Prob_%", "Predicted_Result"]]
    fixtures["Win_Prob_%"] = fixtures["Win_Prob_%"]

    # Color coding
    def color_result(val):
        color = "green" if val == "Win" else "orange" if val == "Draw" else "red"
        return f'background-color: {color}; color: white'

    st.dataframe(
        fixtures.style.map(color_result, subset=["Predicted_Result"]),
        width='stretch'
    )

    col1, col2, col3 = st.columns(3)
    wins = len(fixtures[fixtures["Predicted_Result"] == "Win"])
    draws = len(fixtures[fixtures["Predicted_Result"] == "Draw"])
    losses = len(fixtures[fixtures["Predicted_Result"] == "Loss"])

    col1.metric("Predicted Wins", wins, f"{wins*3} pts from wins")
    col2.metric("Draws", draws, f"+{draws} pts")
    col3.metric("Losses", losses)

    total_pts = wins * 3 + draws
    st.success(f"**Expected Points (Most Likely Outcome): {total_pts}**")

# ====================== 2. FULL LEAGUE TABLE ======================
elif view_mode == "Full League Table":
    st.header("🏆 Predicted 2025-26 Premier League Table")

    points = {}
    P = {}
    for _, row in results_df.iterrows():
        h, a, res = row["HomeTeam"], row["AwayTeam"], row["Predicted_Result"]
        for team in [h, a]:
            points[team] = points.get(team, 0)
            P[team] = P.get(team, 0) + 1

        if res == "Win":
            points[h] += 3
        elif res == "Draw":
            points[h] += 1
            points[a] += 1
        else:  # Loss → away wins
            points[a] += 3

    table = pd.DataFrame({
        "Team": points.keys(),
        "Pts": points.values(),
        "P": P.values()
    }).sort_values("Pts", ascending=False).reset_index(drop=True)
    table.index += 1

    st.dataframe(table.head(20), width='stretch')

    fig = px.bar(table.head(15), x="Team", y="Pts", title="Top 15 Predicted Finish")
    st.plotly_chart(fig, width='stretch')

# ====================== 3. ANY TEAM ======================
elif view_mode == "Any Team":
    team = st.selectbox("Select Team", sorted(results_df["HomeTeam"].unique()))
    st.header(f"{team} 2025-26 Season")

    home_games = results_df[results_df["HomeTeam"] == team]
    away_games = results_df[results_df["AwayTeam"] == team]

    # Predicted result from team's perspective
    def get_result(row, team):
        if row["HomeTeam"] == team:
            return row["Predicted_Result"]
        else:
            return "Win" if row["Predicted_Result"] == "Loss" else "Loss" if row["Predicted_Result"] == "Win" else "Draw"

    fixtures = []
    for _, row in home_games.iterrows():
        fixtures.append({"Opponent": row["AwayTeam"], "Venue": "Home", "Result": row["Predicted_Result"]})
    for _, row in away_games.iterrows():
        fixtures.append({"Opponent": row["HomeTeam"], "Venue": "Away", "Result": get_result(row, team)})

    df = pd.DataFrame(fixtures)
    wins = len(df[df["Result"] == "Win"])
    pts = wins * 3 + len(df[df["Result"] == "Draw"])

    col1, col2 = st.columns(2)
    col1.metric("Wins", wins)
    col2.metric("Total Points", pts)

    st.dataframe(df, width='stretch')

# ====================== 4. MONTE CARLO ======================
else:
    st.header("🎲 Monte Carlo Simulation (10,000 Seasons)")

    if st.button("Run Simulation"):
        n = 10000
        points_list = []

        with st.spinner("Simulating 10,000 seasons..."):
            for _ in range(n):
                points = 0
                for _, row in prob_df.iterrows():
                    p_win = row["Prob_Avg"]
                    p_draw = 0.22  # realistic draw rate
                    p_loss = 1 - p_win - p_draw

                    outcome = np.random.choice(["Win", "Draw", "Loss"], p=[p_win, p_draw, p_loss])
                    points += 3 if outcome == "Win" else 1 if outcome == "Draw" else 0
                points_list.append(points)

        avg_pts = np.mean(points_list)
        top4 = np.percentile(points_list, 95)
        title = len([p for p in points_list if p >= 95]) / n * 100

        col1, col2, col3 = st.columns(3)
        col1.metric("Average Points", f"{avg_pts:.1f}")
        col2.metric("Top 4 Chance (≥{top4})", f"{sum(p >= top4 for p in points_list)/n:.1%}")
        col3.metric("Title Chance (1st)", f"{title:.2f}%")

        fig = px.histogram(points_list, nbins=40, title="Man United Points Distribution")
        fig.add_vline(x=avg_pts, line_color="red", annotation_text="Average")
        st.plotly_chart(fig, width='stretch')

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using real ML models trained on 30++ years of Man United data")"""
with open("app.py", "w") as f:
    f.write(streamlit_app_content)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using real ML models trained on 30+ years of Man United data")
