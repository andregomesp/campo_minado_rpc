from random import randint


class Board:
    bombMap: {}
    no_rows_columns = 0
    number_bombs = 0

    def count_adjacent(self, x, y):
        bombs_found = 0
        for x_pos in range(-1, 2):
            for y_pos in range(-1, 2):
                x_current = int(x) - x_pos
                y_current = int(y) - y_pos
                if (x_current >= 0 or x_current < 2) and (y_current >= 0 or y_current < 2):
                    xy = str(x_current) + str(y_current)
                    if xy in self.bombMap:
                        bombs_found += 1
        return bombs_found

    def mark_square(self, x, y):
        xy = str(x) + str(y)
        if xy in self.bombMap:
            return -1
        return self.count_adjacent(x, y)

    def create_bombs(self):
        aux = 0
        while aux < self.number_bombs:
            x = randint(0, self.no_rows_columns)
            y = randint(0, self.no_rows_columns)
            xy = str(x) + str(y)
            if xy not in self.bombMap:
                self.bombMap[xy] = 1
                aux += 1

    def reset_bombs(self):
        self.bombMap = {}

    def initialize_board(self, number_bombs, no_rows_columns):
        self.number_bombs = number_bombs
        self.no_rows_columns = no_rows_columns
        self.create_bombs()
        return "done"
