import streamlit as st
import pandas as pd

# SCELTA PUNTO FATTO O SUBITO

# Passo 1
st.subheader("What happened?")

if st.button("Point scored"):
    st.session_state.df.loc[st.session_state.current_row, "step1"] = "Point scored"
    st.switch_page("pages/w_point_type.py")

if st.button("Point lost"):
    st.session_state.df.loc[st.session_state.current_row, "step1"] = "Point lost"
    st.switch_page("pages/w_point_type.py")

# Salva il DataFrame in un file Excel
st.subheader("Save the match")
if st.button("Save on Excel"):
    #st.session_state.df.to_excel("Match.xlsx", index=False)  # Salva il file Excel
    st.session_state.df.to_excel(f"Match_{st.session_state.date_str}.xlsx", index=False)
    st.success("File Excel updated and saved")
    # Reset the DataFrame and current row
    st.session_state.df = pd.DataFrame(columns=st.session_state.df.columns)
    st.session_state.current_row = 0