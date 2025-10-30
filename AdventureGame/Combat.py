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

    def player_attack(self):
        """ Randomizes damage based on weapon min and max damage. Max is a builtin python function that returns the larger of two values"""
        damage = random.randint(self.player.weapon.min_damage, self.player.weapon.max_damage)
        self.enemy.health = max(0, self.enemy.health - damage)
        print(f"You attack {self.enemy.name} for {damage} damage!\n")

    def enemy_attack(self):
        """ Randomizes damage based on weapon min and max damage. Also checks enemy health"""
        if self.enemy.health <= 0:
            return
        damage = random.randomint(self.enemy.weapon.min_damage, self.enemy.weapon.max_damage)
        self.player.health = max(0, self.player.health - damage)
        print(f"{self.enemy.name} attacks you for {damage} damage!\n")