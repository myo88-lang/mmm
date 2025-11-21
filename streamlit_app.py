# app.py
import streamlit as st
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
    fixtures["Win_Prob_%"] = fixtures["Win_Prob_%"].round(1)

    # Color coding
    def color_result(val):
        color = "green" if val == "Win" else "orange" if val == "Draw" else "red"
        return f'background-color: {color}; color: white'

    st.dataframe(
        fixtures.style.applymap(color_result, subset=["Predicted_Result"]),
        use_container_width=True
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
    played P = {}
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

    st.dataframe(table.head(20), use_container_width=True)

    fig = px.bar(table.head(15), x="Team", y="Pts", title="Top 15 Predicted Finish")
    st.plotly_chart(fig, use_container_width=True)

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

    st.dataframe(df, use_container_width=True)

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
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using real ML models trained on 30+ years of Man United data")
