import card
import random


# DECK CLASS =========
class Deck:
    def __init__(self):
        self.deck = []
        self.build_deck()

    def build_deck(self):
        for suit in card.suits:
            for c in card.cards:
                self.deck.append(card.Card(suit, c, card.cards_values[c]))

    def shuffle(self):
        for i in range(len(self.deck)-1, 0, -1):
            r = random.randint(0, i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]
