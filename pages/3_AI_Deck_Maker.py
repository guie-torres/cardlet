import streamlit as st
from storage import storage
import ai
import utils.ui as ui
import utils.session as session

session.on_page_load("AI_deck_maker")
ui.load_css("AI_maker")

st.markdown(
    """
    <div class="main-title">
        <h1>CREATE DECKS USING AI</h1>
        <p>Input a theme (e.g. photosynthesis) or a source to automatically make an AI deck!</p>
    </div>
    """,
    unsafe_allow_html=True
)

input = st.text_input("Enter a theme or source", key="ai_input")

if input and st.button("CONFIRM"):
    aiDeck = ai.generate_deck(input)
    storage.ai_deck_converter(aiDeck)
    st.success("Deck generated! Check the Manage page to view it")
