from person import Person
import random


class Dealer(Person):
    def __init__(self, deck):
        Person.__init__(self, deck)
        # TODO: add parameter for deck/hand maybe?

    def dealer_shuffle(self):
        # call shuffle within deck.py
        self.deck.shuffle()

    # add deal_card(self) maybe ?

    # hit is same as in Person

    def stand(self):
        # dealer reveals card ?
        pass
