# Class for TicTacToe Board


class Board:

    def __init__(self, player1, player2):
        self.game_board = [chr(i + 49) for i in range(9)]
        self.p1 = player1
        self.p2 = player2
        self.p_on_move = self.p1

    def display(self):
        print()
        for y in range(0, 9, 3):
            print("+---+---+---+")
            print(f"+ {self.game_board[y+0]} + {self.game_board[y+1]} + {self.game_board[y+2]} +")
        print("+---+---+---+")

    def make_turn(self, player, field):
        self.game_board[field] = player

    def is_field_free(self, field):
        if self.game_board[field] == self.p1.symbol or self.game_board[field] == self.p2.symbol:
            return False
        return True

    def check_win(self, player, msg=True):
        win = False
        for y in range(0, 9, 3):
            if self.game_board[y] == player and self.game_board[y + 1] == player and self.game_board[y + 2] == player:
                win = True
        for x in range(3):
            if self.game_board[x] == player and self.game_board[x + 3] == player and self.game_board[x + 6] == player:
                win = True
        if self.game_board[0] == player and self.game_board[4] == player and self.game_board[8] == player:
            win = True
        if self.game_board[2] == player and self.game_board[4] == player and self.game_board[6] == player:
            win = True
        if win and msg:
            self.display()
            print(f"Player {self.p_on_move.name} wins!")
            if not self.p_on_move.human:
                print("AI is the best!")
        return win

    def check_draw(self):
        for i in range(9):
            if self.game_board[i] != self.p1.symbol and self.game_board[i] != self.p2.symbol:
                return False
        self.display()
        print("The Game ended in a draw!")
        return True

    def player_change(self):
        if self.p_on_move == self.p1:
            self.p_on_move = self.p2
        else:
            self.p_on_move = self.p1
