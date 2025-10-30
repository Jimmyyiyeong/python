from .Inventory import *
from .Inventory import *

class Character:

    def __init__(self, name, char_type="char", health=0, weapon=None):
        """ Default character attributes """
        self.name = name
        self.weapon = weapon
        self.armor = None
        self.inventory = []
        self.health = health
        self.max_health = health

    def greeting(self):
        """ Introduction of player character """
        weapon_name = self.weapon.name if self.weapon else "no weapon"
        print(f"Hello, my name is {self.name} and I wield {weapon_name}. Time to die!\n")

    def add_to_inventory(self, item):
        """ Adds an item to inventory """
        self.inventory.append(item)
        print(f"{item.name} has been added to your inventory!\n")

    def show_inventory(self):
        """ Display inventory as a list, starting at 1"""
        if not self.inventory:
            print("Your inventory is empty..\n")
            return
        print(f"\n{self.name}'s Inventory:\n")
        for i, item in enumerate(self.inventory, start = 1):
            print(f"{i}. {item.describe()}")
        print("")

    def use_item(self, index):
        """ Uses/equips item/weapon and removes it from inventory """
        try:
            index -= 1
            if 0 <= index < len(self.inventory):
                item = self.inventory.pop(index)
                item.use(self)
            else:
                print("Invalid item selection.\n")
        except(ValueError, IndexError, AttributeError) as e:
                print("Something went wrong while using the item...\n")
    