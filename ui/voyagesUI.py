# TODO: Remove all the commented code
# TODO: Add typehints
# TODO: add input validation

from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from datetime import datetime
from model.upcoming_voyage_model import UpcomingVoyage

VOYAGES_OPTIONS = [
    "1. Create a voyage",
    "2. List of voyages",
    "3. Staff a voyage",
    "4. cancel a voyage",
]
LIST_VOYAGES_OPTIONS = ["1. List of voyages by day", "2. List of voyages by week"]
PAST_OR_PRESENT_VOYAGES = ["1. List of upcoming voyages", "2. List of past voyages"]
VOYAGE_HEADER = "{:^10}{:^10}{:^6}{:^22}{:^22}{:^15}{:^17}{:^27}".format(
    "Flight Number",
    "From",
    "To",
    "Departure Time",
    "Arrival Time",
    "Captain",
    "Copilot",
    "Flight Service Manager",
)


class VoyagesUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()

    def voyages_options(self) -> str:
        self.menus.display_options(VOYAGES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action


    def add_voyage(self) -> None:
        """ TODO: add docstring. """
        print("New voyage: ")

        find_last_id = list(self.logic_wrapper.upcoming_voyages().keys())

        the_last_id = find_last_id[-1]
        flight_number = input("Enter flight number: ")
        departure_location = input("Enter 3 letter keyword for departure location: ")
        arrival_location = input("Enter 3 letter keyword for arrival location: ")
        departure_date = input(f"Enter departure date from {departure_location}; year-month-day: ")
        departure_time = input(f"Enter departure time from {departure_location}: ")
        return_flight_date = input(f"Enter departure date from {arrival_location}; year-month-day: ")
        return_flight_time = input(f"Enter departure time from {arrival_location}: ")
        aircraft_id = input("Enter a valid aircraft: ")


        # TODO: add comment
        departure_date_time = departure_date + " " + departure_time
        arrival_date_time = return_flight_date + " " + return_flight_time

        unstaffed = "N/A"
        the_last_id = int(the_last_id)
        the_last_id += 1
        

        print("New voyage: ") #TODO laga þetta heheheh
        print("~" * 20)
        print("Flight id: ", the_last_id)
        print("Flight Number: ", flight_number)
        print("Departure Location: ", departure_location)
        print("Arrival Location: ", arrival_location)
        print("Departure date and time: ", departure_date_time)
        print("Arrival date and time: ", arrival_date_time)
        
        save_prompt = input("Would you like to save this new voyage, (y)es or (n)o? ")
        if save_prompt == "y":
            print("New voyage has been saved!")

            upcoming_flight1 = UpcomingVoyage(
                id=the_last_id,
                flight_nr=flight_number,
                dep_from=departure_location,
                arrival_location=arrival_location,
                arr_at=departure_date_time, 
                departure=(departure_date + " " + departure_time), 
                aircraft_id=aircraft_id
            )

            # TODO: make this one like the above one :p
            upcoming_flight2 = UpcomingVoyage((the_last_id + 1),flight_number, arrival_location, departure_location, arrival_date_time, arrival_date_time, aircraft_id, unstaffed, unstaffed, unstaffed, unstaffed, unstaffed, unstaffed, unstaffed, unstaffed)

            self.logic_wrapper.add_upcoming_voyages(upcoming_flight1)
            self.logic_wrapper.add_upcoming_voyages(upcoming_flight2)

        elif save_prompt == "n":
            print("New voyage was not saved.")
        

    def manager_staffs_voyage(self):
        """TODO: add docstring"""
        pass
        # captain = input("Enter captain's social id: ")
        # copilot = input("Enter captain's social id: ")
        # flight_service_manager = input("Enter captain's social id: ")
        # add_flight_attendant = input("Enter social id of an additional flight attendant: ")
        # flight_attendants = [add_flight_attendant]
        # while add_flight_attendant:
        #     if len(flight_attendants) < 5:
        #         add_flight_attendant = input("Enter social id of an additional flight attendant: ")
        #         flight_attendants.append(add_flight_attendant)

        # if len(flight_attendants) < 5:
        #     empty_flight_attendant_slots = 5 - len(flight_attendants)
        #     for slots in empty_flight_attendant_slots:
        #         flight_attendants.append("N/A")
                
        # flight_attendant_1 = flight_attendants[0]
        # flight_attendant_2 = flight_attendants[1]
        # flight_attendant_3 = flight_attendants[2]
        # flight_attendant_4 = flight_attendants[3]
        # flight_attendant_5 = flight_attendants[4]

    def list_voyage_options(self) -> str:
        """TODO: add docstring"""
        self.menus.display_options(LIST_VOYAGES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action

    def voyage_past_or_present_options(self) -> str:
        """TODO: add docstring"""
        self.menus.display_options(PAST_OR_PRESENT_VOYAGES)
        action = str(input("Enter your action: ").lower())
        return action

    def get_date(self) -> str:
        """TODO: add docstring"""
        date = input("Enter date; year-month-day: ")
        return date

    def get_week(self) -> str:
        """TODO: add docstring"""
        year = input("Enter year: ")
        week = input("Enter week number (1-52): ")
        return year, week

    def get_upcoming_voyage_by_date(self, date) -> str:
        """TODO: add docstring"""

        voyage_counter = 0
        print("=" * 130)
        print(VOYAGE_HEADER)
        print("=" * 130)
        for flight_values in self.logic_wrapper.upcoming_voyages().values():
            if date in flight_values.departure.strftime('%Y-%m-%d %H:%M:%S'):
                print(
                    f"{flight_values.flight_nr:^10}{flight_values.dep_from:^11}{flight_values.arr_at:^9}{flight_values.departure.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.arrival.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.captain:^17}{flight_values.copilot:^17}{flight_values.fsm:^23}",
                    end="\n",
                )
                voyage_counter += 1
                if voyage_counter == 2:
                    voyage_counter = 0
                    print("-" * 130)

    def get_upcoming_voyage_by_week(self, year, week_nr):
        """
        TODO: add docstring"""
        voyage_counter = 0
        print("=" * 130)
        print(VOYAGE_HEADER)
        print("=" * 130)
        for flight_values in self.logic_wrapper.upcoming_voyages().values():
            weeks = str(flight_values.departure.isocalendar().week)
            if year in flight_values.departure.strftime("%Y-%m-%d %H:%M:%S"):
                if weeks == week_nr:
                    print(
                        f"{flight_values.flight_nr:^10}{flight_values.dep_from:^11}{flight_values.arr_at:^9}{flight_values.departure.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.arrival.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.captain:^17}{flight_values.copilot:^17}{flight_values.fsm:^23}",
                        end="\n",
                    )
                    voyage_counter += 1
                    if voyage_counter == 2:
                        voyage_counter = 0
                        print("-" * 130)

    def get_past_voyage_by_date(self, date) -> str:
        """TODO: add docstring"""

        voyage_counter = 0
        print("=" * 130)
        print(VOYAGE_HEADER)
        print("=" * 130)
        for flight_values in self.logic_wrapper.past_voyages().values():
            if date in flight_values.departure.strftime('%Y-%m-%d %H:%M:%S'):
                print(
                    f"{flight_values.flight_nr:^10}{flight_values.dep_from:^11}{flight_values.arr_at:^9}{flight_values.departure.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.arrival.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.captain:^17}{flight_values.copilot:^17}{flight_values.fsm:^23}",
                    end="\n",
                )
                voyage_counter += 1
                if voyage_counter == 2:
                    voyage_counter = 0
                    print("-" * 130)

    def get_past_voyage_by_week(self, year, week_nr):
        """
        TODO: add docstring
        TODO: add typehints

        TODO: Do this: :)
        Args:
            year: ???
            week_nr: ??

        """
        voyage_counter = 0
        print("=" * 130)
        print(VOYAGE_HEADER)
        print("=" * 130)

        # TODO Comment this code
        for flight_values in self.logic_wrapper.past_voyages().values():
            weeks = str(flight_values.departure.isocalendar().week)
            if year in flight_values.departure.strftime("%Y-%m-%d %H:%M:%S"):
                if weeks == week_nr:
                    # TODO: this line is too long check if we can split it without affecting output, make clean :)
                    print(
                        f"{flight_values.flight_nr:^10}{flight_values.dep_from:^11}{flight_values.arr_at:^9}{flight_values.departure.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.arrival.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.captain:^17}{flight_values.copilot:^17}{flight_values.fsm:^23}"
                    )
                    voyage_counter += 1

                    # Comment this - what's happening here
                    if voyage_counter == 2:
                        voyage_counter = 0
                        print("-" * 130)

    def staff_voyage(self) -> None:
        """TODO: add docstring"""

        flight_number = input("Enter a flight number: ")
        captain = input("Enter captain's social ID: ")
        pilot = input("Enter pilot's social ID: ")
        head_flight_crew = input("Enter head flight attendant's social ID: ")
        # TODO add an option for more flight attendants

    def cancel_voyage(self):  # define
        """TODO: add docstring"""

        flight_number = input("Enter flight number: ")
        save_prompt = input(
            f"Would you like to cancel voyage {flight_number}? (y)es or (n)o"
        )
        # TODO show th ifo for the voyage

        if save_prompt == "y":
            # TODO: implement
            print("Voyage has been canceled!")

        elif save_prompt == "n":
            print("Voyage was not canceled.")
