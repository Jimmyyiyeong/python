from .Item import Item

class Armor(Item):
    def __init__(self, name, defense=0, rarity=None):
        super().__init__(name, item_type="Armor", rarity=rarity)
        self.defense = defense

    def describe(self):
        """ Description of armor """
        return f"{self.name} | Type: {self.item_type} | Rarity: {self.rarity} | Defense: {self.defense}"

    def equip(self, user):
        if user.armor:
            print(f"{user.name} unequipped {user.armor.name} and returned it to inventory.")
            user.inventory.append(user.armor)
        user.armor = self
        print(f"{user.name} equipped {self.name}!\n")

    def use(self, user):
        self.equip(user)

#PREDEFINED ARMORS
Cloth_armor = Armor("Magister's Regalia", 2, "Rare")
Leather_armor = Armor("Bloodfang Armor", 3, "Epic")
Mail_armor = Armor("Dragonstalker Regalia", 4, "Epic")
Plate_armor = Armor("Judgement Armor", 6, "Legendary")