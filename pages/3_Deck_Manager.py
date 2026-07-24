import streamlit as st
import storage
import deck

if "mode" not in st.session_state:
    st.session_state.mode = None


def set_state(state):
    st.session_state.mode = state
    st.rerun()


def render_main():
    if st.button("ADD DECK"):
        set_state("add")

    if st.button("LIST DECKS"):
        set_state("list")

    if st.button("GENERAL CARD MANAGER"):
        st.switch_page("pages/1_Card_Manager.py")

    if st.button("RETURN TO MAIN MENU"):
        st.switch_page("Main.py")


def render_add():
    name = st.text_input("Input deck name")

    if st.button("Save Deck") and name.strip():
        storage.decks.append(deck.Deck(name, None))
        st.success("Added!")
        set_state(None)


def render_list():
    if len(storage.decks) <= 0:
        st.write("No Decks!")
        return

    for i in range(0, len(storage.decks)):
        _deck = storage.decks[i]
        st.markdown(
            f"""
            ### Deck {i + 1}:
            - **Name:** {_deck.name}""")


def render_backbutton():
    if st.button("BACK"):
        set_state(None)


match st.session_state.mode:
    case "add":
        render_add()
        render_backbutton()
    case "list":
        render_list()
        render_backbutton()
    case _:
        render_main()
