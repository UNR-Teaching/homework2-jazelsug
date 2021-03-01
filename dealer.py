from person import Person


class Dealer(Person):
    def __init__(self, deck):
        Person.__init__(self, deck)
        # TODO: add parameter for deck/hand maybe?

    def shuffle(self):
        pass

    # add deal_card(self) maybe ?

    # hit is same as in Person

    def stand(self):
        # dealer reveals card ?
        pass
