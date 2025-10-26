from AdventureGame.Weapon import *

class Character:
    def __init__(self, name, age, sex, occupation, weapon = None):
        self.name = name
        self.age = age
        self.sex = sex
        self.occupation = occupation
        self.weapon = weapon


    def greeting(self):
        weapon_name = self.weapon.name if self.weapon else "no weapon"
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am a {self.sex} {self.occupation} and I wield {weapon_name}. Nice to meet you!")
        print("")