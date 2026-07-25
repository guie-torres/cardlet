class Deck:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def to_dict(self):
        return {
            "name": self.name,
            "cards": [card.to_dict() for card in self.cards],
        }
