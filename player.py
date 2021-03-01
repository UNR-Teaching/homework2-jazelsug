from person import Person


class Player(Person):
    def __init__(self, d):
        Person.__init__(self, d)
        # TODO: parameter for deck/hand maybe?
        # TODO: player bets?

    # hit is the same as in Person

    def show_hand(self):
        print("PLAYER'S HAND:")
        for h in self.hand:
            h.show()
        print("Score: {}".format(self.score))

    def check_bust(self):
        if self.score > 21:
            return True
        else:
            return False

    '''
    def bet(self, amount):
        self.bet = amount
    '''