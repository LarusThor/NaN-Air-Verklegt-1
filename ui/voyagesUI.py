from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from datetime import datetime, date
from model.upcoming_voyage_model import UpcomingVoyage

VOYAGES_OPTIONS = [
    "1. Create a voyage",
    "2. List of voyages",
    "3. Staff a voyage",
    "4. Cancel a voyage",
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
        """ TODO: add docstring """
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()


    def voyages_options(self) -> str:
        """ TODO: add docstring """
        self.menus.display_options("Voyages:", VOYAGES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action


    def add_voyage(self) -> None:
        """ TODO: add docstring. """

        find_last_id = list(self.logic_wrapper.upcoming_voyages().keys())

        print("New voyage: ")
        print("=" + "-=" * 20)
        flight_number = input("Enter flight number: ")
        departure_location = input("Enter 3 letter keyword for departure location: ")
        arrival_location = input("Enter 3 letter keyword for arrival location: ")
        departure_date = input(f"Enter departure date from {departure_location}; year-month-day: ")
        departure_time = input(f"Enter departure time from {departure_location}: ")
        # arrival_time = input(f"Enter arrival time for {arrival_location}: ")
        return_flight_date = input(f"Enter departure date from {arrival_location}; year-month-day: ")
        return_flight_time = input(f"Enter departure time from {arrival_location}: ")

        # TODO: use datetime module
        departure_date_time = departure_date + " " + departure_time
        arrival_date_time = return_flight_date + " " + return_flight_time

        # arrival_time = calculate_flight_time(departure_date_time)
        # retrun_flight_arrival = calculate_flight_time(arrival_date_time)
        

        the_last_id = find_last_id[-1]
        the_last_id = int(the_last_id)
        the_last_id += 1
        
        new_flight_number = int(flight_number[-2:]) + 1 #TODO commenta
        if new_flight_number >= 100:
            back_flight_number = flight_number[:-3] + str(new_flight_number)
        else:
            back_flight_number = flight_number[:-2] + str(new_flight_number)

        calculated_arrival_flight_time = self.logic_wrapper.flight_time(arrival_location, departure_date_time)
        calculated_return_flight_time = self.logic_wrapper.flight_time(arrival_location, arrival_date_time )

        print("Would you like to save this new voyage: ") #TODO laga þetta heheheh
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
                arr_at=arrival_location,
                departure=departure_date_time, 
                arrival=calculated_arrival_flight_time, 
            )

            # TODO: make this one like the above one :p
            upcoming_flight2 = UpcomingVoyage(
                id=(the_last_id + 1),
                flight_nr=back_flight_number,
                dep_from=arrival_location,
                arr_at=departure_location,
                departure=arrival_date_time,
                arrival=calculated_return_flight_time, #
            )

            self.logic_wrapper.add_upcoming_voyages(upcoming_flight1)
            self.logic_wrapper.add_upcoming_voyages(upcoming_flight2)
            print("saving_files")

        elif save_prompt == "n":
            print("New voyage was not saved.")
        
    def get_voyage_flight_number(self) -> str:
        """TODO: add docstring"""
        flight_number = input("Enter flight number: ")
        return flight_number

    def get_voyage_date(self) -> str:
        """TODO: add docstring"""
        date = input("Enter year date; year-month-day: ")
        return date

    def manager_staffs_voyage(self, voyage_flight_number: str, voyage_date: str) -> None:
        """TODO: add docstring"""
        # TODO: accept voyage_date as date object
        aircraft_check = False
        captain_check = False
        copilot_check = False
        flight_service_manager_check = False
        flight_attendant_check = False

        return_flight_id, return_flight_number, return_flight_dep_from, return_flight_arr_at, return_flight_date_departure, return_flight_arrival = self.logic_wrapper.voyage_info_for_return_flight(voyage_flight_number, voyage_date)
        voyage_flight_number_info = self.logic_wrapper.upcoming_voyages().values()
        employee_information = self.logic_wrapper.show_employee_info()
        for voyages_info in voyage_flight_number_info:
            # TODO: just get this as a variable, dont reassign the attribute
            departure_date = voyages_info.departure.strftime("%Y-%m-%d")
            if voyage_flight_number == voyages_info.flight_nr and voyage_date == departure_date:
                while not aircraft_check:
                    aircraft_id = input("Enter a valid aircraft: ")
                    if self.logic_wrapper.get_total_future_hours_for_airplane(aircraft_id, voyages_info.departure, return_flight_arrival) == 0:
                        aircraft_check = True
                    else:
                        print(f"Airplane {aircraft_id} not available on between {voyages_info.departure} and {return_flight_arrival}")
                        aircraft_check = False

                while not captain_check:
                    captain = input("Enter captain social id: ")
                    if employee_information[captain].rank == "Captain":
                        if self.logic_wrapper.check_pilot_qualifications(aircraft_id, captain):
                            if self.logic_wrapper.staff_availability_check(captain, voyages_info.departure, return_flight_arrival) == 0:
                                captain_check = True
                            else:
                                print(f"Captain {captain} not available on between {voyages_info.departure} and {return_flight_arrival}")
                                captain_check = False
                        else:
                            print(f"Captain {captain} does not have the license to fligh {aircraft_id}")
                            captain = False
                    else:
                        print(f"{captain} is not a captain")
                        
                    
                    # flights_list, total_hours_worked = self.logic_wrapper.get_total_future_hours_worked(captain, voyages_info.departure, return_flight_arrival)
                    # if total_hours_worked != 0:
                    #     print("NEi")
                while not copilot_check:
                    copilot = input("Enter copilot's social id: ")
                    if employee_information[copilot].rank == "Copilot":
                        if self.logic_wrapper.check_pilot_qualifications(aircraft_id, copilot):
                            if self.logic_wrapper.staff_availability_check(copilot, voyages_info.departure, return_flight_arrival) == 0:
                                copilot_check = True
                            else:
                                print(f"Copilot {copilot} not available on between {voyages_info.departure} and {return_flight_arrival}")
                                copilot_check = False
                        else:
                            print(f"Copilot {copilot} does not have the license to fligh {aircraft_id}")
                            copilot_check = False
                    else:
                        print(f"{copilot} is not a copilot")
                        
                while not flight_service_manager_check:               
                    flight_service_manager = input("Enter Flight service manager's social id: ")
                    if employee_information[flight_service_manager].rank == "Flight Service Manager":
                            if self.logic_wrapper.staff_availability_check(flight_service_manager, voyages_info.departure, return_flight_arrival) == 0:
                                flight_service_manager_check = True
                            else:
                                print(f"Flight service manager {flight_service_manager} not available on between {voyages_info.departure} and {return_flight_arrival}")
                                flight_service_manager_check = False
                    else:
                        print(f"{flight_service_manager} is not a Flight service manager")  

                flight_attendants = []
                
                while not flight_attendant_check:
                    add_flight_attendant = input("Enter social id of an additional flight attendant: ")
                    
                    
                    if add_flight_attendant == "":
                        for i in range(5):
                            flight_attendants.append("N/A")
                    
                    else:
                            if employee_information[add_flight_attendant].rank == "Flight Attendant":
                                if self.logic_wrapper.staff_availability_check(add_flight_attendant, voyages_info.departure, return_flight_arrival) == 0:
                                    flight_attendants = [add_flight_attendant]
                                    flight_attendant_check = True
                                else:
                                    print(f"Flight Attendant {flight_service_manager} not available on between {voyages_info.departure} and {return_flight_arrival}")
                                    flight_attendant_check = False

                            else:
                                print(f"{add_flight_attendant} is not a Flight Attendant")
                                flight_attendant_check = False
    

                while add_flight_attendant:
                    if len(flight_attendants) == 5:
                        add_flight_attendant = ""
                    flight_attendant_check = False
                    if len(flight_attendants) < 5:
                        while not flight_attendant_check:
                            add_flight_attendant = input("Enter social id of an additional flight attendant: ")
                            if add_flight_attendant == "": 
                                unstaffed = 5 - len(flight_attendants)
                                for flight_attendant in range(unstaffed):
                                    flight_attendants.append("N/A")
                                    flight_attendant_check = True

                            else:
                                if employee_information[add_flight_attendant].rank == "Flight Attendant":
                                    if self.logic_wrapper.staff_availability_check(add_flight_attendant, voyages_info.departure, return_flight_arrival) == 0:
                                        flight_attendants.append(add_flight_attendant)
                                        flight_attendant_check = True

                                    else:
                                        print(f"Flight Attendant {flight_service_manager} not available on between {voyages_info.departure} and {return_flight_arrival}")
                                        flight_attendant_check = False

                                else:
                                    print(f"{add_flight_attendant} is not a Flight Attendant")
                                    flight_attendant_check = False

                assert len(flight_attendants) == 5

                print("Would you like to save this crew: ") 
                print("~" * 20)
                print("Captain: ", captain)
                print("Copilot: ", copilot)
                print("Flight Service Manager: ", flight_service_manager)
                for flight_attendant in flight_attendants:
                    print("Flight Attendant:", flight_attendant)
                        
                # return_flight_id, return_flight_number, return_flight_dep_from, return_flight_arr_at, return_flight_date_departure, return_flight_arrival = self.logic_wrapper.voyage_info_for_return_flight(voyage_flight_number, voyage_date)


                save_prompt = input(f"Would you like to add this staff to the voyage {voyage_flight_number}, (y)es or (n)o? ")
                if save_prompt == "y":

                    upcoming_voyage_staff_first_flight = UpcomingVoyage(
                        id=voyages_info.id,
                        flight_nr=voyages_info.flight_nr,
                        dep_from=voyages_info.dep_from,
                        arr_at=voyages_info.arr_at,
                        departure=voyages_info.departure,
                        arrival=voyages_info.arrival,
                        aircraft_id=aircraft_id,
                        captain=captain,
                        copilot=copilot,
                        fsm=flight_service_manager,
                        fa1=flight_attendants[0],
                        fa2=flight_attendants[1],
                        fa3=flight_attendants[2], 
                        fa4=flight_attendants[3],
                        fa5=flight_attendants[4]
                    )
                    

                    #TODO: Change return flight staff aswell
                    upcoming_voyage_staff_return_flight = UpcomingVoyage(

                        id=return_flight_id,
                        flight_nr=return_flight_number,
                        dep_from=return_flight_dep_from,
                        arr_at=return_flight_arr_at,
                        departure=return_flight_date_departure,
                        arrival=return_flight_arrival,
                        aircraft_id=aircraft_id,
                        captain=captain,
                        copilot=copilot,
                        fsm=flight_service_manager,
                        fa1=flight_attendants[0],
                        fa2=flight_attendants[1],
                        fa3=flight_attendants[2], 
                        fa4=flight_attendants[3],
                        fa5=flight_attendants[4]
                    )

                    self.logic_wrapper.add_staff_to_voyage(upcoming_voyage_staff_first_flight)
                    self.logic_wrapper.add_staff_to_voyage(upcoming_voyage_staff_return_flight)
                    print("Voyage has been staffed!")

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
        week = input("Enter week number (1-52): ")
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
        
        self.menus.print_the_info(title, result)

    def get_upcoming_voyage_by_week(self, year: str, week_nr: str) -> None:
        """TODO: add docstring"""
        title = f"Upcoming voyages on week {week_nr}:"
        result = "=" * 130 + "\n" + VOYAGE_HEADER + "\n" + "=" * 130 + "\n"
        voyage_counter = 0

        for flight_values in self.logic_wrapper.upcoming_voyages().values():
            weeks = str(flight_values.departure.isocalendar().week)
            if year in flight_values.departure.strftime('%Y-%m-%d %H:%M:%S'):
                if weeks == week_nr:
                    result += f"{flight_values.flight_nr:^13}{flight_values.dep_from:^10}{flight_values.arr_at:^7}{flight_values.departure.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.arrival.strftime('%Y-%m-%d %H:%M:%S'):^22}{flight_values.captain:^15}{flight_values.copilot:^16}{flight_values.fsm:^24}\n"
                    voyage_counter += 1
                    if voyage_counter == 2:
                        voyage_counter = 0
                        result += "-" * 130 + "\n"
        
        self.menus.print_the_info(title, result)


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
    
        self.menus.print_the_info(title, result)


    def get_past_voyage_by_week(self, year:str,  week_nr:str) -> None:
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
        
        self.menus.print_the_info(title, result)

    def staff_voyage(self) -> None:
        """Adds staff to voyage in the system."""

        flight_number = input("Enter a flight number: ")
        captain = input("Enter captain's social ID: ")
        pilot = input("Enter pilot's social ID: ")
        head_flight_crew = input("Enter head flight attendant's social ID: ")
        # TODO add an option for more flight attendants

    def cancel_voyage(self) -> None:  # define
        """Cancels a voyage in teh system."""

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
            print("Voyage was not canceled.")
