from .Item import Item

class Weapon(Item):

    
    def __init__(self, name, item_type, min_damage, max_damage, durability = None, rarity = None, range = 1):
        super().__init__(name,item_type, rarity)
        self.item_type = item_type if item_type is not None else "Weapon"
        self.min_damage = min_damage
        self.max_damage = max_damage
        average_damage = (min_damage + max_damage) / 2
        self.durability = durability if durability is not None else round(average_damage * 5)
        self.rarity = rarity if rarity is not None else "Common"
        self.range = range if range is not None else 1

    def describe(self):
        return (
            f"{self.name}, Type: {self.item_type}, Rarity: {self.rarity}, "
            f"Damage: {self.min_damage}-{self.max_damage}, "
            f"Durability: {self.durability}, "
            f"Range: {self.range} "
        )

axe = Weapon("Good Axe",None, 100,120)

