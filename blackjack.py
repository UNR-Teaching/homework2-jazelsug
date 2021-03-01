from deck import Deck
from dealer import Dealer
from player import Player


# BLACKJACK CLASS ===========================
class BlackJack:
    def __init__(self, p, d, w=False):
        self.player = p
        self.dealer = d
        self.winner = w

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

    def has_winner(self):
        if self.player.score == 21:
            self.winner = "Player"
        elif self.dealer.score == 21:
            self.winner = "Dealer"
        else:
            self.winner = None

    def naturals(self):
        # TODO: order of ops - check naturals before drawing dealer's face down card

        if self.dealer.score == 10 or self.dealer.score == 11:
            # check face down card
            dealer_score = 0
            for c in self.dealer.hand:
                dealer_score += c.card_value
            if dealer_score == 21:
                for c in self.dealer.hand:
                    c.face_up = True
                self.dealer.score = 21
                self.winner = "Dealer"

    def play_game(self):
        print("LET'S PLAY!\nShuffling deck...\n")
        self.dealer.dealer_shuffle()

        self.deal()
        # check for player naturals
        self.has_winner()
        if self.winner:
            return self.winner
        # check for dealer naturals
        self.naturals()
        if self.winner:
            return self.winner

        # continue the play


# MAIN FUNCTION =====================================
if __name__ == "__main__":
    game_deck = Deck()
    p1 = Player(game_deck)
    d1 = Dealer(game_deck)
    game = BlackJack(p1, d1)

    winner = game.play_game()
    print("{} won!".format(winner))
