from .Item import Item

class Weapon(Item):
    item_type = "Weapon"
    attributes = ["name", "min_damage", "max_damage", "durability", "range"]
    
    def __init__(self, name, min_damage, max_damage, durability = None, rarity = "Common", range = 1, sell_price = 0):
        super().__init__(name, rarity, sell_price)
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
            f"Range: {self.range}, "
            f"Sell Price: {self.sell_price} "
        )

