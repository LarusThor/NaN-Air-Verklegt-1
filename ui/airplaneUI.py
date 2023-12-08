from ui.menu_managerUI import Menu
from logic.LogicWrapper import LogicWrapper
from model.airplane_model import Airplane
 
AIRPLANE_OPTIONS = ["1. Airplane types and license", "2. Add new airplane", "3. Airplane usage"]
AIRPLANE_TYPES_AND_LICENSE_OPTIONS = ["1. Pilots by license", "2. List all airplane types"]
PILOTS_BY_LICENSE_OPTIONS = ["1. Licensed pilots for a specific airplane type", "2. All pilots listed by license", "3. Number of licensed pilots for each airplane type"]
AIRPLANE_USAGE = ["1. Get most used airplane", "2. Get airplane which flown furthest"]


class AirplaneUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()
        self.airplane_types = self.logic_wrapper.airplane_types()


    def airplane(self) -> str:
        self.menus.display_options(AIRPLANE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action


    def airplane_types_and_licanse(self) -> str: #if nr 1 from AIRPLANE_OPTIONS is chosen
        self.menus.display_options(AIRPLANE_TYPES_AND_LICENSE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    

    def pilots_by_licanse(self) -> None: # if nr 1 from AIRPLANE_TYPES_AND_LICENSE_OPTIONS is chosen
        self.menus.display_options(PILOTS_BY_LICENSE_OPTIONS)
        action = str(input("Enter your action: ").lower())
    

    def types(self) -> str:
        for item in self.airplane_types:
            print(item)
        print()
        print("(M)enu  (R)epeat")
        action = str(input("Enter your action: ").lower())
        return action


    def add_airplane(self): #define
        name = input("Enter airplane name: ")
        type = input("Enter airplane type: ")
        manufacturer = input("Enter airplane manufacturer: ")
        model = input("Enter a Model: ")
        number_of_seats = input("Enter the number of seats in the airplane: ")
        print("New airplane: ")
        print("Name:", name)
        print("Type:", type)
        print("Manufacturer:", manufacturer)
        print("Model:", model)
        print("Number of seats:", number_of_seats)
        save_prompt = input("Would you like to save this new airplane, (y)es or (n)o? ").lower()
        airplane = Airplane(name,type,manufacturer,model,number_of_seats)
        self.logic_wrapper.add_airplane(airplane)
        

    def airplane_usage_options(self) -> str:
        self.menus.display_options(AIRPLANE_USAGE)
        action = str(input("Enter your action: ").lower())
        return action


    def most_used_airplane():
        pass


    def flown_furthest_airplane():
        pass