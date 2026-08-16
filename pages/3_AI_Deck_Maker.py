import streamlit as st
from storage import storage
import ai
import utils.ui as ui
import utils.session as session

if "current_page" not in st.session_state:
    st.session_state.current_page = "none"

session.on_page_load("AI_deck_maker")
ui.load_css("AI_maker")

if "loaded" not in st.session_state:
    storage.load()
    st.session_state.loaded = True


def generate_deck(input, name, amount):
    aiDeck = ai.generate_deck(input, name, amount)

    if aiDeck.error:
        st.error(f"ERROR: {aiDeck.error_message}")
        return

    if len(aiDeck.cards) == 0:
        st.error(
            "No cards were generated, please try again")
        return

    if len(aiDeck.cards) != amount and amount != "any amount of":
        st.warning(
            f"The AI generated {len(aiDeck.cards)} cards instead of {amount}."
        )

    storage.ai_deck_converter(aiDeck)
    st.success("Deck generated! Check the Manage page to view it")


st.markdown(
    """
    <div class="main-title">
        <h1>CREATE DECKS USING AI</h1>
        <p>Input a theme (e.g. photosynthesis) or a source to automatically make an AI deck!</p>
    </div>
    """,
    unsafe_allow_html=True
)

amount = st.number_input(
    "Enter the number of cards you want to generate (optional, 0 = any)", key="ai_amount", min_value=0, max_value=50, step=1)
name = st.text_input(
    "Enter the name of the deck (optional)", key="ai_name")
input = st.text_input("Enter a theme or source", key="ai_input")

if input and st.button("CONFIRM"):
    if (amount == 0):
        amount = "any amount of"

    if (name.strip() == ""):
        name = "anything"

    generate_deck(input, name, amount)
