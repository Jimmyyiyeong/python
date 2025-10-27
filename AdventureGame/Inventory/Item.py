class Item:
    registry ={}
    schemas = {}
    
    def __init_subclass__(cls, item_type = None, attributes = None, **kwargs):
        super().__init_subclass__(**kwargs)
        if item_type:
            Item.registry[item_type] = cls
            Item.schemas[item_type] = attributes or []
            cls.item_type = item_type
                    
    def __init__(self, name, rarity = "Common", sell_price = 0):    
        self.item_type = getattr(self.__class__, "item_type", "generic")
        self.name = name
        self.rarity = rarity
        self.sell_price = sell_price
        

    def describe(self):
        return f"{self.name} ({self.item_type}, Rarity: {self.rarity}, Price: {self.sell_price})"

    def __str__(self):
        return self.describe()
    
