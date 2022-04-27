""" The main module that starts the game
and manages the flow of the application.
"""
from view import LinuxConsole
from model import Model


class Controller:
    """ It is where the flow of the application is managed. """

    def __init__(self):
        self.view = LinuxConsole()
        self.model = None
        self.log_path = "game.log"
        self.rematch = False

    def menu(self) -> None:
        """ Handle all user actions in the menu. """
        while True:
            action = self.view.show_menu()

            if action == 0:
                while True:
                    self.new_game()
                    self.rematch = self.view.play_again()
                    if not self.rematch:
                        break
                continue

            if action == 1:
                with open(self.log_path, 'r+', encoding='utf-8') as log:
                    self.view.show_log(log.readlines())
                continue

            if action == 2:
                with open(self.log_path, mode='w', encoding='utf-8') as log:
                    log.close()
                continue

            if action == 3:
                break

    def new_game(self) -> None:
        """ Implement interaction between the user and the model throughout one game. """
        player_names = None if self.rematch else self.view.input_names()
        grid_size = self.view.choose_grid()
        self.model = Model(grid_size)

        while True:
            self.view.show_field(self.model.grid)
            y_pos, x_pos = self.view.take_move()
            game_status = self.model.update_status(y_pos, x_pos)

            if game_status != "continue":
                self.view.show_field(self.model.grid)
                break

        winner = self.model.active_player
        if game_status == "draw":
            winner = None

        self.view.show_game_over(winner)
        self.log_result(player_names, winner)

    def log_result(self, names: tuple, winner_number: int) -> None:
        """ Save game result to the log.
        If names is None, it means that players play rematch, so no names are needed.
        If winner_number is None, it means that game finished with draw.
        """
        with open(self.log_path, "a+", encoding='utf-8') as log:
            if names is None:
                # FIXME: implement game result saving for rematches
                # last_game = log.readlines()[-1]
                pass
            else:
                if winner_number is None:
                    log.write(f"{names[0]} and {names[1]} played a draw;" + "\n")
                else:
                    log.write(f"{names[winner_number - 1]} wins {names[winner_number - 2]};" + "\n")


if __name__ == "__main__":

    tic_tac_toe = Controller()
    tic_tac_toe.menu()
