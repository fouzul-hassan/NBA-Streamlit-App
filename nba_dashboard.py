import streamlit as st
import pandas as pd
st.title("🏀 NBA Play-by-Play Analysis Dashboard")
st.subheader("Visualizing Team and Player Performance across Matches")
st.markdown("**Prepared for CMM705 - Big Data Programming (2024/25)**")

st.header("⏱️ Most Scoring Quarter per Team")
df_quarters = pd.read_csv("most_scoring_quarters.csv")
st.dataframe(df_quarters)

fig = px.bar(df_quarters, x="Team", y="Score", color="Quarter", barmode="group", title="Highest Scoring Quarter for Each Team")
st.plotly_chart(fig)

st.header("🔥 Top 5 Teams by Total Points")
df_top_teams = pd.read_csv("top_5_teams.csv")
st.dataframe(df_top_teams)

fig = px.bar(df_top_teams, x="Total_Points", y="Team", orientation="h", title="Top 5 Teams by Score")
st.plotly_chart(fig)

st.header("🔥 Top 5 Teams by Total Points")
df_top_teams = pd.read_csv("top_5_teams.csv")
st.dataframe(df_top_teams)

fig = px.bar(df_top_teams, x="Total_Points", y="Team", orientation="h", title="Top 5 Teams by Score")
st.plotly_chart(fig)

st.header("💪 Players with 40+ Points in a Game")
df_40plus = pd.read_csv("players_40_or_more.csv")
st.dataframe(df_40plus[['Player', 'Game_ID', 'Total_Points']].head(10))

percent = (len(df_40plus) / len(df)) * 100
st.metric(label="Percentage of 40+ Point Games", value=f"{percent:.2f}%")

st.header("🏁 Team Match Outcomes")
df_summary = pd.read_csv("summary_df.csv")
st.dataframe(df_summary)

fig = px.bar(df_summary, x="Team", y=["Win", "Loss"], title="Team Wins vs Losses", barmode="stack")
st.plotly_chart(fig)

st.markdown("**Top Scorer per Team**")
st.dataframe(df_summary[['Team', 'Top_Scorer']])
