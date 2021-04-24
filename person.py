import random


class Person:
    """Base class for Dealer and Player.

    Parameters
    ----------
    d : Deck object
        A Deck object to be used in the Blackjack game.
    
    Attributes
    ----------
    hand : list of Card objects
        The cards that the person (dealer or player) is holding.
    score : int
        The count of the person; the sum of the card values in their hand.
    person_deck : Deck object
        A Deck object being used in the Blackjack game. The Dealer and the
        Player should be using the same Deck.
    """
    def __init__(self, d):
        self.hand = []
        self.score = 0
        self.person_deck = d

    def hit(self, up):
        """Function for hitting in a game of Blackjack.
        Here, the Person is asking for another card in an attempt to
        get closer to a count of 21, or even hit 21 exactly.

        Parameters
        ----------
        up : bool
            Indicates whether the added card should be face up or not.
        """
        new_card = None
        while new_card is None or new_card.in_hand:
            new_card = random.choice(self.person_deck.deck)
        new_card.face_up = up
        self.hand.append(new_card)
        new_card.in_hand = True
        self.get_score()

    def check_bust(self):
        """Function for checking if the Person has busted (has gotten
        a score larger than 21). We also check for a soft hand; if the
        Person busts with an Ace worth 11 in their hand, they can switch
        the Ace value to 1. This enables them to keep playing.

        Returns
        ----------
        True if the Person has busted,
        False if the Person has not yet busted.
        """
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
        """Function to calculate the updated score of cards in the
        Person's hand. At this point, the Person is done drawing cards.
        """
        self.get_score()

    def get_score(self):
        """Function for calculating the current score of face-up cards
        in the Person's hand.
        """
        s = 0
        for c in self.hand:
            if c.face_up:
                s += c.card_value
        self.score = s

    def check_naturals(self):
        """Function for checking if the Person has a natural or Blackjack
        (first two cards are an ace and a "ten-card", resulting in a score of 21).
        Overridden in Dealer but NOT in Player.

        Returns
        -------
        True if the Person has a natural,
        False if the Person does not have a natural.
        """
        if self.score == 21:
            return True
        else:
            return False

    def show_hand(self):
        """Function for printing to terminal the Person's hand. Utilizes
        the show() method in Card for each Card in the Person's hand.
        Also prints the score of the Person.

        Is overridden in Player and Dealer.
        """
        print("PERSON'S HAND:")
        for h in self.hand:
            h.show()
        print("Score: {}".format(self.score))
