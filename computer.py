# TODO: 1. Count the number of 0's, 1's, 2's, etc., in your hand, and in the snake.
#       2. Each domino in your hand receives a score equal to the sum of appearances of each of its numbers.
from domino import Domino
from hand import Hand
from snake import Snake

hand = Hand([Domino(i, i) for i in range(7)])
snake = Snake()
snake.add_list([Domino(i, i+1) for i in range(4)])

class Computer:
    def __init__(self, hand, snake) -> None:
        self.hand = hand
        self.snake = snake
        self.hand_list = self.flatten_hand(self.hand)
        self.snake_list = self.flatten_hand(self.snake)
        self.count_dict = self.count_pips(self.hand_list + self.snake_list)

    def flatten_hand(self, hand):
        """Flattens/unpacks a list of dominos into a list of pips
        e.g: [[1,2],[3,4],[5,6]] -> [1,2,3,4,5,6]

        Args:
            hand (list): either hand or snake list of domino objects

        Returns:
            list: returns a flattened list of all integer values
        """
        return sum((_.return_list() for _ in hand.return_list()), [])  #  flattens dominoes


    def count_pips(self, list):
        """Counts the number of items it appears in a list.

        Returns:
            dict: a dict of counts for all unique values
        """        
        return {i: list.count(i) for i in list}