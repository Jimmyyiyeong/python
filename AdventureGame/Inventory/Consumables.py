from .Item import Item

class Consumables(Item):
    
    def __init__(self, name, rarity = "Common", permanent = False):
        super().__init__(name, rarity)
        self.permanent = permanent
        self.rarity = rarity if rarity is not None else "Common"
        
    def describe(self):
        return (
            f"{self.name}, Rarity: {self.rarity}, "
            f"Permanent: {"Yes" if self.permanent else "No"}, "
        )
        
