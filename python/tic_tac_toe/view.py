""" Implements all possible interfaces with the game. """
from abc import ABC, abstractmethod
from os import system


class View(ABC):
    """ It is how the game is presented and interacted with the user. """

    @abstractmethod
    def show_menu(self) -> int:
        """ Represent possible actions in menu."""

    @abstractmethod
    def show_log(self, log_list: list) -> None:
        """ Represent a list with the results of past games. """

    @abstractmethod
    def input_names(self) -> tuple:
        """ Request player names. """

    @abstractmethod
    def choose_grid(self) -> int:
        """ Request a grid size. """

    @abstractmethod
    def show_field(self, grid: list) -> None:
        """ Represent the current state of the field. """

    @abstractmethod
    def take_move(self) -> tuple:
        """ Request a cell to move. """

    @abstractmethod
    def show_game_over(self, player_number: int) -> None:
        """ Represent game over screen with possible actions. """

    @abstractmethod
    def play_again(self) -> bool:
        """ Ask if the player(s) wants to rematch. """


class LinuxConsole(View):
    """ View in CLI for Linux systems. """

    def show_menu(self):
        system("clear")

        print("Press 0 to play\n"
              "Press 1 to view win log\n"
              "Press 2 to clear win log\n"
              "Press 3 to exit")

        return int(input("Enter the command: "))

    def show_log(self, log_list):
        system("clear")

        if len(log_list) > 0:
            for game in log_list:
                print(game, end="")
            print()
        else:
            print("Nothing to see here yet")

        input("Press Enter to return to the menu: ")

    def input_names(self):
        system("clear")

        print("Enter player names(skip the second one if you gonna play with AI")

        return (input("Enter player_1 name: "),
                input("Enter player_2 name: "))

    def choose_grid(self):
        system("clear")

        print("Press 3 to play in 3x3\n"
              "Press 5 to play in 5x5\n"
              "Press 7 to play in 7x7")

        return int(input("Grid size: "))

    def show_field(self, grid):
        system('clear')

        grid_size = len(grid)

        for y in range(grid_size):
            print("+----+" * grid_size)

            for x in range(grid_size):
                print("| ", end="")

                if grid[y][x] == 1:
                    symbol = "()"
                elif grid[y][x] == 2:
                    symbol = "><"
                else:
                    symbol = "  "

                print(f"{symbol} |", end="")

            print("\n", "+----+" * grid_size, sep="")

    def take_move(self):
        return (int(input("Enter the row: "))-1,
                int(input("Enter the col: "))-1)

    def show_game_over(self, player_number):
        if player_number is None:
            print("DRAW!")
        else:
            print(f"PLAYER {player_number} WINS!")

    def play_again(self):
        print("Press 0 to rematch\n"
              "Press Enter to return to the menu")

        return bool(input("Enter the command: "))

# TODO: implement Tkinter interface
# class Tkinter(View):
#     pass
