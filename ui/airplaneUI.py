from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from model.airplane_model import Airplane


AIRPLANE_OPTIONS = [
    "1. Airplane types and license",
    "2. Add new airplane",
    "3. Airplane usage",
]
AIRPLANE_TYPES_AND_LICENSE_OPTIONS = [
    "1. Pilots by license",
    "2. List all airplane types",
]
PILOTS_BY_LICENSE_OPTIONS = [
    "1. Licensed pilots for a specific airplane type",
    "2. All pilots listed by license",
    "3. Number of licensed pilots for each airplane type",
]
AIRPLANE_USAGE = [
    "1. Get most used airplane",
    "2. Get airplane that has flown the furthest",
]


class AirplaneUI:
    def __init__(self) -> None:
        """ "Instantiate a ArplaneUI object."""
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()
        self.validation = self.logic_wrapper.validation

    def airplane_options(self) -> str:  # 1
        """Displays the options a user can chose in Airplanes."""

        self.menus.display_options("Airplane:", AIRPLANE_OPTIONS)
        action = input("Enter your action: ").lower().strip()

        return action

    def airplane_types_and_licence(self) -> str:  # 1-1

        """Lets a user chose options for airplane types and licence."""
        self.menus.display_options("Airplane types and license:", AIRPLANE_TYPES_AND_LICENSE_OPTIONS)
        user_input = input("Enter your action: ").lower().strip()

        return user_input

    def pilots_by_license(self) -> None:  # 1-1-1
        """Displays user options for pilots by license."""
        
        self.menus.display_options("Pilots by license:", PILOTS_BY_LICENSE_OPTIONS)
        user_input = input("Enter your action: ").lower().strip()

        return user_input
    
    def airplane_usage_options(self) -> str:  # 1-3
        """Calls a function in the menu_manager that prints out the options. Then asks the user for their action and returns the input"""

        self.menus.display_options("Airplane usage:", AIRPLANE_USAGE)
        user_input = input("Enter your action: ").lower().strip()

        return user_input

    def get_pilots_for_a_specific_type(self) -> None:  # 1-1-1-1
        """Asks the user to enter in an airplane type. Checks if the input is valid. Goes through the airplane types
        and gets the pilots that are qualified to fly that airplane type. Then calls a function in the menu_manager to print it out.
        """
        pilots_by_license = self.logic_wrapper.pilots_by_license()
        planes = {(i + 1): plane for i, plane in enumerate(pilots_by_license.keys())}

        print("Choose plane: \n")

        for index, plane in enumerate(pilots_by_license.keys()):
            print(f"{index + 1}. {plane}")

        airplane_choice = input("Enter an airplane choice: ").strip()
        while not self.validation.validate_choice(airplane_choice, len(planes)):
            print("Invalid choice \nTry again.")
            airplane_choice = input("Enter an airplane choice: ").strip()

        title = f"\nAll pilots qualified to fly {planes[int(airplane_choice)]}:"
        result = ""
        pilots = pilots_by_license[planes[int(airplane_choice)]]

        for pilot in pilots:
            result += pilot + "\n"

        user_input = self.menus.print_the_info(title, result)
        return user_input

    def list_pilots_by_license(self) -> None:  # 1-1-1-2
        """Goes through the pilots and license from the logic wrapper and adds it to the result string.
        Then calls the function in the menu_manager that takes care of printing tha information out.
        """

        title = "{:<14} | {}".format("Airplane type", "Pilots")
        result = ""

        for keys, values in self.logic_wrapper.pilots_by_license().items():
            result += "{:<14} | {} \n".format(keys, ", ".join(sorted(values)))

        user_input = self.menus.print_the_info(title, result)
        return user_input

    def get_number_of_pilots_for_airplanes(self) -> None:  # 1-1-1-3
        """ "Gets the number of pilots that arae qualifid to fly the airplanes.
        Calls a function in the menu_manager that takes care of printing the information out.
        """

        title = "Number of pilots that are qualified for each airplane type:"
        result = ""

        for key, value in self.logic_wrapper.pilots_by_license().items():
            result += f"{key}: \n  {len(value)} licensed pilots.\n"

        user_input = self.menus.print_the_info(title, result)
        return user_input

    def types(self) -> str:  # 1-1-2
        """Gets all of the airplane types and calls a function to print the information out."""

        title = "Airplane types: "
        result = ""

        for flight_type_tuple in self.logic_wrapper.airplane_types():
            flight_type_list = []
            for flight_type in flight_type_tuple:
                flight_type_list.append(flight_type)
            result += f"{flight_type_list[0]}\n"

        user_input = self.menus.print_the_info(title, result)
        return user_input

    def add_airplane(self) -> None:  # define
        """Adds airplane to the system."""
        airplane_types = self.logic_wrapper.airplane_types()

        print("\nAdding a new airplane to the system: ")
        print("Examples of airplane names:  TF-EPG, TF-UVR, TF-XZR")

        name = input("Enter airplane insignia: ").strip()
        while not self.validation.validate_airplane_name(name):
            print("ERROR: Invalid airplane insignia. \nInsignia must start with TF- followed by 3 letters. ")
            name = input("Enter airplane insignia: ").strip()

        planes = {(i + 1): plane for i, plane in enumerate(airplane_types)}

        for index, plane in enumerate(airplane_types):
            print(f"{index + 1}. {plane[0]}")

        type_choice = int(input("Enter airplane type: ").strip())
        plane_type = planes[type_choice][0]
        manufacturer = planes[type_choice][1]
        model = planes[type_choice][2]
        number_of_seats = planes[type_choice][3]

        result = f"\nName: {name}\nType: {plane_type}\nManufacturer: {manufacturer}\nModel: {model}\nNumber of seats: {number_of_seats}"
        print(result)

        save_prompt = input("\nWould you like to save this new airplane, (y)es or (n)o? ").lower().strip()        
        if save_prompt == "y":
            airplane = Airplane(name, plane_type, manufacturer, model, number_of_seats)
            self.logic_wrapper.add_airplane(airplane)
            user_input = self.menus.print_the_info("New airplane has been saved!")
            return user_input
        
        elif save_prompt == "n":
            user_input = self.menus.print_the_info("New airplane was not saved")
            return user_input


    def most_used_airplane(self) -> None:  # 1-3-1
        """Calls a function in the menu_manager that takes care of printing the title and the result of the most used airplane."""

        title = "The most used airplane is:"
        result = f"{self.logic_wrapper.airplane_usage()[0]} - {self.logic_wrapper.airplane_usage()[1][self.logic_wrapper.airplane_usage()[0]]} voyages"

        user_input = self.menus.print_the_info(title, result)
        return user_input

    def flown_furthest_airplane(self) -> None:  # 1-3-2
        """Calls a function in the menu_manager that takes care of printing the title and the result of the furthest flown airplane."""

        title = "The airplane that has flown the furthest:"
        result = f"Airplane name: {self.logic_wrapper.furthest_flown()[0]} - Distance: {self.logic_wrapper.furthest_flown()[1]}km."

        user_input = self.menus.print_the_info(title, result)
        return user_input
