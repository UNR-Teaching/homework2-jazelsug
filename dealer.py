from person import Person


class Dealer(Person):
    """Person who deals cards and plays against the Player in the
    Blackjack game. Inherits from Person.

    Parameters
    ----------
    deck : Deck object
        The Deck being played with for a Blackjack game.
    """
    def __init__(self, deck):
        Person.__init__(self, deck)

    def dealer_shuffle(self):
        """Function for shuffling the deck. Calls the shuffle()
        method within deck.py.
        """
        self.person_deck.shuffle()

    def show_hand(self):
        """Function for printing to terminal the Dealer's hand.
        Utilizes the show() method in card.py.
        Overrides the show_hand() method in person.py.
        """
        print("DEALER'S HAND:")
        for h in self.hand:
            h.show()
        print("Score: {}".format(self.score))

    def flip_cards(self):
        """Function for flipping all the cards in the Dealer's hand to
        face up. Updates the dealer's score to account for newly-turned
        face-up cards.
        """
        for h in self.hand:
            h.face_up = True
        self.get_score()

    def check_naturals(self):
        """Function for checking naturals for a Dealer. Calculates
        the Dealer's score from both face-up AND face-down cards
        (unlike for Player). Overrides the function from Person.

        Returns
        -------
        True if the Dealer's score in-hand equals 21,
        False if the Dealer's score in-hand is not 21.
        """
        # different from in Person - must check face down card
        print("Checking for dealer natural...\n")
        nat_score = 0
        for h in self.hand:
            nat_score += h.card_value
        if nat_score == 21:
            return True
        else:
            print("No dealer natural.")
            return False

    # hit is same as in Person
