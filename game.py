from board import Board

from player import Easy,Human,Medium,Player

x = "X"
o = "O"
empty = " "



init_state = empty * 9#  "_________"





class Game:
    symbols=[x,o]
    def __init__(self,* player_names  , cells=init_state):
        self.board = Board(cells)
        first_player , second_player = player_names
        self.players = [ Player.create(first_player,x,self.board),Player.create(second_player,o,self.board)]


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
                if self.board.is_valid_coordinate(position,show = player.show):
                    break
            self.board.play(position, player.id)
            print(self.board)
            status = self.board.get_status( player.id)
            if status:
                print(status)
            if self.board.player_win( player.id ) or not self.board.has_empty_cell():
                break
            self.next_player()







