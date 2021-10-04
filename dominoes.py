import random


class Dominoes:
    def __init__(self):
        self.set = [[a, b] for b in range(7) for a in range(7) if a <= b]
        self.doubles = [[a, a] for a in range(7)]
        self.stock = []
        self.computer = self.player = self.snake = []
        self.status = ""

    def shuffle(self):
        random.shuffle(self.set)
        while all(x not in self.doubles for x in self.set[:14]):
            random.shuffle(self.set)
        self.stock = self.set[14:]
        self.computer = self.set[:7]
        self.player = self.set[7:14]

    def find_snake(self):
        self.snake = [max(i for i in self.doubles if i in self.set[:14])]
        if self.snake[0] in self.computer:
            self.computer.remove(self.snake[0])
            self.status = "player"
        else:
            self.player.remove(self.snake[0])
            self.status = "computer"


def game():
    Game = Dominoes()
    Game.shuffle()
    Game.find_snake()

    print("=" * 70)
    print(
        f"""Stock size: {len(Game.stock)}
Computer pieces: {len(Game.computer)}

{Game.snake[0]}

Your pieces:
"""
    )
    for i in range(len(Game.player)):
        print(f'{i+1}:{Game.player[i]}')


if __name__ == "__main__":
    game()

