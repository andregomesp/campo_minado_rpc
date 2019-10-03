from random import randint


class Board:
    bombMap: {}
    no_rows_columns = 0
    number_bombs = 0

    def count_adjacent(self, x, y):
        bombs_found = 0
        for x_pos in range(-1, 2):
            for y_pos in range(-1, 2):
                if not (x_pos == -1 and x == 0) and not (x_pos == 1 and x == self.no_rows_columns - 1):
                    if not (y_pos == -1 and y == 0) and not (y_pos == 1 and y == self.no_rows_columns - 1):
                        if self.bombMap[str(x) + str(y)] is not None:
                            bombs_found += 1
        return bombs_found

    def mark_square(self, x, y):
        if self.bombMap[str(x) + str(y)] is not None:
            return -1
        return self.count_adjacent(x, y)

    def create_bombs(self):
        aux = 0
        while aux < self.number_bombs:
            x = randint(0, self.no_rows_columns)
            y = randint(0, self.no_rows_columns)
            xy = str(x) + str(y)
            if self.bombMap[xy] is None:
                self.bombMap[xy] = 1
                aux += 1

    def reset_bombs(self):
        self.bombMap = {}

    def initialize_board(self, number_bombs, no_rows_columns):
        self.number_bombs = number_bombs
        self.no_rows_columns = no_rows_columns
        self.create_bombs()
