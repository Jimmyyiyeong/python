class Item:

    def __init__(self, name, item_type, rarity = "Common"):
        self.name = name
        self.item_type = item_type
        self.rarity = rarity
        
    def describe(self):
        return f"{self.name}, Type: {self.item_type}, Rarity: {self.rarity}"

    def __str__(self):
        return self.describe()
    
    
