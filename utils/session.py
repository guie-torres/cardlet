import streamlit as st

current_page = ""


def on_page_load(page):
    if page != current_page:
        current_page = page
        st.session_state = None
