from deck import Deck




# PLAYER CLASS ======================
class Player:
    def __init__(self, first_bet=0):
        # TODO: parameter for deck/hand maybe?
        self.bet = first_bet
        pass

    def bet(self, amount):
        self.bet = amount

    # TODO: make hit and stand functions? or make those Person methods + inheritance


# BLACKJACK CLASS ===========================
class BlackJack:
    def __init__(self):
        pass


# MAIN FUNCTION =====================================
if __name__ == "__main__":
    game_deck = Deck()
    game_deck.shuffle()

    for x in game_deck.deck:
        x.show()
