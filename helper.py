# players
x = "X"
o = "O"

# empty cell
empty = " "

def position_to_string(row,col):
    """
    transform position array with (0,0) top left to  position board (1,1) bottom left
    return string "col row"
    """
    return f"{col + 1} {3 -  row }"


def other(current):
    """
    helper return other player
    """
    return x if current == o else x


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

