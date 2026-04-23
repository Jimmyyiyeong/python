from .Character import *
from .Inventory import *

class Enemy(Character):
    def __init__(self, name, health=None, weapon=None, armor=None, level=1, experience_value=50):
        """ Inherits from Character class """
        super().__init__(name=name, char_type="enemy", health=health, weapon=weapon, level=level)
        """ Default enemy attributes """
        self.armor = armor
        self.experience_value = experience_value

    def describe(self):
        """ Description of enemy """
        description = f"{self.name} (HP: {self.health}/{self.max_health})"
        if self.weapon:
            description += f"Weapon: {self.weapon.describe()}"
        else:
            description += f"Weapon: Unarmed"
        return description
    
#PREDEFINED ENEMIES
def goblin():
    return Enemy("Premature Goblin", 50, Sulfuras, Goblin_armor, level=1, experience_value=100)