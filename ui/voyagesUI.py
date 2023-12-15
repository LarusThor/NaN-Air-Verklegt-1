from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from datetime import datetime, date
from typing import Any, Callable
from model.upcoming_voyage_model import UpcomingVoyage
from model.employee_model import Employee
from model.upcoming_voyage_model import UNSTAFFED

VOYAGES_OPTIONS = [
    "1. Create a voyage",
    "2. List of voyages",
    "3. Staff a voyage",
    "4. Cancel a voyage",
]

NUM_FLIGHT_ATTENDANTS_PER_FLIGHT = 5
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
        """TODO: add docstring"""
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()
        self.validation = self.logic_wrapper.validation


    def voyages_options(self) -> str:
        """TODO: add docstring"""
        self.menus.display_options("Voyages:", VOYAGES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        
        return action


    def add_voyage(self) -> None:
        """TODO: add docstring."""
        destination_list = self.logic_wrapper.destination_list()
        find_last_id = list(self.logic_wrapper.upcoming_voyages().keys())

        print("New voyage: ")
        print("=" + "-=" * 20)

        flight_number = input(
            "Enter flight number: "
        )  # TODO: validate - format og lengd
        while not self.validation.validate_flight_nr(flight_number):
            print("ERROR: invalid flight number.\nMust start with NA and contain three numbers. ")
            flight_number = input("Enter flight number: ")
        departure_location = "Kef"  # NaN air always departs from Kef

        print("Choose an arrival destination")
        for index, destination in enumerate(destination_list):
            print(f"{index + 1}. {destination.destination}")

        action = int(input("Enter choice: "))
        arrival_location = destination_list[action - 1]

        departure_date = input(
            f"Enter departure date from {departure_location}: year-month-day: "
        )  # TODO: validate
        departure_time = input(
            f"Enter departure time from {departure_location}: hours:minutes:seconds"
        )  # TODO: bæta við formatti hvernig þið viljið tímann og validate

        return_flight_date = input(
            f"Enter departure date from {arrival_location.destination}: year-month-day: "
        )  # TODO: validate
        return_flight_time = input(
            f"Enter departure time from {arrival_location.destination}: hours:minutes:seconds"
        )  # TODO: validate

        # TODO: use datetime module
        # Calculate arrical time from departure time
        date_format = "%Y-%m-%d %H:%M:%S"
        departure_date_time = departure_date + " " + departure_time
        arrival_date_time = return_flight_date + " " + return_flight_time
        departure_date_time = datetime.strptime(departure_date_time, date_format)
        arrival_date_time = datetime.strptime(arrival_date_time, date_format)

        calculated_arrival_flight_time = self.logic_wrapper.flight_time(
            arrival_location, departure_date_time
        )
        calculated_return_flight_time = self.logic_wrapper.flight_time(
            arrival_location, arrival_date_time
        )

        the_last_id = find_last_id[-1]
        the_last_id = int(the_last_id)
        the_last_id += 1

        new_flight_number = int(flight_number[-2:]) + 1  # TODO commenta
        if new_flight_number >= 100:
            back_flight_number = flight_number[:-3] + str(new_flight_number)
        else:
            back_flight_number = flight_number[:-2] + str(new_flight_number)

        print("Would you like to save this new voyage: ")  # TODO laga þetta heheheh
        print("~" * 20)
        print("Flight id: ", the_last_id)
        print("Flight Number: ", flight_number)
        print("Departure Location: ", departure_location)
        print("Arrival Location: ", arrival_location.destination_id)
        print("Departure date and time: ", departure_date_time)
        print("Arrival date and time: ", arrival_date_time)

        save_prompt = input("Would you like to save this new voyage, (y)es or (n)o? ")
        if save_prompt == "y":
            # Two flights to make one voyage

            upcoming_flight1 = UpcomingVoyage(
                id=the_last_id,
                flight_nr=flight_number,
                dep_from=departure_location,
                arr_at=arrival_location.destination_id,
                departure=departure_date_time,
                arrival=calculated_arrival_flight_time,
            )

            upcoming_flight2 = UpcomingVoyage(
                id=(the_last_id + 1),
                flight_nr=back_flight_number,
                dep_from=arrival_location.destination_id,
                arr_at=departure_location,
                departure=arrival_date_time,
                arrival=calculated_return_flight_time,  #
            )

            self.logic_wrapper.add_upcoming_voyages(upcoming_flight1)
            self.logic_wrapper.add_upcoming_voyages(upcoming_flight2)
            user_input = self.menus.print_the_info("New voyage has been saved!")
            return user_input

        elif save_prompt == "n":
            user_input = self.menus.print_the_info("New voyage was not saved.")
            return user_input


    def get_voyage_flight_number(self) -> str:
        """TODO: add docstring"""
        flight_number = input("Enter flight number: ")
        while not self.validation.validate_flight_nr(flight_number):
            print("ERROR: invalid flight number.\nMust start with NA and contain three numbers. ")
            flight_number = input("Enter flight number: ")
        return flight_number


    def get_voyage_date(self) -> str:
        """TODO: add docstring"""
        date = input("Enter year date; year-month-day: ")
        return date
        

    def __get_flight_attendants(self, available_employees: dict[str, Employee]):
        available_flight_attendants = [
            employee
            for employee in available_employees.values()
            if employee.rank == "Flight Attendant"
        ]

        chosen_flight_attendants = []

        while len(chosen_flight_attendants) < NUM_FLIGHT_ATTENDANTS_PER_FLIGHT:
            choice_idx = self.__choose_element_from_list(
                available_flight_attendants,
                display_function=lambda fa: f"{fa.name}",
                prompt=f"Choose flight attendant [{len(chosen_flight_attendants) + 1}/{NUM_FLIGHT_ATTENDANTS_PER_FLIGHT}]: ",
                top_prompt="Available flight attendants",
                allow_cancel=True,
                cancel_option="Finish picking flight attendants",
            )

            if choice_idx is None:
                break

            flight_attendant = available_flight_attendants[choice_idx]
            chosen_flight_attendants.append(flight_attendant)

            del available_flight_attendants[choice_idx]

        return chosen_flight_attendants


    def __choose_element_from_list(
        self,
        element_list: list[Any],
        display_function: Callable[[Any], str],
        prompt: str,
        top_prompt: str = None,
        allow_cancel=False,
        cancel_option: str = None,
    ) -> Any:
        print()
        if top_prompt:
            print(top_prompt)

        for index, element in enumerate(element_list):
            print(f"{index + 1}. {display_function(element)}")

        if allow_cancel:
            if cancel_option is None:
                cancel_option = "Cancel"
            print(f"c. {cancel_option}")

        while True:
            choice = input(prompt).strip()

            if allow_cancel and choice == "c":
                return None

            if choice.isnumeric():
                choice_int = int(choice)
                if 1 <= choice_int <= len(element_list):
                    return choice_int - 1
            print("Invalid choice!")


    def manager_staffs_voyage(
        self, voyage_flight_number: str, voyage_date: str
    ) -> None:
        """TODO: add docstring"""
        # TODO: accept voyage_date as date object

        # get flight and return flight
        flight: UpcomingVoyage = (
            self.logic_wrapper.get_upcoming_voyage_by_flight_nr_and_date(
                voyage_flight_number, voyage_date
            )
        )
        return_flight: UpcomingVoyage = (
            self.logic_wrapper.voyage_info_for_return_flight(
                voyage_flight_number, voyage_date
            )
        )

        # get the aircraft to assign to the flights
        available_aircrafts = self.logic_wrapper.get_available_airplanes_over_period(
            flight.departure, return_flight.arrival
        )
        aircraft_idx = self.__choose_element_from_list(
            available_aircrafts,
            lambda a: f"{a.plane_insignia}, {a.plane_type_id}",
            "Choose aircraft: ",
        )
        aircraft = available_aircrafts[aircraft_idx]
        aircraft_id = aircraft.plane_insignia

        flight.aircraft_id = aircraft_id
        return_flight.aircraft_id = aircraft_id

        # we can filter this list later later
        available_employees = self.logic_wrapper.get_available_employees_over_period(
            flight.departure, return_flight.arrival
        )

        # get captain
        qualified_captains = self.logic_wrapper.get_qualified_captains_for_plane_type(
            aircraft.plane_type_id
        )

        available_captains = [
            available_employees[captain_id]
            for captain_id in qualified_captains
            if captain_id in available_employees
        ]

        captain_idx = self.__choose_element_from_list(
            available_captains,
            lambda c: f"{c.name}",
            "Choose captain: ",
            top_prompt="List of available and qualified captains.",
        )
        captain = available_captains[captain_idx]

        flight.captain = captain.social_id
        return_flight.captain = captain.social_id

        # get copilot
        qualified_copilots = self.logic_wrapper.get_qualified_copilots_for_plane_type(
            aircraft.plane_type_id
        )

        available_copilots = [
            available_employees[copilot_id]
            for copilot_id in qualified_copilots
            if copilot_id in available_employees
        ]

        copilot_idx = self.__choose_element_from_list(
            available_copilots,
            lambda c: f"{c.name}",
            "Choose copilot: ",
            top_prompt="List of available and qualified copilots.",
        )
        copilot = available_copilots[copilot_idx]

        flight.copilot = copilot.social_id
        return_flight.copilot = copilot.social_id

        # get flight service manager
        available_flight_service_managers = [
            employee
            for employee in available_employees.values()
            if employee.rank == "Flight Service Manager"
        ]
        fsm_idx = self.__choose_element_from_list(
            available_flight_service_managers,
            lambda c: f"{c.name}",
            "Choose flight service manager: ",
            top_prompt="List of available flight service managers.",
        )
        fsm = available_flight_service_managers[fsm_idx]

        flight.fsm = fsm.social_id
        return_flight.fsm = fsm.social_id

        # get flight attendants
        flight_attendants = self.__get_flight_attendants(available_employees)

        flight_attendants_social_ids = [fa.social_id for fa in flight_attendants] + [
            UNSTAFFED
        ] * (NUM_FLIGHT_ATTENDANTS_PER_FLIGHT - len(flight_attendants))

        # assign them
        (
            flight.fa1,
            flight.fa2,
            flight.fa3,
            flight.fa4,
            flight.fa5,
        ) = flight_attendants_social_ids

                    # self.logic_wrapper.add_staff_to_voyage(upcoming_voyage_staff_first_flight)
                    # self.logic_wrapper.add_staff_to_voyage(upcoming_voyage_staff_return_flight)
                    # user_input = self.menus.print_the_info("Voyage has been staffed!")
                    # return user_input
        (
            return_flight.fa1,
            return_flight.fa2,
            return_flight.fa3,
            return_flight.fa4,
            return_flight.fa5,
        ) = flight_attendants_social_ids

        # confirm changes
        print("Crew overview: ")
        print("~" * 20)
        print("Captain: ", captain.name)
        print("Copilot: ", copilot.name)
        print("Flight Service Manager: ", fsm.name)
        for flight_attendant in flight_attendants:
            print("Flight Attendant:", flight_attendant.name)

        save_prompt = input(
            f"Would you like to add this staff to flights {flight.flight_nr} and {return_flight.flight_nr}, (y)es or (n)o? "
        )
        if save_prompt == "y":
            self.logic_wrapper.add_staff_to_voyage(flight)
            self.logic_wrapper.add_staff_to_voyage(return_flight)
            user_input = self.menus.print_the_info("Voyages have been staffed!")


    def list_voyage_options(self) -> str:
        """TODO: add docstring"""
        self.menus.display_options("List voyages", LIST_VOYAGES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action


    def voyage_past_or_present_options(self) -> str:
        """TODO: add docstring"""
        self.menus.display_options("List voyages:", PAST_OR_PRESENT_VOYAGES)
        action = str(input("Enter your action: ").lower())
        return action


    def get_date(self) -> str:
        """TODO: add docstring"""
        date = input("Enter date; year-month-day: ")
        return date


    def get_week(self) -> str:
        """TODO: add docstring"""
        year = input("Enter year: ")
        while not self.validation.validate_year():
            print("ERROR: invalid year.\nYear must be a number.")
            year = input("Enter year: ")
        week = input("Enter week number (1-52): ")
        while not self.validation.validate_weeks(week):
            print("ERROR: invalid week number.\nWeek must be from 1-52.")
            week = input("Enter week: ")
        return year, week


    def get_upcoming_voyage_by_date(self, date: date) -> str:
        """TODO: add docstring"""
        title = f"Upcoming voyages on {date}:"
        result = "=" * 130 + "\n" + VOYAGE_HEADER + "\n" + "=" * 130 + "\n"
        voyage_counter = 0
        for flight_values in self.logic_wrapper.upcoming_voyages().values():
            if date in flight_values.departure.strftime("%Y-%m-%d %H:%M:%S"):
                result += f"{flight_values.flight_nr:^13}{flight_values.dep_from:^10}{flight_values.arr_at:^7}{flight_values.departure.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.arrival.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.captain:^15}{flight_values.copilot:^16}{flight_values.fsm:^24}\n"
                voyage_counter += 1
                if voyage_counter == 2:
                    voyage_counter = 0
                    result += "-" * 130 + "\n"
        
        user_input = self.menus.print_the_info(title, result)
        return user_input


    def get_upcoming_voyage_by_week(self, year: str, week_nr: str) -> None:
        """TODO: add docstring"""
        title = f"Upcoming voyages on week {week_nr}:"
        result = "=" * 130 + "\n" + VOYAGE_HEADER + "\n" + "=" * 130 + "\n"
        voyage_counter = 0

        for flight_values in self.logic_wrapper.upcoming_voyages().values():
            weeks = str(flight_values.departure.isocalendar().week)
            if year in flight_values.departure.strftime("%Y-%m-%d %H:%M:%S"):
                if weeks == week_nr:
                    result += f"{flight_values.flight_nr:^13}{flight_values.dep_from:^10}{flight_values.arr_at:^7}{flight_values.departure.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.arrival.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.captain:^15}{flight_values.copilot:^16}{flight_values.fsm:^24}\n"
                    voyage_counter += 1
                    if voyage_counter == 2:
                        voyage_counter = 0
                        result += "-" * 130 + "\n"
        
        user_input = self.menus.print_the_info(title, result)
        return user_input


    def get_past_voyage_by_date(self, date: date) -> str:
        """TODO: add docstring"""

        title = f"Past voyages on {date}:"
        result = "=" * 130 + "\n" + VOYAGE_HEADER + "\n" + "=" * 130 + "\n"
        voyage_counter = 0

        for flight_values in self.logic_wrapper.get_past_voyages().values():
            if date in flight_values.departure.strftime("%Y-%m-%d %H:%M:%S"):
                result += f"{flight_values.flight_nr:^13}{flight_values.dep_from:^10}{flight_values.arr_at:^7}{flight_values.departure.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.arrival.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.captain:^15}{flight_values.copilot:^16}{flight_values.fsm:^24}\n"
                voyage_counter += 1
                if voyage_counter == 2:
                    voyage_counter = 0
                    result += "-" * 130 + "\n"
    
        user_input = self.menus.print_the_info(title, result)
        return user_input


    def get_past_voyage_by_week(self, year: str, week_nr: str) -> None:
        """
        TODO: add docstring
        TODO: add typehints

        TODO: Do this: :)
        Args:
            year: ???
            week_nr: ??

        """
        title = f"Past voyages on week {week_nr}:"
        result = "=" * 130 + "\n" + VOYAGE_HEADER + "\n" + "=" * 130 + "\n"
        voyage_counter = 0

        # TODO Comment this code
        for flight_values in self.logic_wrapper.get_past_voyages().values():
            weeks = str(flight_values.departure.isocalendar().week)
            if year in flight_values.departure.strftime("%Y-%m-%d %H:%M:%S"):
                if weeks == week_nr:
                    # TODO: this line is too long check if we can split it without affecting output, make clean :)
                    result += f"{flight_values.flight_nr:^10}{flight_values.dep_from:^11}{flight_values.arr_at:^9}{flight_values.departure.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.arrival.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.captain:^17}{flight_values.copilot:^17}{flight_values.fsm:^23}\n"
                    voyage_counter += 1
                    # Comment this - what"s happening here
                    if voyage_counter == 2:
                        voyage_counter = 0
                        result += "-" * 130 + "\n"
        
        user_input = self.menus.print_the_info(title, result)
        return user_input

        self.menus.print_the_info(title, result)


    def cancel_voyage(self) -> None:  # define
        """Cancels a voyage in the system."""

        flight_number = input("Enter flight number: ") #validate
        save_prompt = input(
            f"Would you like to cancel voyage {flight_number}? (y)es or (n)o"
        )
        # TODO show the ifo for the voyage

        if save_prompt == "y":
            # TODO: implement
            print("Voyage has been canceled!")

        elif save_prompt == "n":
            print("Voyage was not canceled.")
