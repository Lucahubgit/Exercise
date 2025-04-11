import streamlit as st
import pandas as pd
import numpy as np


# Connection to Google Sheets
from streamlit_gsheets import GSheetsConnection
gconn=st.connection("gsheets", type=GSheetsConnection)
#Now the connection should be available and we are ready to read it
#df=gconn.read()    #to read everything
df=gconn.read(
    worksheet=0,
    usecols=[1, 2],
    nrows=2
)
st.dataframe(df)

# Save same data
import os
cwd=os.getcwd() #to store the current working directory in a string
filename2save=os.path.join(cwd,"data2save.csv")

df.to_csv(filename2save)   #from a dataframe to a csv file. Saved like this the first column is the index, we can avoid it using: df.to_csv(filename2save, index=False)
st.success('File saved')



'''
# DA FINIRE E SISTEMARE

team_name="Barcelona United"
season=["2020-21", "2021-22", "2022-23", "2023-24"]
wins=[20, 22, 18, 25]
losses=[10, 8, 12, 5]
goals_scored=[60, 65, 55, 70]

top_scorers={"Messi":15, "Pelè": 12, "Maradona": 10}

df={"wins":wins, "losses":losses, "season":season}

colA, colB=st.columns([1,1])   #the first column is three times the second one
with colA:
    st.header('Wins')   
    st.line_chart(df, x="season", y="wins")
with colB:
    st.header('Losses')
    st.line_chart(df, x="season", y="losses")

# Tabs
st.title("Select the season")
tab1, tab2, tab3, tab4=st.tabs(season)

colA, colB, colC=st.columns([1,1,1])   #the first column is three times the second one
with colA:
    st.header('Wins')   
    for n in range(len(wins)):
        st.write(wins[n])
with colB:
    st.header('Losses')
    for n in range(len(wins)):
        st.write(losses[n])
with colC:
    st.header('Goals scored')
    for n in range(len(wins)):
        st.write(goals_scored[n])

tab1.subheader("Wins")
for n in range(len(wins)):
    st.write(wins[n])
tab2.subheader("Losses")

tab2.subheader("Goals scored")
'''