from ui.menu_managerUI import Menu
from logic.LogicWrapper import LogicWrapper
from datetime import datetime

VOYAGES_OPTIONS = ["1. Create a voyage", "2. List of voyages", "3. Staff a voyage", "4. cancel a voyage"]
LIST_VOYAGES_OPTIONS = ["1. List of voyages by day", "2. List of voyages by week"]
VOYAGE_HEADER = ("{:^10}{:^10}{:^6}{:^22}{:^22}{:^15}{:^17}{:^27}".format('Flight Number', 'From', 'To', 'Departure Time', 'Arrival Time', 'Captain', 'Copilot', 'Flight Service Manager'))



class VoyagesUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()
        self.get_voyages = self.logic_wrapper.upcoming_voyages()

    def voyages_options(self) -> str:
        self.menus.display_options(VOYAGES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    
    def add_voyage(self) -> None:
        print("New voyage: ")
        destination = input("Destination: ")
        airplane_type = input("Airplane type: ")
        departure_date = input("Enter departure date; day/month/year: ")
        departure_time = input("Enter departure time: ")
        return_flight_date = input("Enter return flight date; day/month/year: ")
        return_flight_time = input("Enter return flight time: ")
        print("New voyage:")
        print("Destination:", destination)
        print("Airplane type:", airplane_type)
        print("Departure date:", departure_date)
        print("Departure time:", departure_time)
        print("Return flight date:", return_flight_date)
        print("Return flight time:", return_flight_time)
        save_prompt = "Would you like to save this new voyage, (y)es or (n)o? "
        if save_prompt == "y":
            print("New voyage has been saved!")
        elif save_prompt == "n":
            print("New voyage was not saved.")

    def list_voyage_options(self) -> str:
        self.menus.display_options(LIST_VOYAGES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
        
    def get_date(self) -> str:
        date = input("Enter date; year-month-day: ")
        return date
    
    def get_week(self) -> str:
        week = input("Enter week number (1-52): ")
        return week
    
    def get_voyage_by_date(self, date) -> str: 
        voyage_counter = 0
        print("=" * 130)
        print(VOYAGE_HEADER)
        print("=" * 130)
        for id, flight_values in self.get_voyages.items():
            if date in flight_values.departure:
                print(f"{flight_values.flight_nr:^10}{flight_values.dep_from:^11}{flight_values.arr_at:^9}{flight_values.departure:^22}{flight_values.arrival:^22}{flight_values.captain:^17}{flight_values.copilot:^17}{flight_values.fsm:^23}", end="\n")
                voyage_counter += 1
                if voyage_counter == 2:
                    voyage_counter = 0
                    print("-" * 130)
    
    def get_voyage_by_week(self, week_nr):
        voyage_counter = 0
        date = ""
        print("=" * 130)
        print(VOYAGE_HEADER)
        print("=" * 130)
        for id, flight_values in self.logic_wrapper.upcoming_voyages().items():
            # print(type(flight_values.departure))
            # print(flight_values.departure)
            # departure_date = datetime.strptime(flight_values.departure, "%Y-%m-%d %H:%M:%S")
            # date = departure_date[0].split("-")
            # year, month, day = map(int, date)
            if flight_values.departure.isocalendar().week == week_nr:
                 print(f"{flight_values.flight_nr:^10}{flight_values.dep_from:^11}{flight_values.arr_at:^9}{flight_values.departure:^22}{flight_values.arrival:^22}{flight_values.captain:^17}{flight_values.copilot:^17}{flight_values.fsm:^23}", end="\n")
                 voyage_counter += 1
                 if voyage_counter == 2:
                     voyage_counter = 0
                     print("-" * 130)


    def staff_voyage(self) -> None:
        flight_number = input("Enter a flight number: ")
        captain = input("Enter captain's social ID: ")
        pilot = input("Enter pilot's social ID: ")
        head_flight_crew = input("Enter head flight attendant's social ID: ")
        #TODO add an option for more flight attendants

    def cancel_voyage(self): #define
        flight_number = input("Enter flight number: ")
        save_prompt = input(f"Would you like to cancel voyage {flight_number}? (y)es or (n)o")
        #TODO show th ifo for the voyage

        if save_prompt == "y":
            print("Voyage has been canceled!")
            
        elif save_prompt == "n":
            print("Voyage was not canceled.")