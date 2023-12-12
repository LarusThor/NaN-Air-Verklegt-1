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
        aircraft_id = input("Enter a valid aircraft: ")

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
                aircraft_id=aircraft_id
            )

            # TODO: make this one like the above one :p
            upcoming_flight2 = UpcomingVoyage(
                id=(the_last_id + 1),
                flight_nr=back_flight_number,
                dep_from=arrival_location,
                arr_at=departure_location,
                departure=arrival_date_time,
                arrival=calculated_return_flight_time, #
                aircraft_id=aircraft_id
            )

            self.logic_wrapper.add_upcoming_voyages(upcoming_flight1)
            self.logic_wrapper.add_upcoming_voyages(upcoming_flight2)

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

    def manager_staffs_voyage(self, voyage_flight_number, voyage_date):
        """TODO: add docstring"""
        voyage_flight_number_info = self.logic_wrapper.upcoming_voyages().values()
        for voyages_info in voyage_flight_number_info:
            voyages_info.departure = voyages_info.departure.strftime("%Y-%m-%d")
            if voyage_flight_number in voyages_info.flight_nr and voyage_date in voyages_info.departure:
                
                if voyage_date in voyages_info.departure:
                    aircraft_id = "TF-EPG" #input("Enter a valid aircraft: ")
                    captain = "2706838569" #input("Enter captain's social id: ")

                    if self.logic_wrapper.check_pilot_qualifications(aircraft_id, captain) == True:
                        captain = captain
                    copilot = "2410876598" #input("Enter copilot's social id: ")
                    if self.logic_wrapper.check_pilot_qualifications(aircraft_id, captain) == True:
                        copilot = copilot
                        
                    flight_service_manager = "1600904199"#input("Enter flight service manager's social id: ")
                    flight_attendants = []
                    add_flight_attendant = input("Enter social id of an additional flight attendant: ")
                    if add_flight_attendant == "":
                        for i in range(5):
                            flight_attendants.append("N/A")
                    else:
                        flight_attendants = [add_flight_attendant]
                    while add_flight_attendant:
                        if len(flight_attendants) < 5:
                            add_flight_attendant = input("Enter social id of an additional flight attendant: ")
                            if add_flight_attendant == "": #[2q75645]
                                unstaffed = 5 - len(flight_attendants)
                                for flight_attendant in range(unstaffed):
                                    flight_attendants.append("N/A")

                            else:
                                flight_attendants.append(add_flight_attendant)

                    print("Would you like to save this crew: ") 
                    print("~" * 20)
                    print("Captain: ", captain)
                    print("Copilot: ", copilot)
                    print("Flight Service Manager: ", flight_service_manager)
                    for flight_attendant in flight_attendants:
                        print("Flight Attendant:", flight_attendant)
                            
        
        save_prompt = input(f"Would you like to add this staff to the voyage {voyage_flight_number}, (y)es or (n)o? ")
        if save_prompt == "y":
            print("Voyage has been staffed!")

        upcoming_voyage_staff = UpcomingVoyage(
            id=voyages_info.id,
            flight_nr=voyages_info.flight_nr,
            dep_from=voyages_info.dep_from,
            arr_at=voyages_info.arr_at,
            departure=voyages_info.departure,
            arrival=voyages_info.arr_at,
            aircraft_id=voyages_info.aircraft_id,
            captain=captain,
            copilot=copilot,
            fsm=flight_service_manager,
            fa1=flight_attendants[0],
            fa2=flight_attendants[1],
            fa3=flight_attendants[2], 
            fa4=flight_attendants[3],
            fa5=flight_attendants[4]
        )

        self.logic_wrapper.add_staff_to_voyage(upcoming_voyage_staff)

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
        for flight_values in self.logic_wrapper.get_past_voyages().values():
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
        for flight_values in self.logic_wrapper.get_past_voyages().values():
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
