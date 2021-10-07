

class Domino:
    """Class for objects that represent one domino tile. Has two ends
     marked with an integer value, usually from 0 to 6"""

    def __init__(self, left: int, right: int):
        """:input pair: a pair of two values (l, r) for domino ends."""
        self._left = left
        self._right = right

    @property
    def left(self) -> int:
        """returns the number of pips on the left side"""
        return self._left

    @property
    def right(self) -> int:
        """returns the number of pips on the right side"""
        return self._right

    @property
    def is_double(self) -> bool:
        """returns true if numbers on either end are the same"""
        return self._left == self._right

    @property
    def is_single(self) -> bool:
        """returns true if numbers on either end are different from each other"""
        return self._left != self._right

    @property
    def rank(self) -> int:
        """returns the rank/weight of the domino (sum of numbers)"""
        return self._left + self._right

    def flip(self):
        """flips the domino so what was on the right is now on the left,
        and what was on the left is now on the right."""
        return Domino(self._right, self._left)

    def __gt__(self, other) -> bool:
        return self.rank > other.rank

    def __lt__(self, other) -> bool:
        return self.rank < other.rank

    def __eq__(self, other) -> bool:
        return sorted([self._left, self._right]) == sorted([other._left, other._right])

    def __contains__(self, pip: int) -> bool:
        return pip in [self._left, self._right]

    def __str__(self):
        """[left, right]"""
        return f'[{self._left}, {self._right}]'

    def __repr__(self):
        return str(self)
