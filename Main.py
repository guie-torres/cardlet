import streamlit as st

st.write("WELCOME TO CARDLET!")

if st.button("CARD MENU"):
    st.switch_page("pages/1_Card_Manager.py")

if st.button("PRACTICE"):
    st.switch_page("pages/2_Practice.py")
