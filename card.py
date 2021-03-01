# The type of suit
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

# The type of card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# The card value
cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}


# CARD CLASS =============
class Card:
    def __init__(self, suit, val, card_val):
        # 3rd param for value of card in blackjack?
        self.suit = suit
        self.value = val
        self.card_value = card_val

    def show(self):
        # TODO: maybe add 2nd bool param for whether or not card should be displayed ?
        # TODO: what to do with card_value, if anything ?
        print("{} of {}".format(self.value, self.suit))
