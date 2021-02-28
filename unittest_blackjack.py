import unittest
import io
import sys
from blackjack import Card

# TODO: fix!!

class ShowTests(unittest.TestCase):
    def test_show_equal(self):
        test_card = Card("Hearts", 7)
        correct_output = "7 of Hearts"

        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output
        test_card.show()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), correct_output)


if __name__ == '__main__':
    unittest.main()
