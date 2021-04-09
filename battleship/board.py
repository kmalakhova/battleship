import string 

class Board():
    def __init__(self, row_num, col_num):
        self.row_num = row_num
        self.col_num = col_num

        # self.board = [[0] * self.col_num for x in self.row_num]

        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    # 0 - empty
    # 1 - ship
    # M - missed
    # H - hit  
    # S - sunk
    # Has to be rebuilt
    @staticmethod
    def display_cell(cell):
        if cell == 0:
            print(' ~ ', end='')
        elif cell == 1:
            print(' M ', end='')
        elif cell == 2:
            print(' S ', end='')     
        elif cell == 3:
            print(' H ', end='')  

    def display_board(self):
        print('   ', end='')
        print('  '.join(str(x) for x in range(1,11)))
        row_letters = list(string.ascii_uppercase[:10])
        i = 0
        for row in self.board:
            row_letter = row_letters[i]
            print(row_letter, '', end='')
            for cell in row:
                self.display_cell(cell)
            print()
            i += 1
