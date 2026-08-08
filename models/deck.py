class Deck:
    def __init__(self, name, cards, id):
        self.name = name
        self.cards = cards
        self.id = id

    def to_dict(self):
        return {
            "name": self.name,
            "cards": [card for card in self.cards],
            "id": self.id
        }
