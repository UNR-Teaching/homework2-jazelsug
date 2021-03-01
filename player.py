from person import Person


class Player(Person):
    def __init__(self, d):
        Person.__init__(self, d)
        # TODO: player bets?

    # hit is the same as in Person

    def show_hand(self):
        print("PLAYER'S HAND:")
        for h in self.hand:
            h.show()
        print("Score: {}".format(self.score))

    # check_naturals is the same as in Person

    '''
    def bet(self, amount):
        self.bet = amount
    '''