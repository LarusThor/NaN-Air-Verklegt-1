from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from model.destination_model import Destination


DESTINATIONS_OPTIONS = ["1. List of destinations", "2. Most popular destination", "3. Add new destination", "4. Change destination information"]
CHANGE_OPTIONS = ["1. Everyting", "2. Contact information", "3. Airport"]


class DestinationsUI:
    def __init__(self) -> None:
        """ TODO: add docstring """
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()     


    def destinations(self) -> str:
        """ TODO: add docstring """
        self.menus.display_options("Destinations:", DESTINATIONS_OPTIONS)
        action = str(input("Enter your action: ").lower())

        return action

    
    def select_info(self) -> str:
        self.menus.display_options("What information would you like to change?", CHANGE_OPTIONS)
        action = str(input("Enter your action: ").lower())

        return action


    def get_all_destinations(self) -> None:
        """Will get all the destinations from the logic wrapper and turn them into a one string. 
        Then calls a function in the menu_manager that will take care of printing everything out."""

        title = "All destinations:"
        result = ""

        destinations = sorted(self.logic_wrapper.only_destinations())
        for destination in list(enumerate(destinations, start=1)):
            result += f"{destination[0]}: {destination[1]}\n"

        self.menus.print_the_info(title, result)


    def get_most_popular_destination(self) -> None:
        """Gets the most popular destination from the logic wrapper and sends the title and the 
        result(the most popular destination) to a function in the menu_manager that takes care of printing it out."""

        popular = self.logic_wrapper.popular_destination()
        title = "The most popular destination:"

        self.menus.print_the_info(title, popular[0])


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



    def change_destination_info(self) -> None: #define
        """ TODO: add docstring """
        #TODO: validate
        destination_list = self.logic_wrapper.destination_list()
        destinations = {(i+1): destination for i, destination in enumerate(destination_list)}

        print("\nChanging destination information")
        print("Choose a destination to change\n")

        for index, destination in destinations.items():
            print(f"{index}. {destination.destination}")

        destination_choice = int(input("Choose destination: "))
        destination_info = destinations[destination_choice]


        #setting up variables to use later
        destination_id = destination_info.destination_id
        destination = destination_info.destination
        contact = destination_info.emergency_contact_name
        emergency_contact_number = destination_info.emergency_contact_number
        airport_name = destination_info.airport_name
        distance_from_iceland = destination_info.distance_from_iceland
        estimated_flight_time = destination_info.estimated_flight_time


        print(f"Options to change for {destination_info.destination}")
        options = f"""
            1: Choose a new airport
            2: Choose a new contact for destination
            3: Change contacts phone number
            4: Change estimated flight time (faster planes)

            Press any other key to quit changing
    """
        print(options)
        action = input("Choose action: ").strip()

        while action != "q":
            match action:
                case "1":
                    airport_name = input("Enter new airport name: ").title()
                    action = input("Choose action: ")

                case "2":
                    contact = input("Enter the name for the new emergency contact: ")
                    action = input("Choose action: ")

                case "3":
                    emergency_contact_number = input("Enter a new number for the contact: ").title()
                    action = input("Choose action: ")

                case "4":
                    print("So you've got fast planes now? ")
                    estimated_flight_time = input("How fast can they fly to the destiantion? ")
                    action = input("Choose action: ")

                case _:
                    break


        dest = Destination(destination_id = destination_id, 
            destination = destination, 
            emergency_contact_name = contact, 
            emergency_contact_number = emergency_contact_number, 
            airport_name = airport_name, 
            distance_from_iceland = distance_from_iceland, 
            estimated_flight_time = estimated_flight_time)
        
        print(f"{dest.destination_id}\n"
                f"Destination: {dest.destination}\n"
                f"Emergency contact name: {dest.emergency_contact_name}\n"
                f"Emergency contact number: {dest.emergency_contact_number}\n"
                f"Airport name: {dest.airport_name}\n"
                f"Distance from Iceland: {dest.distance_from_iceland}km\n"
                f"Estimated fligth time: {dest.estimated_flight_time}\n")
        
        save_prompt = input("Would you like to save this new destionation, (y)es or (n)o? ").lower()
        
        if save_prompt == "y":
            self.logic_wrapper.update_destination_info(dest)
            self.menus.print_the_info("Changes have been saved!")
        elif save_prompt == "n":
            self.menus.print_the_info("Changes were not saved.")


    # def change_contact_info(self) -> None:#TODO: eyða
    #     """ TODO: add docstring """
    #     print("\nChanging the contact information: ")
    #     id = input("Enter the ID of the destination you would like to change: ")
    #     contact_name = input("Enter the name of the contact person: ")
    #     contact_number = input("Enter the number of the contact number: ")

    #     all_dests = LogicWrapper().destination_list()

    #     counter = 0
    #     for destination in all_dests:
    #         if destination.destination_id == id:
    #             break
    #         else:
    #             counter += 1

    #     dest = all_dests[counter]
    #     dest.emergency_contact_name = contact_name
    #     dest.emergency_contact_number = contact_number

    #     self.logic_wrapper.update_contact_info(dest)
        
    #     self.menus.print_the_info("Changes have been saved!")
        

    # def change_airport_info(self) -> None:#TODO: eyða
    #     """ TODO: add docstring """
    #     print("\nChanging the airport: ")
    #     id = input("Enter the ID of the destination you would like to change: ")
    #     airport = input("Enter new airport name: ")

    #     all_dests = LogicWrapper().destination_list()

    #     counter = 0
    #     for destination in all_dests:
    #         if destination.destination_id == id:
    #             break
    #         else:
    #             counter += 1

    #     dest = all_dests[counter]
    #     dest.airport_name = airport

    #     self.logic_wrapper.update_contact_info(dest)

    #     self.menus.print_the_info("Changes have been saved!")
