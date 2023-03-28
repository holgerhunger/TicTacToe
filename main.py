# ********* Tic Tac Toe *********
# for Python Console
# Copyright 2023 Holger Hunger
# with OOP: 2023-03-28
# with AI: 2023-02-16
# Begin:   2023-02-15

from board import Board
from player import Player, AIPlayer


print(" *** TIC TAC TOE ***\n")

name = input("Name Player One (X)? ")
# name = ""
player1 = Player('X', name)
# name = input("Name Player Two? ")
cpu_level = int(input("CPU Level? (0-3)"))
player2 = AIPlayer('O', cpu_level)

print()
print(f"Player one is {player1.name}")
print(f"Player two is {player2.name}")
board = Board(player1, player2)

game_end = False

while not game_end:
    board.display()

    selected_field = board.p_on_move.select_field(board)

    board.make_turn(board.p_on_move.symbol, selected_field)

    game_end = board.check_win(board.p_on_move.symbol)
    if not game_end:
        game_end = board.check_draw()

    board.player_change()

print("-----------------------------")
