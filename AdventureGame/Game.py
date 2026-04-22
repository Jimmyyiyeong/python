from AdventureGame import *

class Game:
    def run(self):
        """ What is actually being ran when you start the game """
        self.setup()
        self.game_loop()
        self.end()

    def setup(self):
        """ Asks for a name, creates the player object and provides an option for starting weapon """
        print("Welcome to the jianghu! Ni jiao shenme?\n")
        name = input("Jiao: ").strip()
    
        print("\nChoose your starting weapon:")
        print(f"1. {Frostmourne.describe()}")
        print(f"2. {Sulfuras.describe()}")
        print(f"3. {Thunderfury.describe()}")
    
        starting_weapons = {
            "1": Frostmourne,
            "2": Sulfuras,
            "3": Thunderfury
        }
    
        choice = input("\nChoose (1-3): ").strip()
        weapon = starting_weapons.get(choice, Frostmourne)
    
        self.player = Character(name, health=100, weapon=weapon)
        self.player.add_to_inventory(Minor_health_potion, 3)

        print(f"Welcome, {self.player.name}! Your jianghu adventure begins...\n")

    def menu(self):
        """ Main menu """
        print("Choose an action:")
        print("1. Fight")
        print("2. Inventory")
        print("3. Status")
        print("4. Exit game")

    def action(self, choice):
        """" What happens depending on player choice """
        if choice == "1" or choice == "fight":
            enemy = goblin()
            Combat(self.player, enemy).engage()
        elif choice == "2" or choice == "inventory":
            self.player.open_inventory()
        elif choice == "3" or choice == "status":
            self.player.status()
            self.player.progress()
            self.player.equipment()
        elif choice == "4" or choice == "exit":
            print("Exiting game..")
            exit()

    def game_loop(self):
        """ TBD """
        while self.player.is_alive():
            self.menu()
            choice = input("> ").strip().lower()
            self.action(choice)

    def end(self):
        """ TBD """
        if self.player.is_alive():
            print("You win!")
        else:
            print("You lose!")