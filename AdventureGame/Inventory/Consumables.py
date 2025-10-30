from .Item import Item

class Consumables(Item):
    
    def __init__(self, name, effect_amount=0, rarity=None, permanent=False):
        """ `Default object attributes """
        self.name = name
        self.permanent = permanent
        self.rarity = rarity
        self.effect_amount = effect_amount
        
    def describe(self):
        """ Description of consumable """
        return (
            f"{self.name} | Type: {self.item_type} | Rarity: {self.rarity} | "
            f"Permanent: {"Yes" if self.permanent else "No"} "
        )
    
    def use(self, user):
        """ user in this case is placeholder logic for future expansion. It would enable enemies to use potions aswell using the same function """
        old_health = user.health
        user.health = min(user.max_health, user.health + self.effect_amount)
        healed = user.health - old_health

        print(f"\n{user.name} used {self.name} and healed for {healed} HP!")
        print(f"{user.name}'s HP: {user.health}/{user.max_health}\n")
        
#PREDEFINED CONSUMABLES
Minor_health_potion = Consumables("Minor Health Potion", 20, "Common")
Major_Health_potion = Consumables("Major Health Potion", 50, "Common")