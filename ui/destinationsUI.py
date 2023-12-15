from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from model.destination_model import Destination

DESTINATIONS_OPTIONS = [
    "1. List of destinations",
    "2. Most popular destination",
    "3. Add new destination",
    "4. Change destination information",
]


class DestinationsUI:
    def __init__(self) -> None:
        """ "Instantiate a DestinationUI object."""
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()

    def destinations_options(self) -> str:
        """Displays destination options."""
        self.menus.display_options("Destinations:", DESTINATIONS_OPTIONS)
        action = str(input("Enter your action: ").lower())

        return action

    def get_all_destinations(self) -> None:
        """Will get all the destinations from the logic wrapper and turn them into a one string.
        Then calls a function in the menu_manager that will take care of printing everything out.
        """

        title = "All destinations:"
        result = ""

        destinations = sorted(self.logic_wrapper.only_destinations())
        for destination in list(enumerate(destinations, start=1)):
            result += f"{destination[0]}: {destination[1]}\n"

        user_input = self.menus.print_the_info(title, result)
        return user_input

    def get_most_popular_destination(self) -> None:
        """Gets the most popular destination from the logic wrapper and sends the title and the
        result(the most popular destination) to a function in the menu_manager that takes care of printing it out.
        """
        popular = self.logic_wrapper.popular_destination()
        title = "The most popular destination:"

        user_input = self.menus.print_the_info(title, popular)
        return user_input

    def add_destination(self) -> None:
        """TODO: add docstring"""
        self.validation = self.logic_wrapper.validation

        print("New destination")

        id = input("Enter the 3 letter ID: ").upper()
        destinations = self.logic_wrapper.destination_info_overview()
        while not self.validation.validate_destination_id(id):
            print("ERROR: Invalid ID. \nID has to be a string of length 3. ")
            id = input("Enter the 3 letter ID: ").upper()
            while id in destinations.keys():
                print("Destination already exists, please enter a valid id")
                id = input("Enter the 3 letter ID: ").upper()

        country = input("Enter the destination: ").title()
        while not self.validation.validate_destination_name(country):
            print("ERROR: Invalid destination. \nDestination has to be a string of length > 3. ")
            country = input("Enter the destination: ").title()

        airport = input("Enter the airport: ").title()
        airport_exists = True
        while airport_exists:
            for values in destinations.values():
                if airport in values.airport_name:
                    print("Airport already in use, please enter a valid airport name")
                    airport_exists = True
                    airport = input("Enter the airport: ").title()
                else:
                    airport_exists = False
        while not self.validation.validate_airport(airport):
            print(
                "ERROR: Invalid airport. \nAirport name has to be a string of length > 3 and contain the word Airport."
            )
            airport = input("Enter the airport: ").title()

        distance_from_iceland = input("Enter the distance form Iceland: ")
        while not self.validation.validate_distance_from_iceland(distance_from_iceland):
            print(
                "ERROR: Invalid distance. \nDistance has to be an integer less than 40.000."
            )
            distance_from_iceland = input("Enter the distance form Iceland: ")

        contact_name = input("Enter the name of the contact person: ").title()
        while not self.validation.validate_name(contact_name):
            print("ERROR: Invalid name. \nName has to be a string of length <= 3. ")
            contact_name = input("Enter the name of the contact person: ").title()

        contact_number = input("Enter the number of the contact number: ")
        while not self.validation.validate_number(contact_number):
            print("ERROR: Invalid phone number. \n Phone number should be 7 digits. ")
            contact_number = input("Enter the number of the contact number: ")
            return contact_number

        estimated_flight_time = input("Enter the estimated flight time: ")
        while not self.validation.validate_time(estimated_flight_time):
            print(
                "ERROR: Invalid flight time. \nFlight time should be in the format: 00:00:00. "
            )
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

        save_prompt = input(
            "Would you like to save this new destionation, (y)es or (n)o? "
        ).lower()
        if save_prompt == "y":
            dest = Destination(
                destination_id=id,
                destination=country,
                emergency_contact_name=contact_name,
                emergency_contact_number=contact_number,
                airport_name=airport,
                distance_from_iceland=distance_from_iceland,
                estimated_flight_time=estimated_flight_time,
            )
            self.logic_wrapper.add_destination(dest)
            user_input = self.menus.print_the_info("Destination saved!")
            return user_input
        
        elif save_prompt == "n":
            user_input = self.menus.print_the_info("Destionation not saved.")
            return user_input

    def change_destination_info(self) -> None:
        """Changes information about a destination in the system."""
        # TODO: validate
        destination_list = self.logic_wrapper.destination_list()

        print("\nChanging destination information")
        print("=" * 33)
        print("Choose a destination to change:\n")

        for index, destination in enumerate(destination_list):
            print(f"{index + 1}. {destination.destination}")

        destination_choice = input("Choose destination: ")
        while destination_choice != "1" and destination_choice != "2" and destination_choice != "3" and destination_choice != "4" and destination_choice != "5":
            print("Invalid input! You can choose 1, 2, 3, 4 and 5")
            print("-" * 30)
            destination_choice = input("Destination: ")

        destination_info = destination_list[int(destination_choice) - 1]

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
                    destination_info.airport_name = input(
                        "Enter new airport name: "
                    ).title()
                    action = input("Choose action: ")

                case "2":
                    destination_info.emergency_contact_name = input(
                        "Enter the name for the new emergency contact: "
                    )
                    action = input("Choose action: ")

                case "3":
                    destination_info.emergency_contact_number = input(
                        "Enter a new number for the contact: "
                    ).title()
                    action = input("Choose action: ")

                case "4":
                    print("So you've got fast planes now? ")
                    destination_info.estimated_flight_time = input(
                        "How fast can they fly to the destiantion? "
                    )
                    action = input("Choose action: ")

                case _:
                    break

        print(
            f"{destination_info.destination_id}\n"
            f"Destination: {destination_info.destination}\n"
            f"Emergency contact name: {destination_info.emergency_contact_name}\n"
            f"Emergency contact number: {destination_info.emergency_contact_number}\n"
            f"Airport name: {destination_info.airport_name}\n"
            f"Distance from Iceland: {destination_info.distance_from_iceland}km\n"
            f"Estimated fligth time: {destination_info.estimated_flight_time}\n"
        )

        save_prompt = input(
            "Would you like to save this new destionation, (y)es or (n)o? "
        ).lower()

        if save_prompt == "y":
            self.logic_wrapper.update_destination_info(destination_info)
            user_input = self.menus.print_the_info("Changes have been saved!")
            return user_input
        elif save_prompt == "n":
            user_input = self.menus.print_the_info("Changes were not saved.")
            return user_input
