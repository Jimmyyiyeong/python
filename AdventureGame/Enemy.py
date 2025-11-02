from .Character import *
from .Inventory import *
from .Inventory import *

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
    
    def describe(self):
        """ Description of enemy """
        description = f"{self.name} (HP: {self.health}/{self.max_health})"
        if self.weapon:
            description += f"Weapon: {self.weapon.describe()}"
        else:
            description += f"Weapon: Unarmed"
        return description
    
#PREDEFINED ENEMIES
Goblin = Enemy("Premature Goblin", 50, Sulfuras, Goblin_armor)