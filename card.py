# The type of suit
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

# The type of card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# The card value
cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}


# CARD CLASS =============
class Card:
    """Card class for Blackjack game.

    Parameters
    ----------
    suit : str
        Suit of card (Spades, Hearts, Clubs, or Diamonds)
    val : str
        Value of card (A, 2-10, J, Q, K)
    card_val : int
        Actual value of card in Blackjack. 2-10 cards have inherent values.
        J, Q, and K are worth 10. A is worth 11 by default, but can switch
        to a value of 1 ("soft hand").
    up : bool, default = True
        True if card is face-up, False if face-down.
    h : bool, default = False
        True if card is in the dealer or player's hand,
        False if the card is still able to be pulled from the deck.
        
    Attributes
    ----------
    suit : str
        Suit of card.
    value : str
        Value displayed on card.
    card_value : int
        The Blackjack value of the card.
    face_up : bool
        Tracks if card is face up (value displayed) or not.
    in_hand : bool
        Tracks if card belongs to a hand or is still in the deck.
    """
    def __init__(self, suit, val, card_val, up=True, h=False):
        self.suit = suit
        self.value = val
        self.card_value = card_val
        self.face_up = up
        self.in_hand = h

    def show(self):
        """Function for displaying card information.
        If the card is face up, the card information will be printed in
        "<Value> of <Suit>" format. Otherwise, the card value and suit
        will be hidden and instead an indication of card being face down
        will be printed.
        """
        if self.face_up:
            print("{} of {}".format(self.value, self.suit))
        else:
            print("[face down]")
