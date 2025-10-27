from AdventureGame.Weapon import Weapon

class Enemy:
    def __init__(self, name, health=None, weapon=None):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = weapon

    def is_alive(self):
        return self.health > 0