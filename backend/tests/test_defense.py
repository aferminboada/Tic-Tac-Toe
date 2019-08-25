import unittest
from backend.moves import defense


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
                board,
                0,  # position to check
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
                board,
                1,  # position to check
                'O'  # who I am
            ),
            0
        )

        board = [
            -1, -1, -1,
            -1, 'X', -1,
            -1, -1, -1
        ]
        self.assertEqual(
            self.Play.get_attack_coefficient(
                board,
                0,  # position to check
                'O'  # who I am
            ),
            0
        )

    def test_get_cell_loss(self):
        board = [
            -1, -1, 'O',
            'X', 'X', -1,
            'X', 'O', -1
        ]
        self.assertEqual(
            len(
                self.Play.get_cell_loss(
                    board,
                    'O'
                )
            ),
            2
        )

        board = [
            -1, -1, -1,
            -1, 'X', -1,
            -1, -1, -1
        ]
        self.assertEqual(
            len(
                self.Play.get_cell_loss(
                    board,
                    'O'
                )
            ),
            8
        )


if __name__ == '__main__':
    unittest.main()
