from .Item import Item

class Consumables(Item):
    
    def __init__(self, name, item_type, rarity = "Common", permanent = False):
        super().__init__(name, item_type, rarity)
        self.permanent = permanent
        self.item_type = item_type if item_type is not None else "Consumable"
        self.rarity = rarity if rarity is not None else "Common"
        
    def describe(self):
        return (
            f"{self.name},Type: {self.item_type} Rarity: {self.rarity}, "
            f"Permanent: {"Yes" if self.permanent else "No"}, "
        )
        
