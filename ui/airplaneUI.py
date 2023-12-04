# from main_menuUI import MainMenu_UI
class AirplaneUI(MainMenu_UI):
    def __init__(self) -> None:
        MainMenu_UI.display_options(self, AIRPLANE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        
        if action == "m":
            self.display_options(MAIN_MENU_OPTIONS)
        elif action == "1":
            self.types()
        elif action == "2":
            self.airplane.add_airplane()
        elif action == "3":
            self.airplane.add_airplane()

    def types(self):
        MainMenu_UI.display_options(self, ["1. Pilots by license", "2. List all airplane types"])
        action = str(input("Enter your action: ").lower())
        if action == "1":
            MainMenu_UI.display_options(self, ["1. Licensed pilots for a specific airplane type", "2. All pilots listed by license", "3. Number of licensed pilots for each airplane type"])
            action = str(input("Enter your action: ").lower())

        elif action == "2":
            print("all the airplane types")
        

    def add_airplane(self):
        pass

    def most_used_airplane(self):
        pass

    def flown_furthest_airplane(self):
        pass