import random


class Person:
    def __init__(self, d):
        self.hand = []
        self.score = 0
        self.person_deck = d

    def hit(self, up):
        new_card = random.choice(self.person_deck.deck)
        new_card.face_up = up
        self.hand.append(new_card)

    def stand(self):
        # TODO: define here and in children classes
        # done drawing cards, calculate updated score of cards in hand
        for c in self.hand:
            self.score += c.card_value
        # return score maybe?

    def show_hand(self):
        print("PERSON'S HAND:")
        for h in self.hand:
            h.show()
