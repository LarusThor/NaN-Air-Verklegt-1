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
        self.validation = self.logic_wrapper.validation


    def airplane_options(self) -> str: #1
        """ TODO: add docstring """
        self.menus.display_options("Airplane:", AIRPLANE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    

    def airplane_types_and_licence(self) -> str: # 1-1
        """ TODO: add docstring """
        self.menus.display_options("Airplane types and license:", AIRPLANE_TYPES_AND_LICENSE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    

    def pilots_by_licanse(self) -> None: # 1-1-1
        """ TODO: add docstring """
        self.menus.display_options("Pilots by license:", PILOTS_BY_LICENSE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    

    def get_pilots_for_a_specific_type(self) -> None: # 1-1-1-1
        """Asks the user to enter in an airplane type. Checks if the input is valid. Goes through the airplane types 
        and gets the pilots that are qualified to fly that airplane type. Then calls a function in the menu_manager to print it out."""
        pilots_by_license = self.logic_wrapper.pilots_by_license()
        planes = {(i+1): plane for i, plane in enumerate(pilots_by_license.keys())}

        
        print("Choose plane: \n")

        for index, plane in enumerate(pilots_by_license.keys()):
             print(f"{index + 1}. {plane}")
        

        airplane_choice = int(input("Enter an airplane choice: "))
        print(f"\nAll pilots qualified to fly {planes[airplane_choice]}:") 
        pilots = pilots_by_license[planes[airplane_choice]]

        for pilot in pilots:
            print(pilot)

            

    def list_pilots_by_licanse(self) -> None: # 1-1-1-2
        """Goes through the pilots and license from the logic wrapper and adds it to the result string. 
        Then calls the function in the menu_manager that takes care of printing tha information out."""
        
        title = "{:<14} | {}".format("Airplane type", "Pilots")
        result = ""

        for keys, values in self.logic_wrapper.pilots_by_license().items():
            result += "{:<14} | {} \n".format(keys, ", ".join(sorted(values)))

        self.menus.print_the_info(title, result)


    def get_number_of_pilots_for_airplanes(self) -> None: # 1-1-1-3
        """"Gets the number of pilots that arae qualifid to fly the airplanes. 
        Calls a function in the menu_manager that takes care of printing the information out."""

        title = "Number of pilots that are qualified for each airplane type:"
        result = ""

        for key, value in self.logic_wrapper.pilots_by_license().items():
            result += f"{key}: \n  {len(value)} licensed pilots.\n"

        self.menus.print_the_info(title, result)


    def types(self) -> str: # 1-1-2
        """Gets all of the airplane types and calls a function to print the information out."""

        title = "Airplane types: "
        result = ""

        for item in self.logic_wrapper.airplane_types():
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
        while not self.validation.validate_number_of_seats(number_of_seats):
            print("ERROR: Invalid number of seats \nIt should be and number and under 110 and over 84")
            number_of_seats = input("Enter the number of seats in the airplane: ")
        
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
        """Calls a function in the menu_manager that prints out the options. Then asks the user for their action and returns the input"""
        
        self.menus.display_options("Airplane usage:", AIRPLANE_USAGE)
        action = str(input("Enter your action: ").lower())
        return action


    def most_used_airplane(self) -> None: # 1-3-1
        """Calls a function in the menu_manager that takes care of printing the title and the result of the most used airplane."""

        title = "The mose used airplane is:"
        result = f"{self.logic_wrapper.airplane_usage()[0]} - {self.logic_wrapper.airplane_usage()[1][self.logic_wrapper.airplane_usage()[0]]} voyages"

        self.menus.print_the_info(title, result)


    def flown_furthest_airplane(self) -> None: # 1-3-2
        """Calls a function in the menu_manager that takes care of printing the title and the result of the furthest flown airplane."""

        title = "The airplane that has flown the furthest:"
        result = f"Airplane name: {self.logic_wrapper.furthest_flown()[0]} - Distance: {self.logic_wrapper.furthest_flown()[1]}km."

        self.menus.print_the_info(title, result)
