import random


class Person:
    def __init__(self, d):
        self.hand = []
        self.score = 0
        self.person_deck = d

    def hit(self, up):
        new_card = None
        while new_card is None or new_card.in_hand:
            new_card = random.choice(self.person_deck.deck)
        new_card.face_up = up
        self.hand.append(new_card)
        new_card.in_hand = True
        self.get_score()

    def check_bust(self):
        if self.score > 21:
            # see if Aces can split from 11 to 1
            for h in self.hand:
                if h.value == "A" and h.card_value == 11:
                    h.card_value = 1
                    self.get_score()
            if self.score > 21:
                return True
            else:
                print("Switched Ace value from 11 to 1.")
                return False
        else:
            return False

    def stand(self):
        # done drawing cards, calculate updated score of cards in hand
        self.get_score()

    def get_score(self):
        s = 0
        for c in self.hand:
            if c.face_up:
                s += c.card_value
        self.score = s

    def check_naturals(self):
        if self.score == 21:
            return True

    def show_hand(self):
        print("PERSON'S HAND:")
        for h in self.hand:
            h.show()
        print("Score: {}".format(self.score))
