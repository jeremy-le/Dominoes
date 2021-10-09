# TODO: 1. Count the number of 0's, 1's, 2's, etc., in your hand, and in the snake.
#       2. Each domino in your hand receives a score equal to the sum of appearances of each of its numbers.
from domino import Domino
from hand import Hand
from snake import Snake

hand = Hand([Domino(1,5), Domino(3,5), Domino(0,5)])
# Hand([Domino(i, i) for i in range(7)])
snake = Snake()
snake.add_list([Domino(4,4), Domino(4,2), Domino(2,1), Domino(1,0), Domino(0,0), Domino(0,2)])
    # [Domino(i, i+1) for i in range(4)])

class Computer:
    def __init__(self, hand, snake):
        self.hand = hand
        self.snake = snake
        self.hand_list = self.hand.as_list()
        self._counts = self._counting(self._flatten(self.hand) + self._flatten(self.snake))
        self._values = self._scoring(self._counts, self.hand_list)
        self._scores = dict(zip(self.hand, self._values))

    def _flatten(self, hand):
        """Flattens/unpacks a list of dominos into a list of pips
        e.g: [[1,2],[3,4],[5,6]] -> [1,2,3,4,5,6]

        Args:
            hand (list): either hand or snake list of domino objects

        Returns:
            list: returns a flattened list of all integer values
        """
        return sum((_.as_list() for _ in hand.as_list()), [])  #  flattens dominoes

    def _counting(self, flat) -> dict:
        """Counts the number of items it appears in a flattened list.

        Returns:
            dict: key 1 - 6: count of key occurences
        """        
        return {i: flat.count(i) for i in [0,1,2,3,4,5,6]}

    def _scoring(self, count, list) -> list:
        return [sum(count.get(j) for j in i) for i in list]

    def get_scores(self):
        return self._scores



ai = Computer(hand,snake)