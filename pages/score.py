import streamlit as st
import pandas as pd

# SCELTA PUNTO GUADAGNATO O PERSO E SALVATAGGIO FILE EXCEL

st.subheader("What happened?")

if st.button("Point scored"):
    st.session_state.df.loc[st.session_state.current_row, "score"] = "Point scored"
    st.switch_page("pages/w_point_type.py")

if st.button("Point lost"):
    st.session_state.df.loc[st.session_state.current_row, "score"] = "Point lost"
    st.switch_page("pages/l_player.py")

# Salva il DataFrame in un file Excel
st.subheader("Save the match")
if st.button("Save on Excel"):
    st.session_state.df.to_excel(f"Match_{st.session_state.date_str}.xlsx", index=False)
    st.success("File Excel updated and saved")
    # Reset the DataFrame and current row (resetta il foglio excel precedente nel caso la data scelta sia la stessa)
    #st.session_state.df = pd.DataFrame(columns=st.session_state.df.columns)
    #st.session_state.current_row = 0

import io

# Salva il DataFrame in un buffer in memoria
buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
    st.session_state.df.to_excel(writer, index=False, sheet_name=f"Match_{st.session_state.date_str}")
buffer.seek(0)

# Offri il file per il download
st.download_button(
    label="Scarica il file Excel",
    data=buffer,
    file_name=f"Match_{st.session_state.date_str}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)