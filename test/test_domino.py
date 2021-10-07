import unittest
from domino import Domino


class TestDomino(unittest.TestCase):

    def test_flip(self):
        self.assertEqual(Domino(1, 2).flip()._left, 2)
        self.assertNotEqual(Domino(1, 2).flip()._left, 1)
        self.assertEqual(Domino(6, 6).flip()._left, 6)

    def test_eq(self):
        self.assertEqual(Domino(2, 5), Domino(2, 5))
        self.assertEqual(Domino(5, 2), Domino(5, 2))
        self.assertNotEqual(Domino(1, 2), Domino(1, 3))

    def test_rank(self):
        self.assertEqual(Domino(1, 2).rank, 3)
        self.assertEqual(Domino(2, 1).rank, 3)
        self.assertEqual(Domino(3, 4).flip().rank, 7)
        self.assertEqual(Domino(100, 5).rank, 105)
        self.assertEqual(Domino(5, 100).rank, 105)
        self.assertEqual(Domino(-10, -10).rank, -20)
        self.assertEqual(Domino(-1, 1).rank, 0)
        self.assertEqual(Domino(0, 0).rank, 0)


    def test_gt(self):
        self.assertGreater(Domino(6, 6), Domino(5, 5))
        self.assertGreater(Domino(5, 4), Domino(4, 4))
        self.assertGreater(Domino(1, 0), Domino(-1, 0))
        self.assertGreater(Domino(-10, -5), Domino(-10, -6))

    def test_str(self):
        self.assertEqual(str(Domino(1, 2)), '[1, 2]')

    def test_lt(self):
        self.assertLess(Domino(4, 4), Domino(6, 6))
        self.assertLess(Domino(4, 0), Domino(1, 4))
        self.assertLess(Domino(-2, 0), Domino(0, -1))
        self.assertLess(Domino(-4, 4), Domino(-5, 6))

    def contains(self):
        self.assertTrue(5 in Domino(0, 5))
        self.assertTrue(5 in Domino(5, 0))
        self.assertTrue(5 in Domino(5, 5))
        self.assertFalse(5 in Domino(0, 0))


if __name__ == "__main__":
    unittest.main()
