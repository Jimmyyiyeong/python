from AdventureGame import *

Jimmy = Character("Jimmy", "player", 100, Frostmourne)

""" Jimmy.greeting()
Jimmy.show_inventory() """
Jimmy.add_to_inventory(Sulfuras)
Jimmy.add_to_inventory(Minor_health_potion)
Jimmy.add_to_inventory(Cloth_armor)
""" Jimmy.show_inventory()
Jimmy.health = 50
Jimmy.use_item(2)
Jimmy.use_item(1)
Jimmy.show_inventory()
Jimmy.greeting()
print(Goblin.describe()) """
battle = Combat(Jimmy, Goblin)
Goblin.add_to_inventory(Frostmourne)
Goblin.use_item(1)
battle.engage()