from .Item import Item

class Consumables(Item):
    item_type = "Consumables"
    attributes = ["name", "permanent"]
    
    def __init__(self, name, rarity = "Common", permanent = False, sell_price = 0, ):
        super().__init__(name, rarity, sell_price)
        self.name = name
        self.permanent = permanent
        self.rarity = rarity if rarity is not None else "Common"
        
    def describe(self):
        return (
            f"{self.name}, Type: {self.item_type}, Rarity: {self.rarity}, "
            f"Permanent: {"Yes" if self.permanent else "No"}, "
            f"Sell Price: {self.sell_price} "
        )
        
        
Item.registry["Consumables"] = Consumables
