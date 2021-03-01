import card


# DECK CLASS =========
class Deck:
    def __init__(self):
        self.deck = []
        self.build_deck()

    def build_deck(self):
        for suit in card.suits:
            for c in card.cards:
                self.deck.append(card.Card(suit, c, card.cards_values[c]))
