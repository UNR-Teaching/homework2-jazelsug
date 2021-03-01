import unittest
from card import *
from deck import Deck
from person import Person
from dealer import Dealer
from player import Player
from blackjack import BlackJack

'''
# DECK UNIT TESTS ==========================
class BuildDeckTests(unittest.TestCase):
    def test_same_deck(self):
        test_deck = Deck()
        new_deck = []
        for suit in card.suits:
            for c in card.cards:
                new_deck.append(card.Card(suit, c, card.cards_values[c]))
        self.assertCountEqual(test_deck.deck, new_deck)
'''


# PERSON UNIT TESTS =================
class HitTests(unittest.TestCase):
    def test_card_in_hand(self):
        test_deck = Deck()
        test_person = Person(test_deck)
        test_person.hit(True)
        test_card = test_person.hand[0]
        self.assertTrue(test_card.in_hand)

    def test_card_face_up(self):
        test_deck = Deck()
        test_person = Person(test_deck)
        test_person.hit(True)
        test_card = test_person.hand[0]
        self.assertTrue(test_card.face_up)


class CheckBustTests(unittest.TestCase):
    def test_no_bust(self):
        deck = []
        c1 = Card("Hearts", "3", "3")
        deck.append(c1)
        person = Person(deck)
        self.assertFalse(person.check_bust())

    def test_normal_bust(self):
        deck = []
        person = Person(deck)
        c1 = Card("Hearts", "9", 9)
        c2 = Card("Spades", "9", 9)
        c3 = Card("Diamonds", "9", 9)
        person.hand.append(c1)
        person.hand.append(c2)
        person.hand.append(c3)
        person.get_score()
        self.assertTrue(person.check_bust())

    def test_split_ace(self):
        deck = []
        person = Person(deck)
        c1 = Card("Hearts", "9", 9)
        c2 = Card("Spades", "9", 9)
        c3 = Card("Diamonds", "A", 11)
        person.hand.append(c1)
        person.hand.append(c2)
        person.hand.append(c3)
        person.get_score()
        self.assertFalse(person.check_bust())


'''
class GetScoreTests(unittest.TestCase):
    def test_score_updated(self):
        deck = Deck()
        person = Person(deck)
        c1 = Card("Hearts", "9", 9)
        c2 = Card("Spades", "9", 9)
        person.hand.append(c1)
        person.hand.append(c2)
        s = 0
        for c in person.hand:
            if c.face_up:
                s += c.card_value
        test_score = person.get_score()
        self.assertEqual(s, test_score)
'''


class CheckNaturalsTests(unittest.TestCase):
    def test_yes_natural(self):
        deck = []
        person = Person(deck)
        c1 = Card("Hearts", "9", 9)
        c2 = Card("Spades", "9", 9)
        c3 = Card("Diamonds", "3", 3)
        person.hand.append(c1)
        person.hand.append(c2)
        person.hand.append(c3)
        person.get_score()
        self.assertTrue(person.check_naturals())

    def test_no_natural(self):
        deck = []
        person = Person(deck)
        c1 = Card("Hearts", "9", 9)
        c2 = Card("Spades", "9", 9)
        person.hand.append(c1)
        person.hand.append(c2)
        person.get_score()
        self.assertFalse(person.check_naturals())


# DEALER UNIT TESTS ===============
class FlipCardsTest(unittest.TestCase):
    def test_face_up(self):
        deck = []
        dealer = Dealer(deck)
        c1 = Card("Hearts", "9", 9, False)
        c2 = Card("Spades", "9", 9, False)
        dealer.hand.append(c1)
        dealer.hand.append(c2)
        dealer.flip_cards()
        self.assertTrue(dealer.hand[0].face_up)
        self.assertTrue(dealer.hand[1].face_up)


# BLACKJACK UNIT TESTS =================
class GetWinnerTests(unittest.TestCase):
    def test_player_wins(self):
        deck = []
        p = Player(deck)
        d = Dealer(deck)
        b = BlackJack(p, d)
        b.player.score = 19
        b.dealer.score = 3
        b.get_winner()
        self.assertEqual(b.winner, "Player")

    def test_dealer_wins(self):
        deck = []
        p = Player(deck)
        d = Dealer(deck)
        b = BlackJack(p, d)
        b.dealer.score = 19
        b.player.score = 3
        b.get_winner()
        self.assertEqual(b.winner, "Dealer")

    def test_nobody_wins(self):
        deck = []
        p = Player(deck)
        d = Dealer(deck)
        b = BlackJack(p, d)
        b.dealer.score = 19
        b.player.score = 19
        b.get_winner()
        self.assertEqual(b.winner, "Nobody")

'''
class CheckTiesTests(unittest.TestCase):
    def test_yes_tie(self):
        deck = []
        p = Player(deck)
        d = Dealer(deck)
        b = BlackJack(p, d)
        b.dealer.score = 19
        b.player.score = 19
        self.assertTrue(b.check_ties())
'''

if __name__ == '__main__':
    unittest.main()
