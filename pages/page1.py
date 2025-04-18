import streamlit as st
import pandas as pd

# DATA

# Inserimento della data del match
st.subheader("Insert the match date")
st.session_state.match_date = st.date_input("Match date", st.session_state.match_date)

# Formatta la data come stringa (es. "2025-04-13") e salvala in session_state
if st.session_state.match_date:
    st.session_state.date_str = st.session_state.match_date.strftime("%d-%m-%Y")


st.subheader("Go to the next page")
if st.button("Next"):
    st.switch_page("pages/page2.py")
