import streamlit as st
import storage
import random

if "loaded" not in st.session_state:
    storage.load()
    st.session_state.loaded = True

if "card_index" not in st.session_state:
    st.session_state.card_index = 0

if "s_deck" not in st.session_state:
    st.session_state.s_deck = []

if len(storage.cards) <= 0:
    st.write("NO CARDS!")
    st.stop()


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


if st.session_state.s_deck == []:
    st.session_state.s_deck = shuffle_deck(storage.cards)

if st.session_state.card_index < len(st.session_state.s_deck):
    render_card(st.session_state.s_deck[st.session_state.card_index])
elif st.button("RESHUFFLE"):
    st.session_state.s_deck = shuffle_deck(storage.cards)
    st.session_state.card_index = 0
    st.rerun()

if st.button("RETURN TO MAIN MENU"):
    st.switch_page("Main.py")
