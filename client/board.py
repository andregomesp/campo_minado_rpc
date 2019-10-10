
def ask_number_columns():
    print("Digite número de linhas e colunas", end="\n")
    return input()


def ask_pos():
    print("Digite linha", end="\r\n")
    x = input()
    print("Digite coluna", end="\r\n")
    y = input()
    return str(int(x)-1) + str(int(y)-1)


def print_board(no_rows_columns, number_bomb_map):
    x = 0
    y = 0
    while y < no_rows_columns:
        while x < no_rows_columns:
            if str(x) + str(y) in number_bomb_map:
                bomb_value = number_bomb_map[str(x) + str(y)]
                print(bomb_value, end="\t")
            else:
                print("A", end="\t")
            x += 1
        print("")
        y += 1
        x = 0


def initialize(s, number_bomb_map):
    s.reset_bombs()
    s.initialize_board(5, 5)
    print_board(5, number_bomb_map)
