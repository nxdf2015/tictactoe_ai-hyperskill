from abc import abstractmethod
from random import randint
from operator import itemgetter

from helper import other,position_to_string,x,empty,o

class Player:
    """
    abstract class  for create player
    """
    def __init__(self,id):
        self.id = id
    @staticmethod
    def create(name,symbol, board):
        """
        return an instance of Player
        """
        if name == "user":
            return Human(symbol)
        elif name == "easy":
            return Easy(symbol)
        elif name == "medium":
            return Medium(symbol,board)
        else:
            return Hard(symbol,board)

    @abstractmethod
    def play(self):
        """
        method call when player plays
        return a string "row col" with row col in [1 , 3]  and (0,0) at bottom left
        """
        pass
    @abstractmethod
    def show(self):
        """
        print  error if true
        """
        pass



class Human(Player):
    @property
    def show(self):
        return True

    def play(self):
        while True:
            position =  input("Enter the coordinates: ")
            yield position
    
     



class Computer(Player):
    @property
    def show(self):
        return False




class Easy(Computer):
    """
    player level 'easy'
    select a random position in the board
    """
    def play(self):
        print('Making move level "easy"')
        while True:
            col =randint(0,3)
            row = randint(0,3)
            yield f"{col} {row}"



class Medium(Computer):
    """
    player level 'medium' :
    If it can win in one move (if it has two in a row), it places a third to get three in a row and win.
    If the opponent can win in one move, it plays the third itself to block the opponent to win.
    Otherwise, it makes a random move.
    """
    def __init__(self,name,board):
        super().__init__(name)
        self.board = board

    def play(self):
        print('Making move level "medium"')
        position = self.find_win() or self.find_win(current=False)
        if position:
            yield position
        while True:
            col =randint(1, 3)
            row = randint(1 , 3)
            yield f"{col  } {row}"


    def find_win(self,current=True):
         player = self.id if current else other(self.id)
         for item in  ["rows","cols" ,"diags"]:
             line_with_empty_cell = [ (i,line) for i,line in enumerate(self.board[item]) if line.count(empty) == 1]

             for  i,line in line_with_empty_cell:
               if line.count(player) == 2:
                   j = line.index(empty)
                   if item == "rows":
                     return position_to_string(i,j)
                   elif item == "cols":
                       return position_to_string(j,i)
                   else:
                       return f"{j + 1} {3 - j}" if i == 0 else f"{j+1} {j+1}"
         return False




class Hard(Computer):
    """
    play level 'hard'
    The algorithm that implements this is called Minimax
    """
    def __init__(self,name,board):
        super().__init__(name)
        self.board = board

    def play(self):
        print('Making move level "hard"')
        results=[]
        if self.board.is_empty():
            while True:
                col =randint(1, 3)
                row = randint(1 , 3)
                yield f"{col  } {row}"
        else:

            for row,col in self.board.get_empty_position():

                new_board = self.board.copy()
                new_board.play(position_to_string(row,col),self.id)
                results.append(((row,col),(min_max(new_board,self.id))))

            results.sort(key=itemgetter(1))
            row,col = results[0][0]
            yield  position_to_string(row,col)



def min_max(board,player,current=False,level=0 ):
     """
        implements minmax algoritm for 'hard' player
        level : number of level to see  all if level = 0
     """
     if board.player_win(player):
         if current :
             return 10
         else:
             return -10
     elif board.is_draw(player):
         return 0

     else:
         values = []
         for row,col in  board.get_empty_position():
             new_board = board.copy()
             current_player  = player if current else other(player)
             new_board.play(position_to_string(row,col),current_player)
             values.append(min_max(new_board,player, not current))


         if current:
             return min(values)
         else:
             return max(values)





