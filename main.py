from AdventureGame import *

Jimmy = Character("Jimmy", 69, "male", "thug", 100, Frostmourne)

Jimmy.greeting()
Jimmy.show_inventory()
Jimmy.add_to_inventory(Sulfuras)
Jimmy.add_to_inventory(Minor_health_potion)
Jimmy.show_inventory()
Jimmy.health = 50
Jimmy.use_item(2)
Jimmy.use_item(1)
Jimmy.show_inventory()
Jimmy.greeting()

print(Goblin.describe())