import streamlit as st
import storage


def set_state(state):
    st.session_state.mode = state
    st.rerun()


def render_main():
    if st.button("ADD DECK"):
        set_state("add")

    if st.button("GENERAL CARD MANAGER"):
        st.switch_page("pages/1_Card_Manager.py")

    if st.button("RETURN TO MAIN MENU"):
        st.switch_page("Main.py")


render_main()
