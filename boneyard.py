from random import randint


class BoneYard():

    def __init__(self, domlist=[]):
        self.boneyard = domlist
        self.index = 0

    def draw(self):
        return self.boneyard.pop(randint(0, len(self.boneyard)))

    def __len__(self):
        return len(self.boneyard)

    def __getitem__(self, index):
        return self.boneyard[index]

    def __str__(self) -> str:
        return f'{self.boneyard}'

    def __repr__(self) -> str:
        return str(self)
