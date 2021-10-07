import unittest
from functions import draw_condition
from domino import Domino

class TestFunctions(unittest.TestCase):

    def setUp(self) -> None:
        x = [Domino(5,5), Domino(5,2),Domino(2,1),Domino(1,5), Domino(5,4),Domino(4,0),Domino(0,5), Domino(5,3),Domino(3,6),Domino(6,5)]

    def test1(self):
        pass