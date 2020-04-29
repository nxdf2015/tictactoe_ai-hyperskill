from board import Board

from player import Computer,Human

x = "X"
o = "O"
empty = " "



init_state = empty * 9#  "_________"



class Game:
    symbols=[x,o]
    def __init__(self,cells=init_state):
        self.board = Board(cells)
        self.players = [Human(0),Computer(1)]
        self.current = 0

    def next_player(self):
        self.current = (self.current + 1 ) % 2

    def game_end(self):
        return self.board.game_ended()

    def start(self):
        print(self.board)
        while True:
            player = self.players[self.current]
            for position in player.play():
                if self.board.is_valid_coordinate(position,show = player.id == 0):
                    break
            self.board.play(position,self.symbols[player.id])
            print(self.board)
            status = self.board.get_status(self.symbols[player.id])
            if status:
                print(status)
            if self.board.player_win(self.symbols[player.id]) or not self.board.has_empty_cell():
                break
            self.next_player()







