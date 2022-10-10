import sys
import itertools
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


class PrettyBoard:
    def __init__(self, raw_board):
        self.__board = ""
        self.raw_board = [x for sub in raw_board for x in sub]

    def __str__(self):
        line = "+---+---+---+"
        self.__board += line + "\n"
        for i, j in enumerate(self.raw_board):
            self.__board += f"| {j} "
            if i % 3 == 2:
                self.__board += "|\n"
                self.__board += line + "\n"

        return self.__board.strip()


class TicTacToe:
    def __init__(self):
        self.board = [[" "]*3 for _ in range(3)]
        self.players = {
            "Player 1": "x",
            "Player 2": "o"
        }
        self.turn = itertools.cycle(self.players)  # repeat "player1" "player2"
        self.finished = False
        self.loop()

    def loop(self):
        try:
            while not self.finished:
                actual_player = next(self.turn)

                print(
                    f"{actual_player}'s turn => {self.players[actual_player]}\n")
                self.show_board()

                pos = self.ask_to_play()
                self.play(pos, actual_player)

                status = self.check_win(actual_player)
                if status:
                    self.show_board()
                    print(f"Congratulations to {actual_player} !! ")
                    break
                elif status is None:
                    self.show_board()
                    print("Good Game!! Draww !!")
                    break
        except KeyboardInterrupt:
            print("\n\nBye !! :)")
            sys.exit()

    def ask_to_play(self):
        while True:
            n = int(input("Enter a number of an empty box (1-9) : "))
            print("\n")
            if 0 < n <= 9:
                pos = self.convert_to_base_3(n-1)
                if self.board[pos.x][pos.y] == " ":
                    break
                else:
                    print("This box is already taken, please take another !!")
            else:
                print("Enter a correct number between 1 and 9!!")
        return pos

    @staticmethod
    def convert_to_base_3(n) -> Point:
        """Convert the coordinate to base 3 because the board is 2d array so, for example the coordinates (1) on 1d array correspond to (0;1) in a 2d array"""
        coord = []
        if n < 3:
            return Point(0, n)
        else:
            while n > 0:
                coord.append(n % 3)
                n //= 3

        coord.reverse()

        return Point(*coord)

    def play(self, p: Point, player: str):
        self.board[p.x][p.y] = self.players[player]

    def show_board(self):
        board = str(PrettyBoard(self.board))
        txt = board.center(5, " ")
        print(txt, end="\n")

    def check_win(self, actual_player):

        # Horizontal
        for i in range(3):
            count = 0
            for j in range(3):
                if self.board[i][j] == self.players[actual_player]:
                    count += 1
            if count == 3:
                return True

        # Vertical
        for i in range(3):
            count = 0
            for j in range(3):
                if self.board[j][i] == self.players[actual_player]:
                    count += 1
            if count == 3:
                return True

        # Left diagonal
        count = 0
        for i in range(3):
            if self.board[i][i] == self.players[actual_player]:
                count += 1
            if count == 3:
                return True

        # Right diagonal
        count = 0
        for i in range(3):
            if self.board[2-i][i] == self.players[actual_player]:
                count += 1
            if count == 3:
                return True

        return None if all(x != " " for sub in self.board for x in sub) else False


if __name__ == '__main__':
    a = TicTacToe()
