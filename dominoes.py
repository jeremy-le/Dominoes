import random


class Dominoes:
    def __init__(self):
        self.full_set = [[a, b] for b in range(7) for a in range(7) if a <= b]
        self.doubles = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
        self.stock_pieces = []
        self.computer_pieces = self.player_pieces = []
        self.status = ""

    def shuffle(self):
        self.stock_pieces = []
        while all(x not in self.doubles for x in self.stock_pieces):
            self.stock_pieces = random.sample(self.full_set, 14)

        self.computer_pieces = self.stock_pieces[:7]
        self.player_pieces = self.stock_pieces[7:]

    def snake(self):
        self.snake_piece = max(i for i in self.doubles if i in self.stock_pieces)
        if self.snake_piece in self.computer_pieces:
            self.computer_pieces.remove(self.snake_piece)
            self.status = "player"
        if self.snake_piece in self.player_pieces:
            self.player_pieces.remove(self.snake_piece)
            self.status = "status"


if __name__ == "__main__":
    game = Dominoes()
    game.shuffle()
    game.snake()

    print(
        f"""Stock pieces: {game.stock_pieces}
Computer pieces: {game.computer_pieces}
Player pieces: {game.player_pieces}
Domino snake: {[game.snake_piece]}
Status: {game.status}
"""
    )
