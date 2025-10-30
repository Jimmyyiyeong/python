import random

class Combat:
    def __init__(self, player, enemy):
        """ Default attributes. When in combat, "Character" is referred to as "player" """
        self.player = player
        self.enemy = enemy

    def status(self):
        """ Prints player and enemy status """
        print(f"\n{self.player.name}'s status:")
        print(f"Health: {self.player.health}/{self.player.max_health}")
        if self.player.weapon:
            print(f"Equipped weapon: {self.player.weapon.name}\n")
        else:
            print("No weapon equipped!\n")
        print(f"{self.enemy.name}'s status:")
        print(f"Health: {self.enemy.health}/{self.enemy.max_health}")
        print(f"Equipped weapon: {self.enemy.weapon.name}")

    def player_attack(self):
        """ Randomizes damage based on weapon min and max damage. Max is a builtin python function that returns the larger of two values"""
        damage = random.randint(self.player.weapon.min_damage, self.player.weapon.max_damage)
        self.enemy.health = max(0, self.enemy.health - damage)
        print(f"\nYou attack {self.enemy.name} for {damage} damage!\n")

    def enemy_attack(self):
        """ Randomizes damage based on weapon min and max damage. Also checks enemy health"""
        if self.enemy.health <= 0:
            return
        damage = random.randint(self.enemy.weapon.min_damage, self.enemy.weapon.max_damage)
        self.player.health = max(0, self.player.health - damage)
        print(f"{self.enemy.name} attacks you for {damage} damage!")

    def engage(self):
        """ Combat loop using a while loop and switch, reading input from player """
        print(f"A wild {self.enemy.name} appears!\n")

        while self.enemy.health > 0 and self.player.health > 0:
            print("\n---Battle Menu---")
            print("1. Attack")
            print("2. Inventory")
            print("3. Status")
            print("4. Flee\n")

            choice = input("Choose an action: ").strip()

            if choice == "1":
                self.player_attack()
            elif choice == "2":
                if not self.player.inventory:
                    print("Your inventory is empty. You can't use any items right now.\n")
                while True:
                    self.player.show_inventory()
                    user_input = input("Choose an item number to use (or 'b' to go back): ").strip().lower()
                    if user_input == 'b':
                        print("\nReturning to battle menu...\n")
                        break
                    try:
                        index = int(user_input)
                        self.player.use_item(index)
                        break
                    except ValueError:
                        print("Invalid input. Try again.\n")
                    except IndexError:
                        print("Invalid item. Try again.\n")
            elif choice == "3":
                self.status()
                continue
            elif choice == "4":
                if random.random() < 0.3:
                    print("\nYou attempt to flee but the enemy blocks your path!\n")
                    self.enemy_attack()
                    continue
                else:
                    print("\nYou fled the battle!\n")
                    return
            else:
                print("Invalid choice.\n")
                continue
            if self.enemy.health > 0:
                self.enemy_attack()
        if self.enemy.health <= 0:
            print(f"You have defeated {self.enemy.name}!")
        elif self.player.health <= 0:
            print("You have been defeated... Game over.")