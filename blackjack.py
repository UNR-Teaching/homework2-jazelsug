from deck import Deck
from dealer import Dealer
from player import Player


# BLACKJACK CLASS ===========================
class BlackJack:
    def __init__(self, p, d, w=None):
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

    def reveal_all(self):
        self.dealer.flip_cards()
        self.dealer.show_hand()
        self.player.show_hand()

    def check_ties(self):
        self.reveal_all()
        if self.player.score == self.dealer.score:
            return True
        else:
            return False

    def play_game(self):
        print("LET'S PLAY!\nShuffling deck...\n")
        self.dealer.dealer_shuffle()
        self.deal()

        # check for player natural
        player_nat = self.player.check_naturals()
        if player_nat:
            tied = self.check_ties()
            if tied:
                print("TIED GAME!!")
                self.winner = "Nobody"
                return self.winner
            else:
                print("PLAYER NATURAL!!")
                self.winner = "Player"
                return self.winner

        # check for dealer natural
        dealer_nat = self.dealer.check_naturals()
        if dealer_nat:
            self.reveal_all()
            print("DEALER NATURAL!!")
            self.winner = "Dealer"
            return self.winner

        # no naturals, continue the play
        while self.winner is None:
            player_choice = input("Player, hit or stand (H/S): ")
            while player_choice not in {"H", "h", "S", "s"}:
                player_choice = input("Invalid input. Hit or stand (H/S): ")
            if player_choice in {"H", "h"}:
                self.player.hit(True)
                bust = self.player.check_bust()
                if bust:
                    print("PLAYER BUST!!")
                    self.dealer.flip_cards()
                    self.dealer.show_hand()
                    self.player.show_hand()
                    self.winner = "Dealer"
            elif player_choice in {"S", "s"}:
                self.player.stand()
                # compare player and dealer scores
                self.winner = "Player"  # TODO: fix!!

        # TODO: display cards after each successful hit

        return self.winner


# MAIN FUNCTION =====================================
if __name__ == "__main__":
    game_deck = Deck()
    p1 = Player(game_deck)
    d1 = Dealer(game_deck)
    game = BlackJack(p1, d1)

    winner = game.play_game()
    print("{} won!".format(winner))
