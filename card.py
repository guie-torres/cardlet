class Card:

    def __init__(self, front, back, id):
        self.front = front
        self.back = back
        self.id = id

    def edit(self, front, back):
        self.front = front
        self.back = back

    def to_dict(self):
        return {
            "front": self.front,
            "back": self.back,
            "id": self.id
        }
