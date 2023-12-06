from ui.main_menuUI import Menu
from logic.LogicWrapper import LogicWrapper

FLIGHT_INFORMATION_OPTIONS = ["1. Booking status for specific voyage", "2. Booking status for a specific date"]

class FlightInfoUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()

    def flight_info_options(self):
        self.menus.display_options(FLIGHT_INFORMATION_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    
    def get_voyage(self):
        flight_number = input("Enter flight number: ")
        return flight_number
         

    def get_date(self):
        date = input("Enter date; day/month/year: ") 
        return date 
         
    def get_flight_status_by_voyage(self, voyage):
        pass

    def get_flight_status_by_date(self, date):
        pass
         
         