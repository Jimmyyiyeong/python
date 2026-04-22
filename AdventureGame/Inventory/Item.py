class Item:

    def __init__(self, name, item_type="Item", rarity=None, description=""):
        """ Default item attributes """
        self.name = name
        self.item_type = item_type
        self.rarity = rarity if rarity is not None else "Common"
        self.description = description
        
    def describe(self):
        """ Description of item """
        base = f"{self.name} | Type: {self.item_type} | Rarity: {self.rarity} | "
        if self.description:
            base += f"{self.description}"
        return base

    def __str__(self):
        """ Returns describe function as a string """
        return self.describe()
    
    def use (self, user):
        """ Default behavior for items (may be overridden) """
        print(f"{self.name} cannot be used directly.")
    
    
