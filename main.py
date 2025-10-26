from AdventureGame.Weapon import *
from AdventureGame.Character import *

axe = Weapon("Good Axe", 100,120)
bat = Weapon("Exceptionally Durable Baseball Bat", 10, 200, 1000, "Exceedingly Rare", 3)
Jimmy = Character("Jimmy", 69, "male", "thug", axe)

Jimmy.greeting()
#bat.weapon_info()

