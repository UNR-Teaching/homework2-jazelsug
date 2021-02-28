# The type of suit
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

# The type of card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# The card value
cards_values = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}


class Card:
    def __init__(self, suit, val, cardval):
        # 3rd param for value of card in blackjack?
        self.suit = suit
        self.value = val
        self.card_value = cardval

    def show(self):
        # TODO: maybe add 2nd bool param for whether or not card should be displayed ?
        # TODO: what to do with card_value, if anything ?
        print("{} of {}".format(self.value, self.suit))


class Dealer:
    def __init__(self):
        # TODO: add parameter for deck/hand maybe?
        pass

    def shuffle(self):
        pass

    def deal_card(self):
        pass


class Player:
    def __init__(self, first_bet = 0):
        # TODO: parameter for deck/hand maybe?
        self.bet = first_bet
        pass

    def bet(self, amount):
        self.bet = amount

    # TODO: make hit and stand functions? or make those Person methods + inheritance


class BlackJack:
    def __init__(self):
        pass


def build_deck():
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(Card(suit, card, cards_values[card]))
    return deck


if __name__ == "__main__":
    dealer_deck = build_deck()

    for x in dealer_deck:
        x.show()
