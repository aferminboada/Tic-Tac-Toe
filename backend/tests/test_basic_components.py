import unittest
from backend.play import Play
from backend.messages import (
    test_choose_how_begin,
    test_clear_game,
)


class BasicComponentTest(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        self.Play = Play
        super(BasicComponentTest, self).__init__(methodName=methodName)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_choose_how_begin(self):
        play = self.Play()
        self.assertEqual(play.how_begin, None, test_choose_how_begin)
        self.assertEqual(play.turn_of, None, test_choose_how_begin)
        self.assertEqual(play.board, None, test_choose_how_begin)
        play.choose_how_begin()
        self.assertNotEqual(play.how_begin, None, test_choose_how_begin)
        self.assertNotEqual(play.turn_of, None, test_choose_how_begin)
        self.assertEqual(play.turn_of, play.how_begin, test_choose_how_begin)

    def test_clear_game(self):
        play = self.Play()
        play.clear_game()
        self.assertEqual(play.movements, 0, test_clear_game)
        for index in range(9):
            self.assertEqual(play.board[index], -1, test_clear_game)


if __name__ == '__main__':
    unittest.main()
