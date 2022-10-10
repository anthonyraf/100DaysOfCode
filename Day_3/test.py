import unittest
from tic_tac_toe import PrettyBoard, TicTacToe, Point


class TestPrettyBoard(unittest.TestCase):
    def test_board(self):
        res = """
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
""".strip()
        self.assertEqual(
            str(PrettyBoard(["1", "2", "3", "4", "5", "6", "7", "8", "9"])), res)


class TestGame(unittest.TestCase):
    def test_base10_to_base3_conversion(self):
        self.assertEqual(TicTacToe.convert_to_base_3(0), Point(0, 0))
        self.assertEqual(TicTacToe.convert_to_base_3(1), Point(0, 1))
        self.assertEqual(TicTacToe.convert_to_base_3(2), Point(0, 2))
        self.assertEqual(TicTacToe.convert_to_base_3(3), Point(1, 0))
        self.assertEqual(TicTacToe.convert_to_base_3(4), Point(1, 1))
        self.assertEqual(TicTacToe.convert_to_base_3(5), Point(1, 2))
        self.assertEqual(TicTacToe.convert_to_base_3(6), Point(2, 0))
        self.assertEqual(TicTacToe.convert_to_base_3(7), Point(2, 1))
        self.assertEqual(TicTacToe.convert_to_base_3(8), Point(2, 2))


if __name__ == '__main__':
    unittest.main()
