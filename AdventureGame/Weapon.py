from AdventureGame.Items import Item

class Weapon(Item):
    def __init__(self, name, min_damage, max_damage, durability = None, rarity = "Common", range = 1):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        average_damage = (min_damage + max_damage) / 2

        if durability is None:
            self.durability = round(average_damage * 5)
        else:
            self.durability = durability
        if rarity is None:
            self.rarity = "Common"
        else:
            self.rarity = rarity
        if range is None:
            self.range = 1
        else:
            self.range = range

    def describe(self):
        return (
            f"{self.name} (Damage: {self.min_damage} - {self.max_damage} | Rarity: {self.rarity} | Durability: {self.durability} | Range: {self.range})"
        )


if __name__ == "__main__":
    sword = Weapon("Ironfang", 5, 10)
    sword.weapon_info()
