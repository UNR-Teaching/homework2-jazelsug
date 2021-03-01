import random


class Person:
    def __init__(self, d):
        self.hand = []
        self.score = 0
        self.deck = d

    def hit(self):
        new_card = random.choice(self.deck)
        self.hand.append(new_card)

    def stand(self):
        # TODO: define here and in children classes
        pass
