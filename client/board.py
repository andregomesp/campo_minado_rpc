class Board:

    def ask_number_columns(self):
        print("Digite número de linhas e colunas", end="\n")
        return input()

    def ask_pos(self):
        print("Digite linha", end="\r\n")
        x = input()
        print("Digite coluna", end="\r\n")
        y = input()
        return str(x) + str(y)

    def print_board(self, no_rows_columns):
        aux = 0
        while aux < no_rows_columns:
            print("A \t" * int(no_rows_columns))


    def initialize(self):
        return None
