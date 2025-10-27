from AdventureGame.Inventory.Weapon import *

class Character:

    def __init__(self, name, age, sex, occupation, weapon = None):
        self.name = name
        self.age = age
        self.sex = sex
        self.occupation = occupation
        self.weapon = weapon
        self.inventory = []

    def greeting(self):
        weapon_name = self.weapon.name if self.weapon else "no weapon"
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am a {self.sex} {self.occupation} and I wield {weapon_name}. Nice to meet you!")
        print("")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item.name} has been added to your inventory!\n")

    def show_inventory(self):  
        if not self.inventory:
            print("Your inventory is empty..\n")
            return
  
        print(f"{self.name}'s Inventory:")
        for i, item in enumerate(self.inventory):
            print(f"{i}. {item.describe()}")
        print("")

    def equip_weapon(self, index):
        if 0 <= index < len(self.inventory):
            new_weapon = self.inventory.pop(index)
            if self.weapon:     
                self.inventory.append(self.weapon)
            self.weapon = new_weapon
            print(f"{self.name} equipped {self.weapon.name}!\n")
        else:
            print("Invalid weapon selection.\n")