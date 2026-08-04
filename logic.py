import models.card as card
import storage.storage as storage
import streamlit as st
import models.deck as deck

# CARD LOGIC


def add_card(front, back, id):
    storage.cards.append(card.Card(front, back, id))
    storage.decks[0].cards.append(id)
    storage.nextID += 1
    storage.save()


def edit_card(index, front, back):
    if index < 0 or index >= len(storage.cards):
        st.error("Invalid Index!")
        return

    storage.cards[int(index)].edit(front, back)
    storage.save()


def delete_card(index):

    if index < 0 or index >= len(storage.cards):
        st.error("Invalid Index!")
        return

    del storage.cards[index]
    storage.save()

# DECK LOGIC


def add_deck(name):
    storage.decks.append(deck.Deck(name, []))
    storage.save()


def delete_deck(id):
    del storage.decks[id]
    storage.save()


def add_to_deck(deck, cardID):
    deck.cards.append(cardID)
    storage.save()


def remove_from_deck(deck, cardID):
    del deck.cards[cardID]
    storage.save()
