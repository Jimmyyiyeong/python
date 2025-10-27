from AdventureGame.Weapon import *
from AdventureGame.Character import *
from AdventureGame.Enemy import *

Jimmy = Character("Jimmy", 69, "male", "thug", axe)

Jimmy.greeting()
Jimmy.show_inventory()
Jimmy.add_to_inventory(axe)
Jimmy.show_inventory()
Jimmy.equip_weapon(0)
Jimmy.show_inventory()
Jimmy.greeting()

print(Goblin.describe())