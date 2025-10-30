from AdventureGame.Character import *
from AdventureGame.Inventory.Weapon import *
from AdventureGame.Inventory.Armor import *

class Enemy(Character):
    def __init__(self, name, health=None, weapon=None, armor=None):
        """ Inherits from Character class """
        super().__init__(name=name, char_type="enemy", health=health, weapon=weapon)
        """ Default enemy attributes """
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.health = health
        self.max_health = health

    def is_alive(self):
        """ Checks if health is above 0 """
        return self.health > 0
    
    def describe(self):
        """ Description of enemy """
        description = f"{self.name} (HP: {self.health}/{self.max_health})"
        if self.weapon:
            description += f"Weapon: {self.weapon.describe()}"
        else:
            description += f"Weapon: Unarmed"
        return description
    
#PREDEVINED ENEMIES
Goblin = Enemy("Premature Goblin", 50, Sulfuras, Goblin_armor)