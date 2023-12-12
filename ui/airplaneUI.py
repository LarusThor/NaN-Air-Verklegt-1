from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from model.airplane_model import Airplane


AIRPLANE_OPTIONS = ["1. Airplane types and license", "2. Add new airplane", "3. Airplane usage"]
AIRPLANE_TYPES_AND_LICENSE_OPTIONS = ["1. Pilots by license", "2. List all airplane types"]
PILOTS_BY_LICENSE_OPTIONS = ["1. Licensed pilots for a specific airplane type", "2. All pilots listed by license", "3. Number of licensed pilots for each airplane type"]
AIRPLANE_USAGE = ["1. Get most used airplane", "2. Get airplane that has flown the furthest"]


class AirplaneUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()
        self.airplane_types = self.logic_wrapper.airplane_types()
        self.pilots_license = self.logic_wrapper.pilots_by_license()
        self.flown_furthest = self.logic_wrapper.furthest_flown()
        self.airplane_usage = self.logic_wrapper.airplane_usage()


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
        return action
    

    def list_pilots_by_licanse(self):
        result = ""
        title = "{:<14} | {}".format("Airplane type", "Pilots")
        for keys, values in self.pilots_license.items():
            result += "{:<14} | {} \n".format(keys, ", ".join(sorted(values)))
        self.menus.print_the_info(title, result)


    def types(self) -> str:
        title = "Airplane types: "
        result = ""
        for item in self.airplane_types:
            result += item + "\n"
        self.menus.print_the_info(title, result)


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


    def most_used_airplane(self):
        self.menus.print_the_info("The mose used airplane is:", self.airplane_usage[0])


    def flown_furthest_airplane(self):
        title = "The airplane that has flown the furthest:"
        result = f"Airplane name: {self.flown_furthest[0]} - Distance: {self.flown_furthest[1]}km."
        self.menus.print_the_info(title, result)
