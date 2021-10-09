from domino import Domino


class Snake:
    def __init__(self, domino=None):
        """Only a single domino can be used to intialise the snake"""
        self.snake = [domino] if isinstance(domino, Domino) else []


    def add_list(self, list_):
        """This method can be used to add a list of dominos after object has been created"""
        if all(_ for _ in list_ if isinstance(_, Domino)):
            self.snake += list_

    def add_to(self, domino, side='right'):
        if side == 'right':
            return self.snake.append(domino)
        elif side == 'left':
            return self.snake.insert(0, domino)

    def add_right(self, domino):
        return self.snake.append(domino)

    def add_left(self, domino):
        return self.snake.insert(0, domino)

    def reset(self) -> None:
        self.snake = []
        return self.snake

    def as_list(self) -> list:
        return self.snake

    def as_tuple(self) -> tuple:
        return tuple(self.snake)

    def __len__(self) -> int:
        return len(self.snake)

    def __getitem__(self, index) -> Domino:
        return self.snake[index]

    def __str__(self) -> str:
        if len(self.snake) > 6:
            return f'{self[0]}{self[1]}{self[2]}...{self[-3]}{self[-2]}{self[-1]}'
        else:
            return ''.join(str(d) for d in self.snake)

    def __repr__(self) -> str:
        return str(self)

    def __contains__(self, domino) -> bool:
        return domino in self.snake

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.snake):
            raise StopIteration
        i = self._index
        self._index += 1
        return self.snake[i]
