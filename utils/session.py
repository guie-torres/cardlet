import streamlit as st


def on_page_load(page):
    if page == st.session_state.current_page:
        return

    st.session_state.current_page = page
    st.session_state.mode = None


def set_state(state):
    st.session_state.mode = state
    st.rerun()
