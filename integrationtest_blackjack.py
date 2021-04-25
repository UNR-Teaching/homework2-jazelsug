import unittest
from deck import Deck
from player import Player
from dealer import Dealer
from blackjack import BlackJack
from card import Card


class IntegrationTest(unittest.TestCase):
    def test_big_bang_player_winner(self):
        deck = Deck()
        p = Player(deck)
        d = Dealer(deck)
        game = BlackJack(p, d)
        c1 = Card("Hearts", "9", 9)
        c2 = Card("Spades", "9", 9)
        c3 = Card("Diamonds", "9", 9)
        p.hand.append(c1)
        p.hand.append(c2)
        d.hand.append(c3)
        p.get_score()
        d.get_score()
        game.get_winner()
        self.assertEqual(game.winner, "Player")

    def test_big_bang_player_natural(self):
        deck = Deck()
        p = Player(deck)
        d = Dealer(deck)
        game = BlackJack(p, d)
        c1 = Card("Hearts", "A", 11)
        c2 = Card("Spades", "10", 10)
        c3 = Card("Diamonds", "9", 9)
        p.hand.append(c1)
        p.hand.append(c2)
        d.hand.append(c3)
        p.get_score()
        d.get_score()
        if (p.check_naturals()):
            game.get_winner()
        self.assertEqual(game.winner, "Player")



if __name__ == '__main__':
    unittest.main()
