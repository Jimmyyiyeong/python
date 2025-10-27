from AdventureGame.Weapon import *

class Enemy:
    def __init__(self, name, health=None, weapon=None):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = weapon

    def is_alive(self):
        return self.health > 0
    
    def describe(self):
        description = f"{self.name} (HP: {self.health}/{self.max_health})"
        if self.weapon:
            description += f" (Weapon: {self.weapon.describe()}"
        else:
            description += f" (Weapon: Unarmed"
        return description
    
#ENEMYLIST
    
Goblin = Enemy("Premature Goblin", 50, weapon=axe)