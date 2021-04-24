from deck import Deck
from dealer import Dealer
from player import Player


# BLACKJACK CLASS ===========================
class BlackJack:
    """Class for organizing and running the Blackjack game.

    Parameters
    ----------
    p : Player object
        An external Player created to play Blackjack.
    d : Dealer object
        An external Dealer created to play and deal cards in Blackjack.
    w : str, default = None
        The winner of the Blackjack game.
    
    Attributes
    ----------
    player : Player object
        The Player playing the Blackjack game.
    dealer : Dealer object
        The Dealer playing in the Blackjack game.
    winner : string
        Holds the winner of the Blackjack game. Initialized to None.
        Equals "Player" if the user-controlled Player wins the game,
        "Dealer" if the computer dealer wins the game, or "Nobody" if
        the Player and the Dealer ties.
    """
    def __init__(self, p, d, w=None):
        self.player = p
        self.dealer = d
        self.winner = w

    def deal(self):
        """Function for drawing the first 4 cards of the game.
        The Player draws a face-up card, the Dealer draws a face-up card,
        the Player draws another face-up card, then the Dealer draws
        a face-down card. Hands are shown (printed to terminal) after each draw.
        """
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

    def get_winner(self):
        """Function for determining the winner of the Blackjack game.
        Person with higher score wins. A tied games means nobody wins.
        """
        if self.player.score > self.dealer.score:
            self.winner = "Player"
        elif self.player.score < self.dealer.score:
            self.winner = "Dealer"
        elif self.player.score == self.dealer.score:
            self.winner = "Nobody"
        else:
            self.winner = None

    def show_all_face_up(self):
        """Function for showing the hands of the Dealer and
        the Player. Utilizes respective show_hand methods.
        """
        self.dealer.show_hand()
        print("\n")
        self.player.show_hand()

    def reveal_all(self):
        """Function for turning all cards in both the Dealer and Player's
        hands face up, then showing the upturned hands. Utilizes
        respective show_hand methods.
        """
        print("\n")
        self.dealer.flip_cards()
        self.dealer.show_hand()
        print("\n")
        self.player.show_hand()

    def check_ties(self):
        """Function for checking for ties.
        
        Returns
        -------
        True if Dealer and Player's scores are equal,
        False if Dealer and Player's scores are not equal.
        """
        self.reveal_all()
        if self.player.score == self.dealer.score:
            return True
        else:
            return False

    def play_game(self):
        """Function for playing the Blackjack game. After shuffling
        and dealing, check for naturals. Then continue the game,
        allowing the user-controlled Player to hit and stand as
        desired. Continue playing until a winner is decided.

        Returns
        -------
        winner : str
            The entity that won the Blackjack game.
        """
        print("LET'S PLAY!\nShuffling deck...\n")
        self.dealer.dealer_shuffle()
        self.deal()

        # check for player natural
        player_nat = self.player.check_naturals()
        if player_nat:
            tied = self.check_ties()
            if tied:
                print("\nTIED GAME!!")
                self.winner = "Nobody"
                return self.winner
            else:
                print("\nPLAYER NATURAL!!")
                self.winner = "Player"
                return self.winner

        # check for dealer natural if first card is 10 or 11 value
        if self.dealer.score in {10, 11}:
            dealer_nat = self.dealer.check_naturals()
            if dealer_nat:
                self.reveal_all()
                print("\nDEALER NATURAL!!")
                self.winner = "Dealer"
                return self.winner

        # no naturals, continue the play
        while self.winner is None:
            # get input from player
            player_choice = input("Player, hit or stand (H/S): ")
            while player_choice not in {"H", "h", "S", "s"}:
                player_choice = input("Invalid input. Hit or stand (H/S): ")

            # hit
            if player_choice in {"H", "h"}:
                self.player.hit(True)
                bust = self.player.check_bust()
                if bust:
                    print("\nPLAYER BUST!!")
                    self.reveal_all()
                    self.winner = "Dealer"
                else:
                    self.show_all_face_up()
                    # keep playing
            elif player_choice in {"S", "s"}:
                # stand
                self.player.stand()
                self.reveal_all()
                # dealer hits until score is 17+
                while self.dealer.score < 17:
                    self.dealer.hit(True)
                    self.reveal_all()
                # check for dealer busts
                d_bust = self.dealer.check_bust()
                if d_bust:
                    print("\nDEALER BUST!!")
                    self.winner = "Player"
                    return self.winner
                # dealer score is 17+, check for ties
                tied = self.check_ties()
                if tied:
                    print("\nTIED GAME!!")
                    self.winner = "Nobody"
                    return self.winner
                else:
                    self.get_winner()

        return self.winner


# MAIN FUNCTION =====================================
if __name__ == "__main__":
    game_deck = Deck()
    p1 = Player(game_deck)
    d1 = Dealer(game_deck)
    game = BlackJack(p1, d1)

    winner = game.play_game()
    print("\n{} won!".format(winner))
