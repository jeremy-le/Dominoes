from domino import Domino
from hand import Hand
from snake import Snake


class Computer:
    def __init__(self):
        self.hand = (
            self.snake
        ) = self._counts = self._values = self.commands = self._counts = None

    def _flat(self, hand) -> tuple:
        """Flattens the hand by concatenating items in a list altogether into a single list.
        e.g: [[1,2],[3,4],[5,6]] -> [1,2,3,4,5,6]
        """
        return sum((_.as_tuple() for _ in hand.as_tuple()), ())  #  concatenates

    def _count(self, flat: tuple) -> dict:
        """Counts the number of items it appears in a flattened list."""
        return {_: flat.count(_) for _ in (0, 1, 2, 3, 4, 5, 6)}

    def _value(self, count: dict, hand: Hand) -> list:
        return [sum(count.get(j) for j in i) for i in hand.as_tuple()]

    def scoring(self, hand, snake):
        """computer hand must be first argument, followed by snake

        Returns: list
            returns sorted list of most to least valuable commands
        """
        self.hand = hand
        self.snake = snake
        self._counts = self._count(self._flat(self.hand) + self._flat(self.snake))
        self._values = self._value(self._counts, self.hand)
        self.commands = [i + 1 for i in range(len(self.hand))]
        self._scores = sorted(list(zip(self._values, self.commands)), reverse=True)
        return self._scores
