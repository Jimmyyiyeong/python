from AdventureGame.Inventory.Item import *
from AdventureGame.Inventory.Weapon import *
from AdventureGame.Character import *
from AdventureGame.Inventory.Consumables import *

axe = Weapon("Good Axe", 100,120)
sword = Weapon("Ironfang", 5, 10, None, "Rare", 2, 20)
bat = Weapon("Exceptionally Durable Baseball Bat", 10, 200, 1000, "Exceedingly Rare", 3)
Jimmy = Character("Jimmy", 69, "male", "thug", axe)

potion = Item.create("Consumables", "Healthpot", None, False, 50)

bow = Item.create("Weapon", "Rhok'delar, Longbow of the Ancient Keeper", 89, 166)

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

sword = Weapon("Ironfang", 5, 10, None, "Rare", 2, 20)
print(sword.describe())

print(Item.registry)
for item_type, item_class in Item.registry.items():
    print(f"Type: {item_type}, Class: {item_class.__name__}, Attributes: {item_class.attributes}")

print(Goblin.describe())