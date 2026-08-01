import streamlit as st
import storage
import random

if "card_index" not in st.session_state:
    st.session_state.card_index = 0

if "s_deck" not in st.session_state:
    st.session_state.s_deck = None

if "mode" not in st.session_state:
    st.session_state.mode = None

if len(storage.cards) <= 0:
    st.write("NO CARDS!")
    st.stop()


def set_state(state):
    st.session_state.mode = state
    st.rerun()


def select_menu():
    st.write("### SELECT DECK")

    deckID = st.number_input("Deck index", step=1,
                             min_value=0, max_value=len(storage.decks) - 1)

    _deck = storage.decks[deckID]
    st.write(f"""### DECK NAME: {_deck.name}""")

    if st.button("PRACTICE"):
        st.session_state.s_deck = shuffle_deck(_deck.cards)
        set_state("practice")


def practice():
    if st.session_state.card_index < len(st.session_state.s_deck):
        render_card(storage.find_card(
            st.session_state.s_deck[st.session_state.card_index]))
    elif st.button("RESHUFFLE"):
        st.session_state.s_deck = shuffle_deck(st.session_state.s_deck)
        st.session_state.card_index = 0
        st.rerun()

    if st.button("BACK"):
        st.session_state.card_index = 0
        set_state("select")


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
    st.write(f"***{card.front}***")

    if (st.button("REVEAL ANSWER")):
        st.write(f"***{card.back}***")

    if (st.button("NEXT CARD")):
        st.session_state.card_index += 1
        st.rerun()


if st.session_state.s_deck == None:
    st.session_state.mode = "select"

match st.session_state.mode:
    case "select":
        select_menu()

    case "practice":
        practice()

if st.button("RETURN TO MAIN MENU"):
    st.switch_page("Main.py")
