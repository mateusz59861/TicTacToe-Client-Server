from unittest import TestCase
from board import *

class TestBoard(TestCase):
    def test_if_isWinner_returns_True(self):
        testboard1 = Board()
        testboard1.cells = ["", "X", "X", "X", "", "", "", "", "", ""]
        expected_result1 = True

        testboard2 = Board()
        testboard2.cells = ["", "O", "", "", "", "O", "", "", "", "O"]
        expected_result2 = True

        self.assertEqual(testboard1.isWinner(), expected_result1)
        self.assertEqual(testboard2.isWinner(), expected_result2)

    def test_if_isWinner_returns_False(self):
        testboard = Board()
        testboard.cells = ["", "X", "O", "X", "", "", "", "", "", ""]
        expected_result = False
        self.assertEqual(testboard.isWinner(), expected_result)



