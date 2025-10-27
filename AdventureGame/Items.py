class Item:
    def __init__(self, name, rarity="Common"):
        self.name = name
        self.rarity = rarity

    def describe(self):
        return f"{self.name} (Rarity: {self.rarity})"

    def __str__(self):
        return self.describe()