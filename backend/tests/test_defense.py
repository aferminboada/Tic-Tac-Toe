import unittest
from backend.moves import defense
from backend.utils import get_segments


class DefenseTest(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        self.Play = defense
        super(DefenseTest, self).__init__(methodName=methodName)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_under_attack(self):
        self.assertTrue(
            self.Play.is_under_attack(['X', -1, 'X'], 'O')
        )
        self.assertFalse(
            self.Play.is_under_attack(['X', -1, 'O'], 'O')
        )
        self.assertTrue(
            self.Play.is_under_attack([-1, 'X', 'X'], 'O')
        )
        self.assertFalse(
            self.Play.is_under_attack(['O', 'X', 'O'], 'O')
        )
        self.assertTrue(
            self.Play.is_under_attack(['O', -1, 'O'], 'X')
        )

    def test_get_attack_coefficient(self):
        board = [
            -1, -1, 'O',
            'X', 'X', -1,
            'X', 'O', -1
        ]
        self.assertEqual(
            self.Play.get_attack_coefficient(
                get_segments(board),
                [0, 1, 2],  # positions to check
                'O'  # who I am
            ),
            1
        )

        board = [
            -1, -1, 'O',
            'X', 'X', -1,
            'X', 'O', -1
        ]
        self.assertEqual(
            self.Play.get_attack_coefficient(
                get_segments(board),
                [0, 1, 2],  # position to check
                'O'  # who I am
            ),
            1
        )

        board = [
            -1, -1, -1,
            -1, 'X', -1,
            -1, -1, -1
        ]
        self.assertEqual(
            self.Play.get_attack_coefficient(
                get_segments(board),
                [0, 1, 2],  # position to check
                'O'  # who I am
            ),
            0
        )

        board = [
            'X', 'X', 'O',
            -1, -1, -1,
            -1, -1, 'O'
        ]

        self.assertEqual(
            self.Play.get_attack_coefficient(
                get_segments(board),
                [0, 1, 2],  # position to check
                'X'  # who I am
            ),
            0
        )

    def test_i_will_win(self):
        self.assertTrue(
            self.Play.i_will_win(
                [-1, -1, -1],
                'O'
            )
        )
        self.assertFalse(
            self.Play.i_will_win(
                ['X', -1, -1],
                'O'
            )
        )
        self.assertFalse(
            self.Play.i_will_win(
                ['O', 'X', -1],
                'O'
            )
        )
        self.assertTrue(
            self.Play.i_will_win(
                ['O', -1, -1],
                'O'
            )
        )


if __name__ == '__main__':
    unittest.main()
