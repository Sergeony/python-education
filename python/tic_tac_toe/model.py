""" Tic-tac-toe game logic """


class Model:
    """ Tic-tac-toe game logic """

    def __init__(self, grid_size: int):
        self._grid_size = grid_size
        self.grid = self.init_grid()
        self.active_player = 1
        self._moves_played = 0
        self._line_length = 3 if self._grid_size == 3 else 4

    def init_grid(self) -> list:
        """ Create and fill the grid with empty values. """
        return [[None for _ in range(self._grid_size)] for _ in range(self._grid_size)]

    def update_status(self, y: int, x: int) -> str:
        """ Fill in the cell, if it's empty, then
        call a win check, if the moves are enough to win, then
        check for a draw, if all cells are filled.
        """
        if self.grid[y][x] is None:

            self.grid[y][x] = self.active_player
            self._moves_played += 1

            moves_to_win = 2 * self._line_length - 1
            if self._moves_played >= moves_to_win:
                if self._check_win():
                    return "victory"

            moves_to_draw = self._grid_size ** 2
            if self._moves_played == moves_to_draw:
                return "draw"

            self._switch_player()

        return "continue"

    def _check_win(self) -> bool:
        """ Check all cases for a possible win. """
        return self._diagonal_check() or self._line_check()

        # # Simple checking, works only for 3x3 grid

        # for line in range(self.__grid_size):
        #     if self.grid[0][line] == self.grid[1][line] == self.grid[2][line]:
        #         return True
        #     if self.grid[line][0] == self.grid[line][1] == self.grid[line][2]:
        #         return True
        # if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
        #     return True
        # if self.grid[2][0] == self.grid[1][1] == self.grid[0][2]:
        #     return True

    def _diagonal_check(self) -> bool:
        """ Check all diagonals in both directions. """
        gap_to_move = self._grid_size - self._line_length + 1

        for y in range(gap_to_move):
            for x in range(gap_to_move):

                # Top-to-Bottom diagonal
                for i in range(self._line_length - 1):
                    current_cell = self.grid[y+i][x+i]
                    next_cell = self.grid[y+i+1][x+i+1]
                    if current_cell != next_cell or current_cell is None:
                        break
                else:
                    return True

                # Bottom-to-Top diagonal
                for i in range(self._line_length - 1):
                    reflected_y = y + self._line_length - i - 1
                    current_cell = self.grid[reflected_y][x+i]
                    next_cell = self.grid[reflected_y-1][x+i+1]
                    if current_cell != next_cell or current_cell is None:
                        break
                else:
                    return True

        return False

    def _line_check(self) -> bool:
        """ Check all horizontal and vertical lines. """
        gap_to_move = self._grid_size - self._line_length + 1

        for y in range(self._grid_size):
            for x in range(gap_to_move):

                # horizontal line
                for i in range(self._line_length - 1):
                    current_cell = self.grid[y][x+i]
                    next_cell = self.grid[y][x+i+1]
                    if current_cell != next_cell or current_cell is None:
                        break
                else:
                    return True

                # vertical line
                for i in range(self._line_length - 1):
                    current_cell = self.grid[x+i][y]
                    next_cell = self.grid[x+i+1][y]
                    if current_cell != next_cell or current_cell is None:
                        break
                else:
                    return True

        return False

    def _switch_player(self) -> None:
        """ Toggle to the player who will move next. """
        self.active_player = 1 if self.active_player == 2 else 2
