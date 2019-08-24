import unittest
from backend import utils
from backend.messages import (
    test_clean_positions,
    test_all_equals,
    test_get_segments,
)


class UtilsTest(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        self.Play = utils
        super(UtilsTest, self).__init__(methodName=methodName)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_clean_positions(self):
        # all clean positions
        board = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        clean_positions = self.Play.clean_positions(board)
        self.assertTrue(len(clean_positions) == 9, test_clean_positions)
        for index in range(9):
            self.assertEqual(index+1, clean_positions[index], test_clean_positions)

        # first three with no clean positions
        board = ['X', 'O', 'X', -1, -1, -1, -1, -1, -1]
        clean_positions = self.Play.clean_positions(board)
        self.assertTrue(len(clean_positions) == 6, test_clean_positions)

        # last three with no clean positions
        board = [-1, -1, -1, -1, -1, -1, 'O', 'O', 'X']
        clean_positions = self.Play.clean_positions(board)
        self.assertTrue(len(clean_positions) == 6, test_clean_positions)

        # last three with no clean positions
        board = [-1, 'O', -1, 'X', -1, -1, 'O', 'O', -1]
        clean_positions = self.Play.clean_positions(board)
        self.assertTrue(len(clean_positions) == 5, test_clean_positions)

        # only one cell no clear
        board = [-1, -1, 'X', -1, -1, -1, -1, -1, -1]
        clean_positions = self.Play.clean_positions(board)
        self.assertTrue(len(clean_positions) == 8, test_clean_positions)
        self.assertFalse(3 in clean_positions, test_clean_positions)

        # only one cell no clear
        board = [-1, -1, -1, -1, -1, 'X', -1, -1, -1]
        clean_positions = self.Play.clean_positions(board)
        self.assertTrue(len(clean_positions) == 8, test_clean_positions)
        self.assertFalse(6 in clean_positions, test_clean_positions)

    def test_get_segments(self):
        board = [-1] * 9
        segments = self.Play.get_segments(board)
        self.assertEqual(len(segments), len(self.Play.combinations_wins), test_get_segments)

    def test_all_equals(self):
        segment = ['X', 'O', -1]
        self.assertFalse(self.Play.all_equals(segment), test_all_equals)

        segment = ['X', 'O', 'O']
        self.assertFalse(self.Play.all_equals(segment), test_all_equals)

        segment = ['O', 'O', -1]
        self.assertFalse(self.Play.all_equals(segment), test_all_equals)

        segment = ['X', 'X', -1]
        self.assertFalse(self.Play.all_equals(segment), test_all_equals)

        segment = ['X', 'O', 'X']
        self.assertFalse(self.Play.all_equals(segment), test_all_equals)

        segment = ['X', 'X', 'X']
        self.assertTrue(self.Play.all_equals(segment), test_all_equals)

        segment = ['O', 'O', 'O']
        self.assertTrue(self.Play.all_equals(segment), test_all_equals)

    def test_a_winner(self):
        # no winner
        board = [
            'X', '0', -1,
            -1, 'X', -1,
            -1, -1, '0'
        ]
        self.assertFalse(self.Play.a_winner(board))

        # winner X
        board = [
            'X', '0', '0',
            -1, 'X', -1,
            -1, -1, 'X'
        ]
        self.assertTrue(self.Play.a_winner(board))

        # winner O
        board = [
            '0', 'X', 'X',
            -1, '0', 'X',
            -1, -1, '0'
        ]
        self.assertTrue(self.Play.a_winner(board))

        # no winner
        board = [
            '0', 'X', 'X',
            -1, '0', '0',
            -1, 'X', 'X'
        ]
        self.assertFalse(self.Play.a_winner(board))


if __name__ == '__main__':
    unittest.main()
