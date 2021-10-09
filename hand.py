from domino import Domino


class Hand:
    def __init__(self, domlist=[]):
        self.hand = domlist
        self._astuple = self.as_tuple()

    def play(self, index: int):
        """Removes one tile from hand using index"""
        return self.hand.pop(index)

    def draw(self, domino):
        """Adds a new tile to hand, usually from boneyard"""
        self.hand.append(domino)

    def _remove(self, domino):
        """Similar to play but does not return domino"""
        self.hand.remove(domino)

    def as_list(self):
        return self.hand

    def as_tuple(self):
        return tuple(self.hand)

    def __len__(self) -> int:
        return len(self.hand)

    def __contain__(self, domino):
        return domino in self.hand

    def __getitem__(self, index):
        return self.hand[index]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.hand):
            raise StopIteration
        i = self._index
        self._index += 1
        return self.hand[i]

    def __str__(self):
        return f"{self.hand}"

    def __repr__(self):
        return str(self)
