from abc import abstractmethod
from random import randint



class Human :

    def __init__(self,id):
        self.id =id

    @property
    def show(self):
        return True

    def play(self):
        while True:
            position =  input("Enter the coordinates: ")
            yield position
    
     


class Computer:
    def __init__(self,id):
        self.id = id

    @property
    def show(self):
        return False

    def play(self):
        print('Making move level "easy"')
        while True:
            col =randint(0,3)
            row = randint(0,3)
            yield f"{col} {row}"



    


