from AdventureGame.Inventory.Weapon import *
from AdventureGame.Inventory.Item import *
from AdventureGame.Character import *

axe = Weapon("Good Axe", 100,120)
bat = Weapon("Exceptionally Durable Baseball Bat", 10, 200, 1000, "Exceedingly Rare", 3)
Jimmy = Character("Jimmy", 69, "male", "thug", axe)

Jimmy.greeting()
Jimmy.show_inventory()
Jimmy.add_to_inventory(axe)
Jimmy.show_inventory()
Jimmy.equip_weapon(0)
Jimmy.show_inventory()
Jimmy.greeting()

sword = Weapon("Ironfang", 5, 10, None, "Rare", 2, 20)
print(sword.describe())