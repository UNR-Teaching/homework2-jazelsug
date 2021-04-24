import card
import random


# DECK CLASS =========
class Deck:
    """Deck of cards. Composed of Card class objects.

    Attributes
    ----------
    deck : list of Card objects
        The standard deck of 52 playing cards.
    build_deck() : method
        Builds the standard deck.
    """
    def __init__(self):
        self.deck = []
        self.build_deck()

    def build_deck(self):
        """Function for creating the standard 52-card deck.
        Utilizes the suits, cards, and cards_values in card.py.
        """
        for suit in card.suits:
            for c in card.cards:
                self.deck.append(card.Card(suit, c, card.cards_values[c]))

    def shuffle(self):
        """Function for shuffling the deck. Iterates through the deck and
        utilizes the random function to switch a currently selected card
        with one at the random index.
        """
        for i in range(len(self.deck)-1, 0, -1):
            r = random.randint(0, i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]
