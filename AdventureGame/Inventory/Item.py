class Item:

    def __init__(self, name, rarity = "Common"):
        self.name = name
        self.rarity = rarity
        
    def describe(self):
        return f"{self.name} ({self.item_type}, Rarity: {self.rarity}, Price: {self.sell_price})"

    def __str__(self):
        return self.describe()
    
    
