import streamlit as st
import storage.storage as storage
import utils.ui as ui
import logic
import utils.session as session

session.on_page_load("manage")
ui.load_css("general")

if "mode" not in st.session_state:
    st.session_state.mode = None

if "deleteDeckId" not in st.session_state:
    st.session_state.deleteDeckId = None

if "editCardId" not in st.session_state:
    st.session_state.editCardId = None

if "deleteCardId" not in st.session_state:
    st.session_state.deleteCardId = None

if "addCardId" not in st.session_state:
    st.session_state.addCardId = None


def list():
    if len(storage.decks) <= 0:
        st.write("No Decks!")
        return

    for i in range(0, len(storage.decks)):
        _deck = storage.decks[i]
        ui.render_deck(_deck)


def render_main():

    col1, col2 = st.columns([0.15, 1])

    with col1:
        if st.button("ADD CARD"):
            session.set_state("addCard")
    with col2:
        if st.button("ADD DECK"):
            session.set_state("addDeck")

    list()
    ui.render_back_to_menu_button()


def render_add_card():
    ui.render_card_add()
    ui.render_backbutton()


def render_edit_card():
    ui.render_card_edit(logic.get_card_id(st.session_state.editCardId))
    ui.render_backbutton()


def render_delete_card():
    ui.render_card_delete(logic.get_card_id(st.session_state.deleteCardId))
    ui.render_backbutton()


def render_add_deck():
    ui.render_deck_add()
    ui.render_backbutton()


def render_add_to_deck():
    ui.render_card_add_to_deck(logic.get_card_id(st.session_state.addCardId))
    ui.render_backbutton()


def render_delete_deck():
    ui.render_deck_delete(logic.get_deck_id(st.session_state.deleteDeckId))
    ui.render_backbutton()


match st.session_state.mode:

    case None:
        render_main()
    case "addCard":
        render_add_card()
    case "editCard":
        render_edit_card()
    case "deleteCard":
        render_delete_card()
    case "addDeck":
        render_add_deck()
    case "deleteDeck":
        render_delete_deck()
    case "addToDeck":
        render_add_to_deck()
