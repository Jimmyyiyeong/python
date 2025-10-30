from AdventureGame.Inventory.Weapon import *

class Enemy:
    def __init__(self, name, health=None, weapon=None):
        """ Default enemy attributes """
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = weapon

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
Goblin = Enemy("Premature Goblin", 50, Sulfuras)