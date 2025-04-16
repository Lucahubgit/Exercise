import streamlit as st
import pandas as pd


page1=st.Page('page1.py', title='Page 1')
page2=st.Page('page2.py', title='Page 2')

pg=st.navigation([page1, page2])
st.set_page_config(page_title="Volleyball project")


'''
# Inizializza lo stato della sessione
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["step1", "step2", "step3"])
if "current_row" not in st.session_state:
    st.session_state.current_row = 0  # Indice della riga corrente
if "current_step" not in st.session_state:
    st.session_state.current_step = 1  # Step corrente (1, 2 o 3)
if "match_date" not in st.session_state:
    st.session_state.match_date = None  # Data del match

# Inserimento della data del match
st.subheader("Insert the match date")
st.session_state.match_date = st.date_input("Match date", st.session_state.match_date)
# Formatta la data come stringa (es. "2025-04-13")
date_str = st.session_state.match_date.strftime("%Y-%m-%d")

# Step 1
if st.session_state.current_step == 1:
    st.subheader("What happened?")

    if st.button("Point scored"):
        st.session_state.df.loc[st.session_state.current_row, "step1"] = "Point scored"
        st.session_state.current_step = 2  # Passa allo step 2

    if st.button("Point lost"):
        st.session_state.df.loc[st.session_state.current_row, "step1"] = "Point lost"
        st.session_state.current_step = 2  # Passa allo step 2

# Step 2
if st.session_state.current_step == 2:
    st.subheader("Due to?")

    if st.button("Team point"):
        st.session_state.df.loc[st.session_state.current_row, "step2"] = "Team point"
        st.session_state.current_step = 3  # Passa allo step 3

    if st.button("Opponent error"):
        st.session_state.df.loc[st.session_state.current_row, "step2"] = "Opponent error"
        st.session_state.current_step = 3  # Passa allo step 3

# Step 3
if st.session_state.current_step == 3:
    st.subheader("Select the player involved")

    if st.button("Number 1"):
        st.session_state.df.loc[st.session_state.current_row, "step3"] = "Number 1"

    if st.button("Number 2"):
        st.session_state.df.loc[st.session_state.current_row, "step3"] = "Number 2"

    if st.button("Number 3"):
        st.session_state.df.loc[st.session_state.current_row, "step3"] = "Number 3"

    if st.button("Number 4"):
        st.session_state.df.loc[st.session_state.current_row, "step3"] = "Number 4"

    if st.button("Number 5"):
        st.session_state.df.loc[st.session_state.current_row, "step3"] = "Number 5"

    if st.button("Number 6"):
        st.session_state.df.loc[st.session_state.current_row, "step3"] = "Number 6"

# Bottone "Next action"
st.subheader("Go to the next action")
if st.button("Next action"):
    st.session_state.current_row += 1  # Passa alla riga successiva
    st.session_state.current_step = 1  # Torna allo step 1
    st.success(f"Moved to the next row: {st.session_state.current_row + 1}")

# Bottone "Save on Excel"
st.subheader("Do you want to save the match?")
if st.button("Save on Excel"):
    st.session_state.df.to_excel(f"Match_{date_str}.xlsx", index=False)  # Salva il file Excel
    st.success("File Excel updated and saved")
    # Reset the DataFrame e current row
    st.session_state.df = pd.DataFrame(columns=["step1", "step2", "step3"])
    st.session_state.current_row = 0
    st.session_state.current_step = 1  # Torna allo step 1

'''





pg.run()