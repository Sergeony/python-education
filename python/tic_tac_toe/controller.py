""" The main module that starts the game
and manages the flow of the application.
"""
import logging.config
import yaml
from view import LinuxConsole
from model import Model


class Controller:
    """ It is where the flow of the application is managed. """

    def __init__(self):
        self.view = LinuxConsole()
        self.model = None
        self.log_path = "game.log"
        self.player_names = []
        self.player_scores = [0, 0]
        with open("config.yaml", "r", encoding="utf-8") as file:
            config = yaml.safe_load(file.read())
            logging.config.dictConfig(config)
        self.logger = logging.getLogger()

    def menu(self) -> None:
        """ Handle all user actions in the menu. """
        while True:
            action = self.view.show_menu()

            if action == 0:
                self.game_series()
                continue

            if action == 1:
                with open(self.log_path, 'r+', encoding='utf-8') as log:
                    self.view.show_log(log.readlines())
                continue

            if action == 2:
                with open(self.log_path, 'w', encoding='utf-8') as log:
                    log.close()
                continue

            if action == 3:
                break

    def game_series(self):
        """ Allow users to play multiple games in a row.
        And reset user's info after that.
        """
        while True:
            self.new_game()
            if not self.view.play_again():
                self.player_names.clear()
                self.player_scores[0] = self.player_scores[1] = 0
                break

    def new_game(self) -> None:
        """ Implement interaction between the user and the model throughout one game. """
        # Game inits
        if len(self.player_names) == 0:
            self.player_names = self.view.input_names()
        grid_size = self.view.choose_grid()
        self.model = Model(grid_size)

        # Game in progress
        while True:
            self.view.show_field(self.model.grid)
            y_pos, x_pos = self.view.take_move()
            game_status = self.model.update_status(y_pos, x_pos)

            if game_status != "continue":
                self.view.show_field(self.model.grid)
                break

        # Game ends
        winner = None
        if game_status == "victory":
            winner = self.model.active_player
            self.player_scores[winner] += 1
        self.view.show_game_over(winner)
        self.log_result()

    def log_result(self) -> None:
        """ Save game result to the log. """
        if sum(self.player_scores) == 0:
            self.logger.info("%s and %s played a draw", self.player_names[0], self.player_names[1])
        elif sum(self.player_scores) == 1:
            winner = 1 if self.player_scores[1] == 1 else 0
            self.logger.info("%s wins %s", self.player_names[winner], self.player_names[winner-1])
        else:
            self.logger.info("%s %d:%d %s",
                             self.player_names[0], self.player_scores[0],
                             self.player_scores[1], self.player_names[1])


if __name__ == "__main__":

    tic_tac_toe = Controller()
    tic_tac_toe.menu()
