from abc import abstractmethod
from random import randint

x = "X"
o = "O"
empty = " "

class Player:
    def __init__(self,id):
        self.id = id
    @staticmethod
    def create(name,symbol, board):

        if name == "easy":
            return Easy(symbol)
        elif name == "medium":
            return Medium(symbol,board)
        else:
            return Human(symbol)



    @abstractmethod
    def play(self):
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
     def play(self):
        print('Making move level "easy"')
        while True:
            col =randint(0,3)
            row = randint(0,3)
            yield f"{col} {row}"



def other(current):
    """
    helper return other player x <-> o
    """
    return x if current == o else x


class Medium(Computer):

    def __init__(self,name,board):
        super().__init__(name)
        self.board = board

    def play(self):
        print('Making move level "medium"')
        position = self.find_win() or self.find_win(current=False)
        if position:
            yield position
        # win_current = self.find_win()
        # print(win_current)
        #
        # if win_current:
        #     print(win_current)
        #     yield win_current
        #
        # win_other =  self.find_win(current=False)
        # if win_other:
        #
        #     yield win_other


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


def position_to_string(row,col):
    return f"{col + 1} {3 -  row }"


if __name__=="__main__":
    for row,col in [(0,0),(2,0),(2,2)]:
        print(f"({row},{col}) : {position_to_string(row,col)}")


