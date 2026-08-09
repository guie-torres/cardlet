import models.card as card
import json
import models.deck as deck
import logic

cards = []
decks = []


def save():
    data = []
    for c in cards:
        data.append(c.to_dict())

    with open("storage/cards.json", "w") as file:
        json.dump(data, file, indent=4)

    data = []
    for d in decks:
        data.append(d.to_dict())

    with open("storage/decks.json", "w") as file:
        json.dump(data, file, indent=4)


def load():
    cards.clear()
    decks.clear()
    try:
        with open("storage/cards.json", "r") as file:
            data = json.load(file)

        for item in data:
            cards.append(card.Card(item["front"], item["back"], item["id"]))
    except FileNotFoundError:
        pass

    try:
        with open("storage/decks.json", "r") as file:
            data = json.load(file)

        for item in data:
            decks.append(
                deck.Deck(item["name"], item["cards"], item["id"])
            )
    except FileNotFoundError:
        logic.add_deck("Main")
        save()


def find_card(card_id):
    for card in cards:
        if card.id == card_id:
            return card
    return None


def ai_deck_converter(aiDeck):
    deck = logic.add_deck(aiDeck.name)

    for card in aiDeck.cards:
        c = logic.add_card(card.front, card.back)
        logic.add_to_deck(deck, c)
