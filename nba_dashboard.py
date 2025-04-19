import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NBA Dashboard", layout="wide")

# --------------------
# Header
# --------------------
st.title("🏀 NBA Play-by-Play Analysis Dashboard")
# st.subheader("CMM705 - Big Data Programming Coursework (2024/25)")
st.markdown("This dashboard presents key insights from historical NBA play-by-play data, including team performance, player highlights, and match outcomes.")

# --------------------
# Load Data
# --------------------
@st.cache_data
def load_data():
    df_quarters = pd.read_csv("most_scoring_quarters.csv")
    df_top_teams = pd.read_csv("top_5_teams.csv")
    df_players_40 = pd.read_csv("players_40_or_more.csv")
    df_summary = pd.read_csv("summary_df.csv")
    return df_quarters, df_top_teams, df_players_40, df_summary

df_quarters, df_top_teams, df_players_40, df_summary = load_data()

# --------------------
# Most Scoring Quarter
# --------------------
st.header("⏱️ Most Scoring Quarter per Team")

print(df_quarters.columns)
col1, col2 = st.columns([1, 2])
with col1:
    st.dataframe(df_quarters.drop(columns=['Unnamed: 0']))
with col2:
    fig1 = px.bar(df_quarters, x="Team", y="Score", color="Quarter", barmode="group",
                  title="Highest Scoring Quarter for Each Team")
    st.plotly_chart(fig1, use_container_width=True)

# --------------------
# Top 5 Teams by Points
# --------------------
st.header("🔥 Top 5 Teams by Total Points Scored")

col3, col4 = st.columns([1, 2])
with col3:
    st.dataframe(df_top_teams.drop(columns=['Unnamed: 0']))
with col4:
    fig2 = px.bar(df_top_teams, x="Total_Points", y="Team", orientation="h",
                  title="Top 5 Scoring Teams", text_auto=True)
    st.plotly_chart(fig2, use_container_width=True)

# --------------------
# Players with 40+ Points
# --------------------
st.header("💪 Players Who Scored 40+ Points in a Match")

col5, col6 = st.columns([1, 2])
with col5:
    st.metric("Total Players (40+)", value=len(df_players_40))
    percentage = (len(df_players_40) /  df_players_40["Player"].nunique()) * 100
    st.metric("Percentage of 40+ Point Performances", value=f"{percentage:.2f}%")
    st.dataframe(df_players_40[['Player', 'Game_ID', 'Total_Points']].head(10))
with col6:
    fig3 = px.histogram(df_players_40.head(20), x="Player", y="Total_Points", title="Top 40+ Point Scorers",
                        color="Player")
    st.plotly_chart(fig3, use_container_width=True)

# --------------------
# Team Wins and Losses
# --------------------
st.header("🏁 Team Match Outcomes & Top Scorers")

col7, col8 = st.columns([1, 2])
with col7:
    st.dataframe(df_summary.drop(columns=['Unnamed: 0']))
with col8:
    fig4 = px.bar(df_summary, x="Team", y=["Win", "Loss"], barmode="stack",
                  title="Wins and Losses per Team")
    st.plotly_chart(fig4, use_container_width=True)

# st.markdown("### 🎯 Top Scorer per Team")
# st.dataframe(df_summary[['Team', 'Top_Scorer']])

# --------------------
# Footer
# --------------------
st.markdown("---")
st.markdown("🔍 *All data and analysis are somewhat static and sourced from prepared CSV files and this dashboard is related with CMM705 - Big Data Programming Coursework.*")
