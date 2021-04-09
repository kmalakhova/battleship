from battleship.board import Board
from battleship.game import Game

import string

# Board
row_num = list(string.ascii_lowercase[:10]) # A-J
col_num = 10
board = Board(row_num, col_num) 
board.display_board()

# Game
guesses = 25
quit = 'q'
game = Game(guesses, quit)
game.take_shot("\nChoose a spot to fire at in enemy seas: ", board)

# Ships
# 2x submarine = 1
# 2x destroyer = 2
# 1x cruiser = 3
# 1x battleship = 4
# 1x carrier = 5
