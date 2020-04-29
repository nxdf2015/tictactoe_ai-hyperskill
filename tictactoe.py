
import sys


from game import Game

def get_option():
    choice =  input("Input command: ")
    if choice == "exit":
        return choice

    if  choice.startswith("start") :
        options = choice.split(" ")
        if len(options) == 3:
            return (options[1],options[2])
    return False





def loop():
    choice = ""
    while not choice == "exit":
        choice = get_option()
        if not choice:
            print("Bad parameters!")
            continue
        if not choice == "exit":
            first_player , second_player = choice
            game = Game(first_player,second_player)
            game.start()













if __name__=="__main__":
    loop()
