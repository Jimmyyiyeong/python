from .Inventory import *
from .Inventory import *
from .Util import *

class Character:

    def __init__(self, name, char_type="char", health=0, weapon=None):
        """ Default character attributes """
        self.name = name
        self.weapon = weapon
        self.armor = None
        self.inventory = []
        self.health = health
        self.max_health = health
        self.level = 1
        self.experience = 0
        self.exp_to_next_level = 100

    def greeting(self):
        """ Introduction of player character """
        weapon_name = self.weapon.name if self.weapon else "no weapon"
        print(f"Hello, my name is {self.name} and I wield {weapon_name}. Time to die!\n")

    def gain_experience(self, amount):
        """ Handles exp gain and levelup. Instead of an if statement we use this while loop that supports multiple levelups in case we earn enough experience poimts """
        print(f"{self.name} gains {amount} experience points!\n")
        self.experience += amount
        while self.experience >= self.exp_to_next_level:
            self.experience -= self.exp_to_next_level
            self.level_up()

    def level_up(self):
        """ Increases player level when threshold is reached. Increases max hp by 10% each levelup, heals player to full and increases exp needed to levelup again by 20% """
        self.level += 1
        old_max_hp = self.max_health
        self.max_health = int(self.max_health * 1.1)
        self.health = self.max_health
        self.exp_to_next_level = int(self.exp_to_next_level * 1.20)
        print(f"\n{YELLOW}{self.name}'s level increased to {self.level}!{RESET}")
        print(f"Max HP: {old_max_hp} -> {self.max_health}.\n")

    def is_alive(self):
        """ Checks if health is above 0 """
        return self.health > 0

    def add_to_inventory(self, item):
        """ Adds an item to inventory """
        self.inventory.append(item)
        print(f"{item.name} has been added to {self.name} inventory!\n")

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
    