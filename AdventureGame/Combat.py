import random

class Combat:
    def __init__(self, player, enemy):
        """ Default attributes """
        self.player = player
        self.enemy = enemy

    def status(self):
        """ Prints player and enemy status """
        print(f"{self.player.name}'s status:")
        print(f"Health: {self.player.health}/{self.player.max_health}")
        if self.player.weapon:
            print(f"Equipped weapon: {self.player.weapon.name}")
        else:
            print("No weapon equipped!")
        print(f"{self.enemy.name}'s health: {self.enemy.health}")