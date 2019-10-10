import xmlrpc.client
from board import *

with xmlrpc.client.ServerProxy("http://localhost:8000/", allow_none=True) as s:
    print(s.system.listMethods())
    number_bomb_map = {}
    initialize(s, number_bomb_map)
    while True:
        xy = ask_pos()
        result = s.mark_square(xy[0], xy[1])
        if str(result) == "-1":
            break
        number_bomb_map[xy] = result
        print_board(5, number_bomb_map)
    print("\n\n\nBOOOOOOOOOOOOOOOOOM!!! VOCÊ MORREU!!!!!11!111!1")
