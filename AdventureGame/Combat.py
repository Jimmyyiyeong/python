from AdventureGame.Util.Styling import RED, RESET, ITALIC, wait_for_continue
import random

class Combat:
    def __init__(self, player, enemy):
        """ Default attributes. When in combat, "Character" is referred to as "player" """

        self.player = player
        self.enemy = enemy

    def character_status(self, character):
        """Prints the status of any character"""

        print(f"\n{character.name}'s status:")
        print(f"Health: {character.health}/{character.max_health}")
    
        if character.weapon:
            print(f"Equipped weapon: {character.weapon.describe()}")
        else:
            print("No weapon equipped!")
    
        if character.armor:
            print(f"Equipped armor: {character.armor.name} (abs: {character.armor.defense})\n")
        else:
            print("No armor equipped.\n")

    def status(self):
        """ Prints player and enemy status """

        self.print_character_status(self.player)
        self.print_character_status(self.enemy)

    def calculate_damage(self, attacker, defender, allow_crit=True):
        """ Combat logic. Randomizes a number between the weapon min and max damage, checks for crit and armor absorption and returns the final damage calculation and printable log 
        Allow crit is implemented in case we want specific attacks or spells to not be able to crit in the future (like DOTs or other effects)"""

        base_damage = random.randint(attacker.weapon.min_damage, attacker.weapon.max_damage)
        crit = False
        crit_damage = base_damage

        if allow_crit and random.random() < attacker.weapon.crit_chance:
            crit = True
            crit_damage = int(base_damage * 1.5)

        absorbed = defender.armor.defense if defender.armor else 0
        final_damage = max(0, crit_damage - absorbed)

        log = ""
        if crit:
            log += f"\n{RED}CRITICAL HIT!{RESET} {attacker.name} attacks {defender.name} with great force and precision, dealing {crit_damage} damage!\n"
        else:
            log += f"\n{attacker.name} attacks {defender.name}, dealing {base_damage} damage!\n"
        if absorbed > 0:
            log += f"{ITALIC}{defender.name}'s {defender.armor.name} absorbs {absorbed} damage!{RESET}\n"

        log += f"{defender.name} takes {final_damage} damage. (HP: {defender.health - final_damage}/{defender.max_health})\n"

        return final_damage, log

    def attack(self, attacker, defender, allow_crit=True):
        """ Calls the calculate_damage function and reduces enemy HP accordingly """

        damage, log = self.calculate_damage(attacker, defender, allow_crit)
        print(log)
        defender.health = max(0, defender.health - damage)

    def engage(self):
        """ Combat loop using a while loop and switch, reading input from player """

        print(f"A wild {self.enemy.name} appears!")

        wait_for_continue()

        while self.enemy.is_alive() and self.player.is_alive():
            print("\n---Battle Menu---")
            print("1. Attack")
            print("2. Inventory")
            print("3. Status")
            print("4. Flee\n")

            choice = input("Choose an action: ").strip()

            if choice == "1":
                self.attack(self.player, self.enemy, allow_crit=True)

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
                    self.attack(self.enemy, self.player, allow_crit=True)
                    continue
                else:
                    print("\nYou fled the battle!\n")
                    return
            else:
                print("Invalid choice.\n")
                continue

            if self.enemy.is_alive():
                self.attack(self.enemy, self.player, allow_crit=True)

        if not self.enemy.is_alive():
            print(f"You have defeated {self.enemy.name}!")
        elif not self.player.is_alive():
            print("You have been defeated... Game over.")