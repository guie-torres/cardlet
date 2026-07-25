import card
import json
import deck

cards = []
decks = []

nextID = 0


def save():
    data = []
    for c in cards:
        data.append(c.to_dict())

    with open("cards.json", "w") as file:
        json.dump(data, file, indent=4)

    data = {
        "next_card_id": nextID
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    data = []
    for d in decks:
        data.append(d.to_dict())

    with open("decks.json", "w") as file:
        json.dump(data, file, indent=4)


def load():
    cards.clear()

    try:
        with open("cards.json", "r") as file:
            data = json.load(file)

        for item in data:
            cards.append(card.Card(item["front"], item["back"], item["id"]))
    except FileNotFoundError:
        pass

    try:
        with open("decks.json", "r") as file:
            data = json.load(file)

        for item in data:
            decks.append(
                deck.Deck(item["name"], item["cards"]))
    except FileNotFoundError:
        pass

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        nextID = data["next_card_id"]
    except FileNotFoundError:
        pass
