from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper

DESTINATIONS_OPTIONS = ["1. List of destinations", "2. Most popular destination", "3. Add new destination", "4. Destination information"]


class DestinationsUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()     
        self.destinations_list = self.logic_wrapper.destination_list()   


    def destinations(self) -> str:
        """ TODO: add docstring """
        self.menus.display_options(DESTINATIONS_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action


    def get_all_destinations(self) -> None:
        """ TODO: add docstring """
        print(self.destinations_list)  


    def get_most_popular_destination(self):
        """ TODO: add docstring """
        popular = self.logic_wrapper.popular_destination()
        print(popular)


    def add_destination(self) -> None:
        """ TODO: add docstring """
        print("New destination")
        country = input("Enter the country: ")
        airport = input("Enter the airport: ")
        id = input("Enter the ID: ")
        numeric_id = input("Enter the numeric ID: ")
        distance_from_iceland = input("Enter the distance form Iceland: ")
        contact_name = input("Enter the name of the contact person:")
        contact_number = input("Enter the number of the contact number: ")
        print("New destination:")
        print("Country:", country)
        print("Airport:", airport)
        print("ID:", id)
        print("Numeric ID:", numeric_id)
        print("Distance from Iceland:", distance_from_iceland)
        print("Contact name: ", contact_name)
        print("Contact number: ", contact_number)
        save_prompt = input("Would you like to save this new destionation, (y)es or (n)o? ").lower()
        if save_prompt == "y":
            print("Destination saved!")
        elif save_prompt == "n":
            print("Destionation not saved.")
    
    
    def change_destination_info(self): #define
        """ TODO: add docstring """
        print("What destination would you like to get the information about?")

        