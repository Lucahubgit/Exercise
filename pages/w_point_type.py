import streamlit as st
import pandas as pd

# SCELTA TEAM POINT OR OPPPONENT ERROR

# Passo 2

st.subheader("Due to?")

if st.button("Team point"):
    st.session_state.df.loc[st.session_state.current_row, "point_type"] = "Team point"
    st.switch_page("pages/player.py")

if st.button("Opponent error"):
    st.session_state.df.loc[st.session_state.current_row, "point_type"] = "Opponent error"
    st.switch_page("pages/player.py")

st.subheader("Go back to the intial page")
if st.button("Back"):
    st.switch_page("pages/page2.py")