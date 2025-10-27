from AdventureGame import *

axe = Weapon("Good Axe", None, 100,120)
sword = Weapon("Ironfang", "Sword", 5, 10, None, "Rare", 2)
bat = Weapon("Exceptionally Durable Baseball Bat","Club", 10, 200, 1000, "Exceedingly Rare", 3)
Jimmy = Character("Jimmy", 69, "male", "thug", axe)

potion = Consumables("Healthpot",None, None, False)

bow = Weapon("Rhok'delar, Longbow of the Ancient Keeper","Bow", 89, 166, None, "Legendary", 4)

Jimmy.greeting()
Jimmy.show_inventory()
Jimmy.add_to_inventory(axe)
Jimmy.add_to_inventory(sword)
Jimmy.add_to_inventory(bow)
Jimmy.add_to_inventory(potion)
Jimmy.show_inventory()
Jimmy.equip_weapon(1)
Jimmy.show_inventory()
Jimmy.greeting()

sword = Weapon("Ironfang",None, 5, 10, None, "Rare", 2)
print(sword.describe())

print(Goblin.describe())