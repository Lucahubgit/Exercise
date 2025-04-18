import streamlit as st
import pandas as pd

# SCELTA PLAYER IN CASO DI PUNTO GUADAGNATO

st.subheader("Select the player involved")

if st.button("Number 1"):
    st.session_state.df.loc[st.session_state.current_row, "player"] = "Number 1"
    st.switch_page("pages/w_court.py")

if st.button("Number 2"):
    st.session_state.df.loc[st.session_state.current_row, "player"] = "Number 2"
    st.switch_page("pages/w_court.py")

if st.button("Number 3"):
    st.session_state.df.loc[st.session_state.current_row, "player"] = "Number 3"
    st.switch_page("pages/w_court.py")

if st.button("Number 4"):
    st.session_state.df.loc[st.session_state.current_row, "player"] = "Number 4"
    st.switch_page("pages/w_court.py")

if st.button("Number 5"):
    st.session_state.df.loc[st.session_state.current_row, "player"] = "Number 5"
    st.switch_page("pages/w_court.py")

if st.button("Number 6"):
    st.session_state.df.loc[st.session_state.current_row, "player"] = "Number 6"
    st.switch_page("pages/w_court.py")

# Tasto score page
st.subheader("Go to the initial page")
if st.button("Back"):
    st.switch_page("pages/score.py")