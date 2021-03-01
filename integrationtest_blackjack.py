import unittest
from deck import Deck
from player import Player
from dealer import Dealer
from blackjack import BlackJack
from card import Card


class IntegrationTest(unittest.TestCase):
    def test_big_bang(self):
        d = Deck()
        p = Player(d)
        d = Dealer(d)
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


if __name__ == '__main__':
    unittest.main()
