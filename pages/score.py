import streamlit as st
import pandas as pd
import io   # per scaricare il file excel

# SCELTA PUNTO GUADAGNATO O PERSO E SALVATAGGIO FILE EXCEL

# Inizializza il DataFrame se non esiste
#if "df" not in st.session_state:
    #st.session_state.df = pd.DataFrame(columns=["score", "point_type", "player", "attack_zone", "defense_zone", "block_zone", "serve_zone", "out_zone", "our_score", "opp_score", "set"])
    #st.session_state.df["our_score"] = 0
    #st.session_state.df["opp_score"] = 0
    #st.session_state.df["set"] = 1

#if "our_score" not in st.session_state.df.columns:
    #st.session_state.df["our_score"] = 0
#if "opp_score" not in st.session_state.df.columns:
    #st.session_state.df["opp_score"] = 0

st.subheader("What happened?")

if st.button("Point scored"):
    st.session_state.df.loc[st.session_state.current_row, "score"] = "Point scored"
    if st.session_state.current_row > 0 and st.session_state.current_row - 1 in st.session_state.df.index:
        st.session_state.df.loc[st.session_state.current_row, "our_score"] = st.session_state.df.loc[st.session_state.current_row - 1, "our_score"] + 1
        st.session_state.df.loc[st.session_state.current_row, "opp_score"] = st.session_state.df.loc[st.session_state.current_row - 1, "opp_score"]
    else:
        st.session_state.df.loc[st.session_state.current_row, "our_score"] = 1  # Inizializza a 1 se è la prima riga
        st.session_state.df.loc[st.session_state.current_row, "opp_score"] = 0  # Inizializza a 0 se è la prima riga
    st.switch_page("pages/w_point_type.py")

if st.button("Point lost"):
    st.session_state.df.loc[st.session_state.current_row, "score"] = "Point lost"
    if st.session_state.current_row > 0 and st.session_state.current_row - 1 in st.session_state.df.index:
        st.session_state.df.loc[st.session_state.current_row, "opp_score"] = st.session_state.df.loc[st.session_state.current_row - 1, "opp_score"] + 1
        st.session_state.df.loc[st.session_state.current_row, "our_score"] = st.session_state.df.loc[st.session_state.current_row - 1, "our_score"]
    else:
        st.session_state.df.loc[st.session_state.current_row, "opp_score"] = 1  # Inizializza a 1 se è la prima riga
        st.session_state.df.loc[st.session_state.current_row, "our_score"] = 0  # Inizializza a 0 se è la prima riga
    st.switch_page("pages/l_player.py")

# Salva il foglio "Game Report"
st.subheader("The game is concluded? Save and download the report")
if st.button("Save Game Report"):
    file_name = f"Match_{st.session_state.date_str}.xlsx"
    
    # Verifica se il file esiste
    try:
        # Aggiungi il foglio "Game Report" al file Excel esistente
        with pd.ExcelWriter(file_name, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            st.session_state.df.to_excel(writer, index=False, sheet_name="Game Report")
        
        st.success(f"Game report salvato nel file Excel: {file_name}")
    except FileNotFoundError:
        st.error("Il file Excel non esiste ancora. Salva prima le info nella pagina 'data'.")

# Salva il DataFrame in un buffer in memoria con più fogli
buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
    # Salva il foglio "Game report"
    st.session_state.df.to_excel(writer, index=False, sheet_name="Game report")
    
    # Salva il foglio "Info" (se esiste)
    if "game_roster" in st.session_state and st.session_state.game_roster:
        info_df = pd.DataFrame({
            "Players": st.session_state.game_roster,
            "Data": [st.session_state.match_date] * len(st.session_state.game_roster),
            "Opponent": [st.session_state.game_opp] * len(st.session_state.game_roster)
        })
        info_df.to_excel(writer, index=False, sheet_name="Info")
    
    buffer.seek(0)

# Button per il download del file excel
st.download_button(
    label="Download the Excel file",
    data=buffer,
    file_name=f"Match_{st.session_state.date_str}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)