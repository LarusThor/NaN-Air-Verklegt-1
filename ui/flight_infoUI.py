from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper

FLIGHT_INFORMATION_OPTIONS = ["1. Booking status for specific voyage", "2. Booking status for a specific date"]

class FlightInfoUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()
        self.flight_booking = self.logic_wrapper.flight_fully_booked()

    def flight_info_options(self) -> str:
        """ TODO: add docstring """
        self.menus.display_options(FLIGHT_INFORMATION_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    

    def get_voyage(self) -> str:
        """ TODO: add docstring """
        flight_number = input("Enter flight number: ")
        return flight_number
         

    def get_date(self) -> str:
        """ TODO: add docstring """
        date = input("Enter date; day/month/year: ") 
        return date 
         

    def get_flight_status_by_voyage(self, voyage): #define
        """ TODO: add docstring """
        status = self.flight_booking.get(voyage)
        while status == None:
            print("There is no flight number", voyage)
            voyage = input("Enter flight number: ")
            status = self.flight_booking.get(voyage)

        print()
        print("-"*30)
        try:
            int(status)
            print(voyage, f"has {status} seats left.")
        except:
            print(voyage, "is fully booked.")

        print("-"*30)
        print()
        print("(H)ome  (B)ack")
        action = input("Enter in your action: ")
        return action
        


    def get_flight_status_by_date(self, date): #define
        """ TODO: add docstring """
        pass
         
         