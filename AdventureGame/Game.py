from AdventureGame import *
from .Inventory import *

class Game:
    def run(self):
        self.setup()
        self.game.loop()
        self.end()

    def setup(self):
        print("Welcome to the jianghu! Ni jiao shenme?\n")
        name = input("Jiao: ").strip()
    
        print("\nChoose your starting weapon:")
        print("1. Frostmourne (2-18 dmg, 50% crit)")
        print("2. Sulfuras (5-15 dmg, 10% crit)")
        print("3. Thunderfury (8-12 dmg, 10% crit)")
    
        starting_weapons = {
            "1": Frostmourne,
            "2": Sulfuras,
            "3": Thunderfury
        }
    
        choice = input("\nChoose (1-3): ").strip()
        weapon = starting_weapons.get(choice, Frostmourne)
    
        self.player = Character(name, health=100, weapon=weapon)
        print(f"\nWelcome, {self.player.name}! Your jianghu adventure begins...\n")