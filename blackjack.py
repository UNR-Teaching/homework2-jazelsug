from deck import Deck
from dealer import Dealer
from player import Player


# BLACKJACK CLASS ===========================
class BlackJack:
    def __init__(self, p, d):
        self.player = p
        self.dealer = d

    def deal(self):
        # draw first 4 cards of the game
        self.player.hit(True)
        self.player.show_hand()
        print("\n")
        self.dealer.hit(True)
        self.dealer.show_hand()
        print("\n")
        self.player.hit(True)
        self.player.show_hand()
        print("\n")
        self.dealer.hit(False)
        self.dealer.show_hand()
        print("\n")


# MAIN FUNCTION =====================================
if __name__ == "__main__":
    game_deck = Deck()
    p1 = Player(game_deck)
    d1 = Dealer(game_deck)
    game = BlackJack(p1, d1)

    d1.dealer_shuffle()
    game.deal()
