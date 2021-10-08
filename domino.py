class Domino:
    """Class object representing one domino tile with two ends marked by a number of pips.

    Args:
        left (int): value of left end
        right (int): value of right end
    """

    def __init__(self, left: int, right: int):
      
        self._left = left
        self._right = right

    @property
    def left(self) -> int:
        """returns number of pips on the left end"""
        return self._left

    @property
    def right(self) -> int:
        """returns the number of pips on the right end"""
        return self._right

    @property
    def is_double(self) -> bool:
        """returns true if pips on both ends are equal"""
        return self._left == self._right

    @property
    def is_single(self) -> bool:
        """returns true if pips on both ends are unique """
        return self._left != self._right

    @property
    def rank(self) -> int:
        """returns the rank/weight of the domino (sum of pips)"""
        return self._left + self._right

    def flip(self):
        """flips the orientation of the domino tile, ends are reversed"""
        return Domino(self._right, self._left)

##############################  COMPARISON MAGIC METHODS  ##############################

    def __gt__(self, other) -> bool:
        return self.rank > other.rank

    def __lt__(self, other) -> bool:
        return self.rank < other.rank

    def __eq__(self, other) -> bool:
        return sorted([self._left, self._right]) == sorted([other._left, other._right])

    def __contains__(self, pip: int) -> bool:
        return pip in [self._left, self._right]

###############################  REPRESENTATION METHODS  ###############################

    def __str__(self) -> str:
        """[left, right]"""
        return f'[{self._left}, {self._right}]'

    def __repr__(self) -> str:
        return str(self)
