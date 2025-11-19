import streamlit as st
import pandas as pd
import joblib
import os

# Page config
st.set_page_config(page_title="Man Utd AI Predictor", page_icon="🔴", layout="centered")

# Load model & feature list
@st.cache_resource
def load_model():
    model = joblib.load('model/man_utd_model.pkl')
    features = joblib.load('model/feature_columns.pkl')
    return model, features

model, feature_cols = load_model()

# Title
st.title("🔴 Manchester United Match Predictor")
st.markdown("**AI-powered prediction using your custom-engineered features**")

# User inputs - map to your exact feature columns
st.subheader("Next Match Details")

col1, col2 = st.columns(2)
with col1:
    is_home = st.selectbox("Venue", ["Home (Old Trafford)", "Away"])
    home_advantage = 1 if "Home" in is_home else 0

with col2:
    opponent_input = st.text_input("Opponent", "Liverpool")

# You need to map your features — here are common ones from typical datasets
# Adjust these default values based on current 2025/26 season form!
with st.expander("Advanced: Current Form & Stats (edit as needed)"):
    mu_form_5 = st.slider("Man Utd points last 5 matches", 0, 15, 10)
    mu_goals_scored_5 = st.slider("Man Utd goals scored last 5", 0, 20, 9)
    mu_goals_conceded_5 = st.slider("Man Utd goals conceded last 5", 0, 20, 6)
    opp_form_5 = st.slider("Opponent points last 5", 0, 15, 7)
    mu_elo = st.number_input("Man Utd current ELO rating", 1700, 2000, 1850)
    opp_elo = st.number_input("Opponent ELO rating", 1600, 2000, 1880)

# Create input dataframe matching exact training features
input_data = {}
# Put the values — make sure column names EXACTLY match your CSV!
# Replace these with your actual column names from df.columns in Colab

input_data['IsHome'] = home_advantage
input_data['MU_Form_Pts_Last5'] = mu_form_5
input_data['MU_GS_Last5'] = mu_goals_scored_5
input_data['MU_GC_Last5'] = mu_goals_conceded_5
input_data['Opp_Form_Pts_Last5'] = opp_form_5
input_data['MU_ELO'] = mu_elo
input_data['Opp_ELO'] = opp_elo
# Add more if your dataset has them (e.g., Rest_Days, etc.)

# Fill missing features with reasonable defaults (or 0)
for col in feature_cols:
    if col not in input_data:
        input_data[col] = 0  # or median from training data

input_df = pd.DataFrame([input_data])[feature_cols]  # enforce order

if st.button("🔮 Predict Result", type="primary"):
    probs = model.predict_proba(input_df)[0]
    pred = model.predict(input_df)[0]

    result_map = {-1: "Loss 😢", 0: "Draw 🤝", 1: "Win 🏆"}
    prob_map = {-1: probs[0], 0: probs[1] if len(probs)>2 else probs[1], 1: probs[2] if len(probs)>2 else probs[1]}

    st.success(f"### Predicted: **{result_map[pred]}**")

    chart_data = pd.DataFrame({
        "Outcome": ["Win 🏆", "Draw 🤝", "Loss 😢"],
        "Probability": [prob_map[1], prob_map[0], prob_map[-1]]
    })
    st.bar_chart(chart_data.set_index("Outcome"))

    st.caption(f"Win: {prob_map[1]:.1%} | Draw: {prob_map[0]:.1%} | Loss: {prob_map[-1]:.1%}")

st.markdown("---")
st.caption("Built using your custom Manchester United ML dataset • Model: Random Forest • 2025")
