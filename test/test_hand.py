import unittest
from domino import Domino
from hand import Hand


class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand_1 = Hand()
        self.hand_2 = Hand([Domino(i, i) for i in range(7)])

    def test_draw(self):
        self.hand_1.draw(Domino(1, 1))
        self.assertEqual(len(self.hand_1), 1)
        self.assertTrue(Domino(1, 1) in self.hand_1)
        self.hand_1.draw(Domino(2, 2))
        self.assertEqual(len(self.hand_1), 2)

    def test_contain(self):
        self.assertTrue(Domino(6, 6) in self.hand_2)
        self.assertFalse(Domino(0, 6) in self.hand_2)

    def test_len(self):
        self.assertEqual(len(self.hand_1), 0)
        self.assertEqual(len(self.hand_2), 7)

    def test_iter(self):
        pass


# if __name__ == "__main__":
#     unittest.main()

