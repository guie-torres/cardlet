import models.card as card
import storage.storage as storage
import streamlit as st
import models.deck as deck
import uuid

# CARD LOGIC


def add_card(front, back):
    id = str(uuid.uuid4())

    storage.cards.append(card.Card(front, back, id))
    storage.decks[0].cards.append(id)
    storage.save()
    return get_card_id(id)


def edit_card(card, front, back):
    card.edit(front, back)
    storage.save()


def delete_card(card):
    for d in storage.decks:
        if card.id in d.cards:
            d.cards.remove(card.id)

    storage.cards.remove(card)
    storage.save()


def get_card_id(id):
    for c in storage.cards:
        if c.id == id:
            return c

# DECK LOGIC


def add_deck(name):
    id = str(uuid.uuid4())
    storage.decks.append(deck.Deck(name, [], id))
    storage.save()
    return get_deck_id(id)


def delete_deck(deck):
    storage.decks.remove(deck)
    storage.save()


def add_to_deck(deck, card):
    deck.cards.append(card.id)
    storage.save()


def remove_from_deck(deck, card):
    deck.cards.remove(card.id)
    storage.save()


def get_deck_id(id):
    for d in storage.decks:
        if d.id == id:
            return d


def convert_deck_to_quizlet(deck):
    result = ""

    for card_id in deck.cards:
        _card = storage.find_card(card_id)

        result += f"{_card.front}\t{_card.back}\n"

    return result
