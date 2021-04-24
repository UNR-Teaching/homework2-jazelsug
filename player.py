from person import Person


class Player(Person):
    """User-controlled Player who plays against the Dealer in
    the Blackjack game. Inherits from Person.

    Parameters
    ----------
    d : Deck object
        The Deck played with in the Blackjack game.
    """
    def __init__(self, d):
        Person.__init__(self, d)
        # TODO: player bets?

    # hit is the same as in Person

    def show_hand(self):
        """Function for printing to terminal the Player's hand.
        Utilizes the show() method in card.py.
        Overrides the show_hand() method in person.py.
        """
        print("PLAYER'S HAND:")
        for h in self.hand:
            h.show()
        print("Score: {}".format(self.score))

    # check_naturals is the same as in Person

    '''
    def bet(self, amount):
        self.bet = amount
    '''