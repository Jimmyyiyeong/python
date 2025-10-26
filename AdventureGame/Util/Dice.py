import random

class Die():
    def __init__(self, number_of_faces):
        self.number_of_faces = number_of_faces

    def roll(self):
        return random.randint(1, self.number_of_faces)
    



die1 = Die(8)

print(die1.roll())
