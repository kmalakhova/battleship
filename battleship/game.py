from .board import Board
import string
from collections import OrderedDict

class Game():
    def __init__(self, guesses, quit): 
        self.guesses = guesses
        self.quit = quit

    def guesses_left(self):
        self.guesses -= 1
        while self.guesses != 0:
            return True # How to say goodbye?
    
    def exit(self, shot):
        if shot.lower() == self.quit:
            quit()

    def take_shot(self, prompt, board):
        while self.guesses_left():
            # shot = "a1"
            shot = input(prompt)
            self.exit(shot)
            if self.valid_shot(shot, board):
                return self.convert_shot(shot, board)

    def valid_shot(self, shot, board):
        if len(shot) != 2 and len(shot) != 3:
            take_shot("nOops, that's not even in the ocean.")
            return False
        row_coord = shot[0].lower()
        if not row_coord.isalpha() or row_coord not in board.row_num:
            print("Invalid Row input.")	
            return False
        col_coord = int(shot[1:])
        if col_coord not in range(1, board.col_num + 1):
            take_shot("Invalid Column input.")
            return False
        return True

    def convert_shot(self, shot, board):
        # For tests: A1 = 00, J10 = 99
        row_coord = shot[0].lower()
        letters_to_numbers = dict(zip(string.ascii_lowercase, range(0, 10)))
        row_coord = letters_to_numbers[row_coord]
        col_coord = (int(shot[1]) - 1)
        return(str(row_coord) + str(col_coord))

    ships = [ ['00', '10', '20', '30', '40'], ['22', '23'] ]

    def locate_shot(self, shot, board, ships):
        row = int(shot[0])
        col = int(shot[1])
        for ship in ships:
            for i in range(len(ship)): 
                # Move to display_shot_result()
                if self.is_sunk(shot, board, ships):
                    print("Ship Destroyed!")
                elif self.is_hit(shot, board, ships):
                    print("Hit!")              
                else:
                    print("You missed!")

    def is_hit(self, shot, board, ships):
        if ship[i] == int(shot) and board[row][col] == 1:
            ship[i] = True # Tried to assign -1, didn't work. Why?
        return True

    def is_sunk(self, shot, board, ships):
        if all(ship):
            return True # How to use ternary operator?      
