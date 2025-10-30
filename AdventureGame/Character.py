from AdventureGame.Inventory.Weapon import *
from AdventureGame.Inventory.Consumables import *

class Character:

    def __init__(self, name, age, sex, occupation, health=100, weapon=None):
        """ Default character attributes """
        self.name = name
        self.age = age
        self.sex = sex
        self.occupation = occupation
        self.weapon = weapon
        self.inventory = []
        self.health = health
        self.max_health = health

    def greeting(self):
        """ Introduction of player character """
        weapon_name = self.weapon.name if self.weapon else "no weapon"
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am a {self.sex} {self.occupation} and I wield {weapon_name}. Nice to meet you!\n")

    def add_to_inventory(self, item):
        """ Adds an item to inventory """
        self.inventory.append(item)
        print(f"{item.name} has been added to your inventory!\n")

    def show_inventory(self):
        """ Display inventory as a list, starting at 1"""
        if not self.inventory:
            print("Your inventory is empty..\n")
            return
  
        print(f"{self.name}'s Inventory:")
        for i, item in enumerate(self.inventory, start = 1):
            print(f"{i}. {item.describe()}")
        print("")

    def use_item(self, index):
        """ Uses/equips item/weapon and removes it from inventory """
        index -= 1  
        if 0 <= index < len(self.inventory):
            item = self.inventory.pop(index)
            item.use(self)
        else:
            print("Invalid item selection.\n")
    