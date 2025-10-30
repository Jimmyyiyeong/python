class Item:

    def __init__(self, name, item_type="Item", rarity=None):
        """ Default item attributes """
        self.name = name
        self.item_type = item_type
        self.rarity = rarity
        
    def describe(self):
        """ Description of item """
        return f"{self.name}, Type: {self.item_type}, Rarity: {self.rarity} "

    def __str__(self):
        """ Returns describe function as a string """
        return self.describe()
    
    def use (self, user):
        """ Default behavior for items (may be overridden) """
        print(f"{self.name} cannot be used directly.")
    
    
