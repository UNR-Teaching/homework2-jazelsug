from person import Person


class Dealer(Person):
    def __init__(self, deck):
        Person.__init__(self, deck)
        # TODO: add parameter for deck/hand maybe?

    def dealer_shuffle(self):
        # call shuffle within deck.py
        self.person_deck.shuffle()

    def show_hand(self):
        print("DEALER'S HAND:")
        for h in self.hand:
            h.show()
        print("Score: {}".format(self.score))

    def flip_cards(self):
        for h in self.hand:
            h.face_up = True
        self.get_score()

    def check_naturals(self):
        # different from in Person - must check face down card
        print("Checking for dealer natural...\n")
        nat_score = 0
        for h in self.hand:
            nat_score += h.card_value
        if nat_score == 21:
            return True
        else:
            return False

    # add deal_card(self) maybe ?

    # hit is same as in Person

    def stand(self):
        # dealer reveals card ?
        pass
