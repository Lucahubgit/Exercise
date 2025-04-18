import streamlit as st
import pandas as pd

# SCELTA DELLA DATA

# Inserimento della data del match
st.subheader("Insert the match date")
st.session_state.match_date = st.date_input("Match date", st.session_state.match_date)

# Formatta la data come stringa (es. "13-04-2025") e salvala in session_state
if st.session_state.match_date:
    st.session_state.date_str = st.session_state.match_date.strftime("%d-%m-%Y")

# Button next page
st.subheader("Go to the next page")
if st.button("Next"):
    st.switch_page("pages/score.py")
