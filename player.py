# Class Players for TicTacToe
import copy
import random


def is_int(element: any) -> bool:
    # If you expect None to be passed:
    if element is None:
        return False
    try:
        int(element)
        return True
    except ValueError:
        return False


class Player:

    def __init__(self, token, player_name=""):
        self.human = True
        self.symbol = token
        if player_name == "":
            self.name = "Player"
        else:
            self.name = player_name
        self.name = self.name + ' (' + self.symbol + ')'

    def __repr__(self):
        return f"<Player: {self.name}>"

    def select_field(self, game_board):
        while True:
            field_select = input(f"Select Field {self.name} :")
            if not is_int(field_select):
                print("Input Error! Not a Number!")
                continue
            field_select = int(field_select) - 1
            if 8 > field_select < 0:
                print("Input Error! Only Number 1 to 8 accepted!")
                continue
            if not game_board.is_field_free(field_select):
                print("Input Error! Field is occupied!")
                continue
            break

        return field_select


class AIPlayer(Player):

    def __init__(self, token, level):
        self.level = level
        super().__init__(token, f"CPU Level {self.level}")
        self.board = None
        self.human = False

    def select_field(self, game_board):
        # Create a list of possible moves
        move_choice = None
        free_fields_indices = []
        for i in range(9):
            if game_board.is_field_free(i):
                free_fields_indices.append(i)

        if len(free_fields_indices) == 1:
            print("AI! Only one choice left!")
            move_choice = free_fields_indices[0]

        # Ab lvl1 Sucht gewinn möglichkeit mit 2er
        if move_choice is None and self.level >= 1:
            temp_free_fields = []
            for field in free_fields_indices:
                temp_board = copy.deepcopy(game_board)
                temp_board.make_turn(self.symbol, field)
                if temp_board.check_win(self.symbol, False):
                    temp_free_fields.append(field)
            if len(temp_free_fields) == 1:
                print("AI! Found one win chance!")
                move_choice = temp_free_fields[0]
            elif len(temp_free_fields) > 1:
                print("AI! Found more as one win chance!")
                free_fields_indices = temp_free_fields.copy()

        # Ab lvl2 verhindere Gewinn vom Gegner
        if move_choice is None and self.level >= 2:
            for field in free_fields_indices:
                temp_board = copy.deepcopy(game_board)
                temp_board.player_change()
                temp_board.make_turn(temp_board.p_on_move.symbol, field)
                if temp_board.check_win(temp_board.p_on_move.symbol, False):
                    print("AI! Found opponent win chance!")
                    move_choice = field

        # Ab lvl3 Feld gewichtung
        if move_choice is None and self.level >= 3:
            if 4 in free_fields_indices:
                print("AI! Center is free!")
                move_choice = 4
            else:
                intersection = list(set(free_fields_indices) & {0, 2, 6, 8})
                # print(f"Intersection = {intersection}")
                if len(intersection) > 0:
                    print("AI! Free Corner found!")
                    free_fields_indices = intersection.copy()

        # lvl0 Zufallszug
        if move_choice is None:
            move_choice = random.choice(free_fields_indices)
            print("AI! Made a random choice!")

        print(f"{self.name} choice: {move_choice+1}")
        return move_choice
