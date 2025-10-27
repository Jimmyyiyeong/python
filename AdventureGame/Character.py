from AdventureGame.Weapon import *

class Character:

    def __init__(self, name, age, sex, occupation, weapon = None,):
        self.name = name
        self.age = age
        self.sex = sex
        self.occupation = occupation
        self.weapon = weapon
        self.inventory = []

    def greeting(self):
        weapon_name = self.weapon.name if self.weapon else "no weapon"
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am a {self.sex} {self.occupation} and I wield {weapon_name}. Nice to meet you!")
        print("")

    def add_to_inventory(self, weapon):
        self.inventory.append(weapon)
        print(f"{weapon.name} has been added to your inventory!")

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty..")
            return
        
        for i, weapon in enumerate(self.inventory, 1):
            print(f"{1}. {weapon.name} (Damage: {weapon.min_damage}-{weapon.max_damage} | Durability: {weapon.durability} | Rarity: {weapon.rarity})")
        print("")