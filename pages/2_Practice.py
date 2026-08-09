import streamlit as st
from storage import storage
import random
import utils.ui as ui
import utils.session as session

session.on_page_load("practice")

if "card_index" not in st.session_state:
    st.session_state.card_index = 0

if "s_deck" not in st.session_state:
    st.session_state.s_deck = None

if "mode" not in st.session_state:
    st.session_state.mode = "select"

if "front" not in st.session_state:
    st.session_state.front = True

if len(storage.cards) <= 0:
    st.write("NO CARDS!")
    st.stop()

ui.load_css("general")
ui.load_css("practice_style")


def select_menu():
    st.write("### SELECT DECK")

    deckID = st.number_input("Deck index", step=1,
                             min_value=0, max_value=len(storage.decks) - 1)

    _deck = storage.decks[deckID]
    st.write(f"""### DECK NAME: {_deck.name}""")

    if st.button("PRACTICE"):
        st.session_state.s_deck = shuffle_deck(_deck.cards)
        session.set_state("practice")


def practice():
    if st.session_state.card_index < len(st.session_state.s_deck):
        render_card(storage.find_card(
            st.session_state.s_deck[st.session_state.card_index]))
    elif st.button("RESHUFFLE"):
        st.session_state.s_deck = shuffle_deck(st.session_state.s_deck)
        st.session_state.card_index = 0
        st.rerun()


def shuffle_deck(deck):
    _deck = []

    for i in range(0, len(deck)):

        shuffled = False

        while shuffled == False:
            ci = random.randrange(0, len(deck))

            if not _deck.__contains__(deck[ci]):
                _deck.append(deck[ci])
                shuffled = True

    return _deck


def render_card(card):
    text = ""

    if st.session_state.front:
        text = card.front
    else:
        text = card.back

    ui.render_card_practice(text)


def render_buttons(practice):
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    if practice:
        with col1:
            if (st.button("FLIP")):
                st.session_state.front = not st.session_state.front
                st.rerun()

        with col2:
            if (st.button("NEXT")):
                st.session_state.front = True
                st.session_state.card_index += 1
                st.rerun()

        with col3:
            if st.button("BACK"):
                st.session_state.card_index = 0
                session.set_state("select")

    with col4:
        if st.button("BACK TO MENU", key="return_practice"):
            st.switch_page("Main.py")


if st.session_state.mode == None:
    st.session_state.mode = "select"

match st.session_state.mode:
    case "select":
        select_menu()

    case "practice":
        practice()

render_buttons(st.session_state.mode == "practice")
