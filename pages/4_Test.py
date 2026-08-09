import utils.ui as ui
import storage.storage as storage
import streamlit as st

_card = storage.cards[0]
ui.load_css("general")

ui.render_card_deck(_card, storage.decks[0])

ui.render_card_edit(_card)
