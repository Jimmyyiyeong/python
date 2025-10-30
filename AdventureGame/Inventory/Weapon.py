from .Item import Item

class Weapon(Item):

    def __init__(self, name, min_damage, max_damage, rarity=None, crit_chance=0.1):
        """ Inherits attributes from Item class """
        super().__init__(name, item_type="Weapon", rarity=rarity)
        """ Default wepaon attributes """
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.crit_chance = float(crit_chance)

    def describe(self):
        """ Description of weapon """
        return (
            f"{self.name} | Type: {self.item_type} | Rarity: {self.rarity} | Damage: {self.min_damage}-{self.max_damage} | Crit Chance: {self.crit_chance}")
    
    def equip(self, user):
        """ If user equips another weapon, returns old one to inventory """
        if user.weapon:
            print(f"\n{user.name} unequipped {user.weapon.name} and returned it to inventory.")
            user.inventory.append(user.weapon)
        user.weapon = self
        print(f"{user.name} equipped {self.name}!\n")

    def use(self, user):
        """ Redirects "use" to "equip" for readability and compatability """
        self.equip(user)

# PREDEFINED WEAPONS
Frostmourne = Weapon("Frostmourne", 2, 18, "Legendary", 0.5)
Sulfuras = Weapon("Sulfuras, Hand of Ragnaros", 5, 15, "Legendary")
Thunderfury = Weapon("Thunderfury, Blessed blade of the Windseeker", 8, 12, "Legendary")
Warglaive = Weapon ("Warglaive of Azznioth", 9, 11, "Legendary")
Rhokdelar = Weapon("Rhok'delar, Longbow of the Ancient Keeper", 7, 13, "Legendary")