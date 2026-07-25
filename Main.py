import streamlit as st
import storage

if "loaded" not in st.session_state:
    storage.load()
    st.session_state.loaded = True

st.write("WELCOME TO CARDLET!")

if st.button("CARD MENU"):
    st.switch_page("pages/1_Card_Manager.py")

if st.button("PRACTICE"):
    st.switch_page("pages/2_Practice.py")
