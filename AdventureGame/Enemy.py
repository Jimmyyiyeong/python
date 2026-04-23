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
    
    def reward_experience(self, player):
            level_difference = self.level - player.level
            multiplier = 1.0 + (level_difference * 0.2)
            multiplier = max(0.1, multiplier)
            return int(self.experience_value * multiplier)
    
#PREDEFINED ENEMIES
def goblin():
    return Enemy("Premature Goblin", 50, Sulfuras, Goblin_armor, level=1, experience_value=100)