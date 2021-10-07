from domino import Domino
from snake import Snake
from hand import Hand
from boneyard import BoneYard
from random import sample, randint


def create_set(Double: bool = False):
    if Double:
        while any(_.is_double for _ in create_set()[0:14]):
            return create_set()
    if not Double:
        return sample([Domino(i, j) for i in range(7) for j in range(i, 7)], 28)


class Game():
    def __init__(self):

        self.status = ''
        self.comp_com = None
        self._deck = self.create_deck()
        self._initial = self.high_double
        self.boneyard = self.make_boneyard()
        self.player = self.deal_player()
        self.computer = self.deal_computer()
        self.remove_initial()
        self.snake = self.create_snake()

    @property
    def high_double(self):
        return max(_ for _ in self._deck[:14] if _.is_double)

    def create_deck(self):
        return create_set(Double=True)

    def make_boneyard(self):
        return BoneYard(self._deck[14:])

    def deal_player(self):
        return Hand(self._deck[:7])

    def deal_computer(self):
        return Hand(self._deck[7:14])

    def remove_initial(self):
        if self.high_double in self.player:
            self.player._remove(self.high_double)
            self.status = 'computer'
        elif self.high_double in self.computer:
            self.computer._remove(self.high_double)
            self.status = 'player'

    def create_snake(self):
        return Snake(self.high_double)

########################################################################################

    def command(self):
        if self.status == 'computer':
            # Press Enter -> perform computer action -> switch status
            input(
                "Status: The computer is about to make a move. Press Enter to continue.")
            self.computer_action()
            self.status = 'player'
        elif self.status == 'player':
            #  Enter command -> perform player action -> switch status
            self.player_action(self.player_prompt())
            self.status = 'computer'

    def player_prompt(self) -> int:
        while True:
            try:
                command = int(input("Status: It's your turn to make a move. Enter your command."))
            except ValueError:
                print("Invalid input. Please try again.")
            else:
                if (-1 * len(self.player)) <= command <= len(self.player):
                    return command
                else:
                    print("Invalid input. Please try again.")

    def player_action(self, command):
        if command == 0:
            self.player.draw(self.boneyard.draw())
        elif command > 0:
            self.snake.add_right(self.player.play(command-1))
        elif command < 0:
            self.snake.add_left(self.player.play(abs(command)-1))

    def computer_action(self):
        """computer chooses a random command and plays it"""
        self.comp_com = randint(-1 * len(self.computer), len(self.computer))
        if self.comp_com == 0:
            self.computer.draw(self.boneyard.draw())
        elif self.comp_com > 0:
            self.snake.add_right(self.computer.play(self.comp_com-1))
        elif self.comp_com < 0:
            self.snake.add_left(self.computer.play(abs(self.comp_com)-1))

    def list_pieces(self):
        for i in range(len(self.player)):
            print(f'{i + 1}:{self.player.hand[i]}')

    def screen(self):
        """Displays the current updated screen"""
        print(f"{'=' * 70}")
        print(f"Stock size: {len(self.boneyard)}")
        print(f"Computer pieces: {len(self.computer)}")
        print()
        print(self.snake)
        print()
        print('Your pieces:')
        self.list_pieces()

########################################################################################
    
    def draw_condition(self) -> bool:
        """Checks if both ends of snake are the same and that there are at least 8
        occurences of that number"""
        if self.snake[0].left != self.snake[-1].right: return False

        all_pips = [self.snake[_].left for _ in range(len(self.snake))] + \
        [self.snake[_].right for _ in range(len(self.snake))]
        return all_pips.count(self.snake[0].left) == 8

    def empty_hand(self) -> bool:
        """Checks if either hands are empty"""
        return len(self.computer) == 0 or len(self.player) == 0

########################################################################################
    def play(self):
        while not self.draw_condition() and not self.empty_hand():
            self.screen()
            self.command()
        if self.draw_condition():
            print("Status: The game is over, it's a draw")
        elif len(self.player) == 0:
            print("Status: The game is over. You won!")
        elif len(self.computer) == 0:
            print("Status: The game is over. You lost!")


def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
