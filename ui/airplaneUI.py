from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from model.airplane_model import Airplane


AIRPLANE_OPTIONS = ["1. Airplane types and license", "2. Add new airplane", "3. Airplane usage"]
AIRPLANE_TYPES_AND_LICENSE_OPTIONS = ["1. Pilots by license", "2. List all airplane types"]
PILOTS_BY_LICENSE_OPTIONS = ["1. Licensed pilots for a specific airplane type", "2. All pilots listed by license", "3. Number of licensed pilots for each airplane type"]
AIRPLANE_USAGE = ["1. Get most used airplane", "2. Get airplane that has flown the furthest"]


class AirplaneUI:
    def __init__(self) -> None:
        """ TODO: add docstring """
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()
        self.airplane_types = self.logic_wrapper.airplane_types()
        self.pilots_license = self.logic_wrapper.pilots_by_license()
        self.flown_furthest = self.logic_wrapper.furthest_flown()
        self.airplane_usage = self.logic_wrapper.airplane_usage()
        self.validation = self.logic_wrapper.validation


    def airplane(self) -> str: #1
        """ TODO: add docstring """
        self.menus.display_options(AIRPLANE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    

    def get_pilots_for_a_specific_type(self): # 1-1-1-1
        airplane_type = input("Enter an airplane type: ")# TODO has to be validated
        while not self.validation.validate_aircraft_by_specific_type(airplane_type):
            print("ERROR: Invalid airplane type \nPlease write a airplane type. ")
            airplane_type = str(input("Enter an airplane type: "))
        title = f"Pilots qualified to fly {airplane_type}:"
        result = ""
        for person in self.pilots_license.get(airplane_type):
            result += person + "\n"
        self.menus.print_the_info(title, result)


    def airplane_types_and_licanse(self) -> str: # 1-1
        """ TODO: add docstring """
        self.menus.display_options(AIRPLANE_TYPES_AND_LICENSE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    

    def pilots_by_licanse(self) -> None: # 1-1-1
        """ TODO: add docstring """
        self.menus.display_options(PILOTS_BY_LICENSE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    

    def list_pilots_by_licanse(self): # 1-1-1-2
        """ TODO: add docstring """
        result = ""
        title = "{:<14} | {}".format("Airplane type", "Pilots")
        for keys, values in self.pilots_license.items():
            result += "{:<14} | {} \n".format(keys, ", ".join(sorted(values)))
        self.menus.print_the_info(title, result)

    def get_number_of_pilots_for_airplanes(self): # 1-1-1-3
        """"TODO docstring"""
        title = "Number of pilots that are qualified for each airplane type:"
        result = ""
        for key, value in self.pilots_license.items():
            result += f"{key}: \n  {len(value)} licensed pilots.\n"
        self.menus.print_the_info(title, result)


    def types(self) -> str: # 1-1-2
        """ TODO: add docstring """
        title = "Airplane types: "
        result = ""
        for item in self.airplane_types:
            result += item + "\n"
        self.menus.print_the_info(title, result)


    def add_airplane(self) -> None: #define
        """ TODO: add docstring """
        name = input("Enter airplane name: ")
        while not self.validation.validate_airplane_name(name):
            print("ERROR: Invalid name \nNames of planes \nTF-EPG \nTF-UVR \nTF-XZR \nTF-XZM \nTF-IZE \nTF-PGK \nTF-TYQ \nTF-LNQ \nTF-XUP")
            name = input("Enter an Name: ")
            
        type = input("Enter airplane type: ")
        while not self.validation.validate_aircraft_by_specific_type(type):
            print("ERROR: Invalid airplane type \nPlane types are \nNAFokkerF100 \nNAFokkerF28 \nNABAE146. ")
            type = str(input("Enter an airplane type: "))
            
        manufacturer = input("Enter airplane manufacturer: ")
        while not self.validation.validate_manafacturer_name(manufacturer):
            print("ERROR: Invalid name \nAircraft are  \nFokker \nBAE ")
            manufacturer = input("Enter an manafacturer type: ")
            
        model = input("Enter a Model: ")
        while not self.validation.validate_model_name(model):
            print("ERROR: Invalid model \nModels are \nF100\nF28\n146")
            model = input("Enter a Model: ")
            
        number_of_seats = input("Enter the number of seats in the airplane: ")
<<<<<<< HEAD
        while not self.validation.validate_number_of_seats(number_of_seats):
            print("ERROR: Invalid number of seats \nIt should be and number and under 110 and over 84")
            number_of_seats = input("Enter the number of seats in the airplane: ")
=======
>>>>>>> 057a2820c858bd4364de6b50e3d307e98a74c499
        
        title = "New airplane:"
        result = f"Name: {name}\nType: {type}\nManufacturer: {manufacturer}\nModel: {model}\nNumber of seats: {number_of_seats}"
        
        # print("Name:", name)
        # print("Type:", type)
        # print("Manufacturer:", manufacturer)
        # print("Model:", model)
        # print("Number of seats:", number_of_seats)
        save_prompt = input("Would you like to save this new airplane, (y)es or (n)o? ").lower()
        if save_prompt == "y":
            airplane = Airplane(name,type,manufacturer,model,number_of_seats)
            self.logic_wrapper.add_airplane(airplane)
        else:
            None
        

    def airplane_usage_options(self) -> str: # 1-3
        """ TODO: add docstring """
        self.menus.display_options(AIRPLANE_USAGE)
        action = str(input("Enter your action: ").lower())
        return action


    def most_used_airplane(self): # 1-3-1
        """ TODO: add docstring """
        title = "The mose used airplane is:"
        result = f"{self.airplane_usage[0]} - {self.airplane_usage[1][self.airplane_usage[0]]} voyages"
        self.menus.print_the_info(title, result)


    def flown_furthest_airplane(self): # 1-3-2
        """ TODO: add docstring """
        title = "The airplane that has flown the furthest:"
        result = f"Airplane name: {self.flown_furthest[0]} - Distance: {self.flown_furthest[1]}km."
        self.menus.print_the_info(title, result)
