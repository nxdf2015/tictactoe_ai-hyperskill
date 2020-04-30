
from helper import empty, string_to_position,board_to_string







class Board :
    """
        class board
        constructor cells
    """
    def __init__(self,cells=[empty]*9,empty = True):

        self.board =  [ list(cells[i:i+3]) for i in range(0,9,3)]
        self.empty = empty
    def __str__(self):
        return board_to_string(self.board)

    def play(self,position,player):
        col , row = string_to_position(position)
        self.board[ row ][col  ] = player
        self.empty = False


    def is_valid_coordinate(self , position,show=True):
        """
            return true if position is valid
            message error are printed  if show is true
        """
        try:

            col , row  = string_to_position(position)
            if not( 0 <= row < 3 and 0 <= col < 3):
                if show:
                    print("Coordinates should be from 1 to 3!")
                return False
            if not self.board[ row] [col ] == empty:
                if show:
                    print("This cell is occupied! Choose another one!")
                return False
            else:
                return True



        except Exception as e:
            print("You should enter numbers!")
            return False



    def get_status(self,player):
        """
        return 'player wins' 'draw' or "" if game not finished
        """
        if self.player_win(player):
                return f"{player} wins"
        elif  not self.has_empty_cell():
            return "Draw"
        return ""

    def is_draw(self,player):
        return not self.player_win(player) and not self.has_empty_cell()


    def get_empty_position(self):
        cells = []
        for i,row in enumerate(self.board):
            for j,cell in enumerate(row):
                if cell == empty:
                    cells.append((i,j))
        return cells

    def player_win(self,player):
        status = player * 3
        for items in [self.rows,self.cols,self.diags]:
            if list(filter(lambda row : row == status , items())):
                return True
        return False

    #function helper to verify if player win
    def rows(self):

        return [ "".join(row) for row in self.board]

    def cols(self):
        return [  "".join([self.board[j][i] for j in range(3)]) for i in range(3)]

    def diags(self):
        return ["".join([self.board[i][i] for i in range(3)]),"".join([ self.board[2 - i][i] for i in range(3)])]

    def get_board(self):
        return { "rows" : self.rows() , "cols" : self.cols() , "diags" : self.diags()}

    def __getitem__(self, item):
        if item == "rows":
            return self.rows()
        elif item == "cols":
            return self.cols()
        else:
            return self.diags()

    def has_empty_cell(self):
        return not "".join([ "".join(row) for row in self.board]).find(empty) == -1
    def is_empty(self):
        return self.empty

    def copy(self):
        board= Board()
        board.board=copy_list(self.board)
        return board


def copy_list(ls):
    return [ item[:] for item in ls]
