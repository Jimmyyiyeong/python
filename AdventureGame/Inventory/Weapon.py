from .Item import Item

class Weapon(Item):

    def __init__(self, name, item_type, min_damage, max_damage, durability=None, rarity=None, range=1):
        """ Default wepaon attributes """
        super().__init__(name,item_type, rarity)
        self.item_type = item_type if item_type is not None else "Weapon"
        self.min_damage = min_damage
        self.max_damage = max_damage
        average_damage = (min_damage + max_damage) / 2
        self.durability = durability if durability is not None else round(average_damage * 5)
        self.rarity = rarity if rarity is not None else "Common"
        self.range = range if range is not None else 1

    def describe(self):
        """ Description of weapon """
        return (
            f"{self.name} | Type: {self.item_type} | Rarity: {self.rarity} | "
            f"Damage: {self.min_damage}-{self.max_damage} | "
            f"Durability: {self.durability} | "
            f"Range: {self.range} "
        )
    
    def equip(self, user):
        """ If user equips another weapon, returns old one to inventory """
        if user.weapon:
            print(f"{user.name} unequipped {user.weapon.name} and returned it to inventory.")
            user.inventory.append(user.weapon)
        user.weapon = self
        print(f"{user.name} equipped {self.name}!\n")

    def use(self, user):
        """ Redirects "use" to "equip" for readability and compatability """
        self.equip(user)

# PREDEFINED WEAPONS
Frostmourne = Weapon("Frostmourne", "Weapon", 2, 18, None, "Legendary", 1)
Sulfuras = Weapon("Sulfuras, Hand of Ragnaros", "Weapon", 5, 15, None, "Legendary", 1)
Thunderfury = Weapon("Thunderfury, Blessed blade of the Windseeker", "Weapon", 8, 12, None, "Legendary", 2)
Warglaive = Weapon ("Warglaive of Azznioth", "Weapon", 9, 11, None, "Legendary", 2)
Rhokdelar = Weapon("Rhok'delar, Longbow of the Ancient Keeper", "Weapon", 7, 13, None, "Legendary", 4)

