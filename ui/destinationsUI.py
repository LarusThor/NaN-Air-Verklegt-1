from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from model.destination_model import Destination

DESTINATIONS_OPTIONS = ["1. List of destinations", "2. Most popular destination", "3. Add new destination", "4. Change destination information"]


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
        print()
        print("All destinations:")
        print("-"*15)
        self.print_destination(self.destinations_list)  


    def get_most_popular_destination(self):
        """ TODO: add docstring """
        popular = self.logic_wrapper.popular_destination()
        print()
        print("The most popular destination:")
        print("-"*30)
        print(popular[0])
        print()
        print("(H)ome  (B)ack")
        action = input("Enter your action: ")
        return action


    def add_destination(self) -> None:
        """ TODO: add docstring """
        print("New destination")
        id = input("Enter the ID: ")
        country = input("Enter the country: ")
        airport = input("Enter the airport: ")
        distance_from_iceland = input("Enter the distance form Iceland: ")
        contact_name = input("Enter the name of the contact person:")
        contact_number = input("Enter the number of the contact number: ")
        estimated_flight_time = input("Enter the estimated flight time: ")
        
        print("New destination:")
        print("=" + "-=" * 20)
        print("Country:", country)
        print("Airport:", airport)
        print("ID:", id)
        print("Distance from Iceland:", distance_from_iceland)
        print("Estimated flight time: ", estimated_flight_time)
        print("Contact name: ", contact_name)
        print("Contact number: ", contact_number)
        save_prompt = input("Would you like to save this new destionation, (y)es or (n)o? ").lower()
        if save_prompt == "y":
            print("Destination saved!")
            dest = Destination(destination_id = id, 
            destination = country, 
            emergency_contact_name = contact_name, 
            emergency_contact_number = contact_number, 
            airport_name = airport, 
            distance_from_iceland = distance_from_iceland, 
            estimated_flight_time = estimated_flight_time)
            self.logic_wrapper.add_destination(dest)
        elif save_prompt == "n":
            print("Destionation not saved.")
    
    
    def change_destination_info(self): #define
        """ TODO: add docstring """
        id = input("what destination do you want to change ID: ")
        country = input("Enter the country: ")
        airport = input("Enter the airport: ")
        distance_from_iceland = input("Enter the distance form Iceland: ")
        contact_name = input("Enter the name of the contact person:")
        contact_number = input("Enter the number of the contact number: ")
        estimated_flight_time = input("Enter the estimated flight time: ")
        
        all_dests = self.logic_wrapper.destination_list()
        counter = 0
        for destination in all_dests:
            if destination.destination_id == id:
                break
            else:
                counter += 1
        dest = all_dests[counter]
        dest.destination_id = id
        dest.destination = country
        dest.emergency_contact_name = contact_name
        dest.emergency_contact_number = contact_number
        dest.airport_name = airport
        dest.distance_from_iceland = distance_from_iceland
        dest.estimated_flight_time = estimated_flight_time

        self.logic_wrapper.update_destination_info(dest)

    def print_destination(self, destination_list) -> None:
        """function used to print out a list"""
        destination_list.sort()
        for destination in destination_list:
            print(destination)
        print()
        print("(M)enu  (R)epeat")
        action = str(input("Enter your action: ").lower())
        if action == "m":
            None
        elif action == "r":
            None


    '''destination_id: str
    destination: str
    emergency_contact_name: str
    emergency_contact_number: str
    airport_name: str
    distance_from_iceland: str
    estimated_flight_time: str
'''