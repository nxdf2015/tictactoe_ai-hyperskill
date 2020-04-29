
from collections import namedtuple

x = "X"
o = "O"
empty = "_"


def findPlayer(cells):
    return x if cells.count(o) == cells.count(x) else o


def board_to_string(board):
     rows = [ f'| {" ".join(row)} |' for row in board]
     size = len(rows[0])
     head = "-" * size
     return "\n".join([head ] +rows +[head])


def string_to_position(position):
    col,row = list(map(int, position.split(" ")))
    return (col -1 , 3 - row)

class Board :
    def __init__(self,cells):
        self.board =  [ list(cells[i:i+3]) for i in range(0,9,3)]
        self.current  = findPlayer(cells)

    @property
    def current_player(self):
        return self.current

    def __str__(self):
        return board_to_string(self.board)+"\n"+self.get_status()

    def play(self,position):
        col , row = string_to_position(position)
        self.board[ row ][col  ] = self.current

    def _is_empty(self,position):
        return self.board[position]

    def is_valid_coordinate(self , position):
        try:

            col , row  = string_to_position(position)
            if not( 0 <= row < 3 and 0 <= col < 3):
                print("Coordinates should be from 1 to 3!")
                return False
            if not self.board[ row] [col ] == empty:
                print("This cell is occupied! Choose another one!")
                return False
            else:
                return True



        except Exception as e:
            print("You should enter numbers!")
            return False



    def get_status(self):
        if self.player_win():
                return f"{self.current} wins"
        elif self.has_empty_cell():
                return "Game not finished"
        else:
            return "Draw"



    def rows(self):
        return [ "".join(row) for row in self.board]

    def cols(self):
        return [  "".join([self.board[j][i] for j in range(3)]) for i in range(3)]

    def diags(self):
        return ["".join([self.board[i][i] for i in range(3)]),"".join([ self.board[2 - i][i] for i in range(3)])]

    def has_empty_cell(self):
        return not "".join([ "".join(row) for row in self.board]).find(empty) == -1


    def player_win(self):
        status = self.current * 3
        for items in [self.rows,self.cols,self.diags]:
            if list(filter(lambda row : row == status , items())):
                return True




def game():
    cells=input("Enter cells: ")

    board = Board(cells)
    print(board)
    while True:

        coordinate=input("Enter the coordinates: ")
        if board.is_valid_coordinate(coordinate):
            break
    board.play(coordinate)
    print(board)



game()



