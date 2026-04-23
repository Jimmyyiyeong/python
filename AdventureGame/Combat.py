from .Util import *
import random

class Combat:
    def __init__(self, player, enemy):
        """ Default attributes. When in combat, "Character" is referred to as "player" """
        self.player = player
        self.enemy = enemy

    def combat_status(self):
        """ Prints player and enemy status """
        self.player.status()
        self.player.progress()
        self.player.equipment()
        self.enemy.status()
        self.enemy.equipment()

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
        log += f"{defender.name} takes {final_damage} damage. (HP: {defender.health - final_damage}/{defender.max_health})"
        return final_damage, log
    
    def attack(self, attacker, defender, allow_crit=True):
        """ Calls the calculate_damage function and reduces enemy HP accordingly """

        damage, log = self.calculate_damage(attacker, defender, allow_crit)
        print(log)
        defender.health = max(0, defender.health - damage)

    def start_turn(self):
        """ Placeholder for checking status effects in the future """

    def player_turn(self):
        """ Players turn to act with allowing some actions not to consume a turn using a while loop and switch for choices """
        while True:
            print("\n---Battle Menu---")
            print("1. Attack")
            print("2. Inventory")
            print("3. Status")
            print("4. Flee")
            choice = input("> ").strip()
            if choice == "1":
                self.attack(self.player, self.enemy, allow_crit=True)
                return False
            elif choice == "2":
                used_item = self.player.open_inventory()
                if used_item:
                    return False
            elif choice == "3":
                self.combat_status()
                continue
            elif choice == "4":
                if random.random() < 0.3:
                    print("\nYou attempt to flee but the enemy blocks your path!\n")
                    self.attack(self.enemy, self.player, allow_crit=True)
                    continue
                else:
                    print("\nYou fled the battle!")
                    return True
            else:
                print("Invalid choice.\n")

    def enemy_turn(self):
        self.attack(self.enemy, self.player)

    def end_combat(self):
        """ Rewards experience if you win and game over if you lose """
        if not self.enemy.is_alive():
            print(f"\nYou have defeated {self.enemy.name}!\n")
            Experience = self.enemy.reward_experience(self.player)
            self.player.gain_experience(Experience)
        elif not self.player.is_alive():
            print(f"\n{self.enemy.name} slapped you so hard your ancestors got dizzy lol\n")

    def engage(self):
        """ Combat loop """
        print(f"\nA wild {self.enemy.name} appears!")
        wait_for_continue()

        while self.player.is_alive() and self.enemy.is_alive():

            self.start_turn()

            if self.player_turn():
                break

            if self.enemy.is_alive():
                self.enemy_turn()

        self.end_combat()