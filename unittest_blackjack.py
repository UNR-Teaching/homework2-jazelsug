import unittest
from card import *
from deck import Deck
from person import Person
from dealer import Dealer
from player import Player
from blackjack import BlackJack

# DECK UNIT TESTS ==========================
class BuildDeckTests(unittest.TestCase):
    def test_same_suits(self):
        test_deck = Deck()
        new_deck = []
        # read card values into new_deck
        for suit in suits:
            for c in cards:
                new_deck.append(Card(suit, c, cards_values[c]))
        equals_check = True
        for x, y in zip(test_deck.deck, new_deck):
            if x.suit != y.suit:
                equals_check = False
        self.assertTrue(equals_check)
    
    def test_same_values(self):
        test_deck = Deck()
        new_deck = []
        # read card values into new_deck
        for suit in suits:
            for c in cards:
                new_deck.append(Card(suit, c, cards_values[c]))
        equals_check = True
        for x, y in zip(test_deck.deck, new_deck):
            if x.value != y.value:
                equals_check = False
        self.assertTrue(equals_check)

    def test_same_card_values(self):
        test_deck = Deck()
        new_deck = []
        # read card values into new_deck
        for suit in suits:
            for c in cards:
                new_deck.append(Card(suit, c, cards_values[c]))
        equals_check = True
        for x, y in zip(test_deck.deck, new_deck):
            if x.card_value != y.card_value:
                equals_check = False
        self.assertTrue(equals_check)

    def test_same_face_up(self):
        test_deck = Deck()
        new_deck = []
        # read card values into new_deck
        for suit in suits:
            for c in cards:
                new_deck.append(Card(suit, c, cards_values[c]))
        equals_check = True
        for x, y in zip(test_deck.deck, new_deck):
            if x.face_up != y.face_up:
                equals_check = False
        self.assertTrue(equals_check)
    
    def test_same_in_hand(self):
        test_deck = Deck()
        new_deck = []
        # read card values into new_deck
        for suit in suits:
            for c in cards:
                new_deck.append(Card(suit, c, cards_values[c]))
        equals_check = True
        for x, y in zip(test_deck.deck, new_deck):
            if x.in_hand != y.in_hand:
                equals_check = False
        self.assertTrue(equals_check)


class ShuffleTests(unittest.TestCase):
    def test_different_suits(self):
        deck_one = Deck()
        deck_two = Deck()
        # shuffle second deck
        deck_two.shuffle()
        equals_check = True
        for x, y in zip(deck_one.deck, deck_two.deck):
            if x.suit != y.suit:
                equals_check = False
        self.assertFalse(equals_check)

    def test_different_values(self):
        deck_one = Deck()
        deck_two = Deck()
        # shuffle second deck
        deck_two.shuffle()
        equals_check = True
        for x, y in zip(deck_one.deck, deck_two.deck):
            if x.value != y.value:
                equals_check = False
        self.assertFalse(equals_check)

    def test_different_card_values(self):
        deck_one = Deck()
        deck_two = Deck()
        # shuffle second deck
        deck_two.shuffle()
        equals_check = True
        for x, y in zip(deck_one.deck, deck_two.deck):
            if x.card_value != y.card_value:
                equals_check = False
        self.assertFalse(equals_check)

    def test_same_face_up(self):
        deck_one = Deck()
        deck_two = Deck()
        # shuffle second deck
        deck_two.shuffle()
        equals_check = True
        for x, y in zip(deck_one.deck, deck_two.deck):
            if x.face_up != y.face_up:
                equals_check = False
        self.assertTrue(equals_check)

    def test_same_in_hands(self):
        deck_one = Deck()
        deck_two = Deck()
        # shuffle second deck
        deck_two.shuffle()
        equals_check = True
        for x, y in zip(deck_one.deck, deck_two.deck):
            if x.in_hand != y.in_hand:
                equals_check = False
        self.assertTrue(equals_check)


# PERSON UNIT TESTS =================
class HitTests(unittest.TestCase):
    def test_card_in_hand(self):
        test_deck = Deck()
        test_person = Person(test_deck)
        initial_hand_count = len(test_person.hand)
        test_person.hit(True)
        new_hand_count = len(test_person.hand)
        self.assertEqual(initial_hand_count + 1, new_hand_count)

    def test_card_face_up(self):
        test_deck = Deck()
        test_person = Person(test_deck)
        last_index = len(test_person.hand)
        test_person.hit(True)
        test_card = test_person.hand[last_index]
        self.assertTrue(test_card.face_up)


class CheckBustTests(unittest.TestCase):
    def test_no_bust(self):
        d = Deck()
        # c1 = Card("Hearts", "3", "3")
        # d.deck.append(c1)
        person = Person(d)
        person.score = 3
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
        # person.get_score()
        person.score = 27
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
        person.score = 27
        person.get_score()
        person.score = 19
        self.assertFalse(person.check_bust())


class GetScoreTests(unittest.TestCase):
    def test_score_updated(self):
        deck = Deck()
        person = Person(deck)
        c1 = Card("Hearts", "9", 9)
        c2 = Card("Spades", "9", 9)
        person.hand.append(c1)
        person.hand.append(c2)
        person.get_score()
        expected_score = 18
        self.assertEqual(person.score, expected_score)
    
    def test_zero_score(self):
        deck = Deck()
        person = Person(deck)
        # add no cards
        person.get_score()
        expected_score = 0
        self.assertEqual(person.score, expected_score)


class CheckNaturalsTests(unittest.TestCase):
    def test_yes_natural(self):
        deck = []
        person = Person(deck)
        c1 = Card("Hearts", "A", 11)
        c2 = Card("Spades", "J", 10)
        person.hand.append(c1)
        person.hand.append(c2)
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
    
class CheckDealersNaturalsTest(unittest.TestCase):
    def test_yes_natural_with_face_down(self):
        deck = []
        dealer = Dealer(deck)
        c1 = Card("Hearts", "A", 11, True)
        c2 = Card("Spades", "K", 10, False)
        dealer.hand.append(c1)
        dealer.hand.append(c2)
        self.assertTrue(dealer.check_naturals())

    def test_no_natural_with_face_down(self):
        deck = []
        dealer = Dealer(deck)
        c1 = Card("Hearts", "A", 11, True)
        c2 = Card("Spades", "3", 3, False)
        dealer.hand.append(c1)
        dealer.hand.append(c2)
        self.assertFalse(dealer.check_naturals())


# BLACKJACK UNIT TESTS =================
class DealTests(unittest.TestCase):
    def test_two_cards_for_player(self):
        deck = Deck()
        player = Player(deck)
        dealer = Dealer(deck)
        blackjack = BlackJack(player, dealer)
        blackjack.deal()
        players_hand_count = len(player.hand)
        expected_player_hand_count = 2
        self.assertEqual(players_hand_count, expected_player_hand_count)

    def test_two_cards_for_dealer(self):
        deck = Deck()
        player = Player(deck)
        dealer = Dealer(deck)
        blackjack = BlackJack(player, dealer)
        blackjack.deal()
        dealers_hand_count = len(dealer.hand)
        expected_dealer_hand_count = 2
        self.assertEqual(dealers_hand_count, expected_dealer_hand_count)

    def test_second_dealer_card_face_down(self):
        deck = Deck()
        player = Player(deck)
        dealer = Dealer(deck)
        blackjack = BlackJack(player, dealer)
        blackjack.deal()
        self.assertFalse(dealer.hand[1].face_up)


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


class CheckTiesTests(unittest.TestCase):
    def test_yes_tie(self):
        deck = Deck()
        player = Player(deck)
        dealer = Dealer(deck)
        blackjack = BlackJack(player, dealer)
        card_ten = Card("Hearts", "K", 10, True)
        player.hand.append(card_ten)
        dealer.hand.append(card_ten)
        player.score = 10
        self.assertTrue(blackjack.check_ties())

    def test_no_tie(self):
        deck = Deck()
        player = Player(deck)
        dealer = Dealer(deck)
        blackjack = BlackJack(player, dealer)
        card_ten = Card("Hearts", "K", 10)
        card_five = Card("Hearts", "5", 5)
        player.hand.append(card_ten)
        dealer.hand.append(card_five)
        self.assertFalse(blackjack.check_ties())


class PlayGameTests(unittest.TestCase):
    def test_dealer_natural(self):
        low_deck = Deck()
        low_deck.deck.clear()
        c1 = Card("Hearts", "3", 3)
        c2 = Card("Hearts", "A", 11)
        low_deck.deck.append(c1)
        low_deck.deck.append(c2)
        natural_deck = Deck()
        natural_deck.deck.clear()
        c3 = Card("Diamonds", "10", 10)
        c4 = Card("Spades", "A", 11)
        natural_deck.deck.append(c4)
        natural_deck.deck.append(c3)
        player = Player(low_deck)
        dealer = Dealer(natural_deck)
        b = BlackJack(player, dealer)
        self.assertEqual(b.play_game(), "Dealer")

    def test_player_natural(self):
        low_deck = Deck()
        low_deck.deck.clear()
        c1 = Card("Hearts", "3", 3)
        c2 = Card("Hearts", "A", 11)
        low_deck.deck.append(c1)
        low_deck.deck.append(c2)
        natural_deck = Deck()
        natural_deck.deck.clear()
        c3 = Card("Diamonds", "10", 10)
        c4 = Card("Spades", "A", 11)
        natural_deck.deck.append(c4)
        natural_deck.deck.append(c3)
        player = Player(natural_deck)
        dealer = Dealer(low_deck)
        b = BlackJack(player, dealer)
        self.assertEqual(b.play_game(), "Player")

    def test_natural_tie(self):
        low_deck = Deck()
        low_deck.deck.clear()
        c1 = Card("Hearts", "K", 10)
        c2 = Card("Hearts", "A", 11)
        low_deck.deck.append(c1)
        low_deck.deck.append(c2)
        natural_deck = Deck()
        natural_deck.deck.clear()
        c3 = Card("Diamonds", "10", 10)
        c4 = Card("Spades", "A", 11)
        natural_deck.deck.append(c4)
        natural_deck.deck.append(c3)
        player = Player(natural_deck)
        dealer = Dealer(low_deck)
        b = BlackJack(player, dealer)
        self.assertEqual(b.play_game(), "Nobody")



if __name__ == '__main__':
    unittest.main()
