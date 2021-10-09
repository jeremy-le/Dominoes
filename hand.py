from domino import Domino

class Hand():
    def __init__(self, domlist=[]):
        self.hand = domlist
        self.index = 0
        self._astuple = self.return_astuple()

    def play(self, index: int):
        """Removes one tile from hand using index"""
        return self.hand.pop(index)

    def draw(self, domino):
        """Adds a new tile to hand, usually from boneyard"""
        self.hand.append(domino)

    def _remove(self, domino):
        """Similar to play but does not return domino"""
        self.hand.remove(domino)

    def return_aslist(self):
        return self.hand

    def return_astuple(self):
        return tuple(self.hand)
        
    def __len__(self) -> int:
        return len(self.hand)

    def __contain__(self, domino):
        return domino in self.hand

    def __getitem__(self, index):
        return self.hand[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.hand):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.hand[index]

    def __str__(self):
        return f'{self.hand}'

    def __repr__(self):
        return str(self)
