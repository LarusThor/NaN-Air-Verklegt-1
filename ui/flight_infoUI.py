from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper

FLIGHT_INFORMATION_OPTIONS = ["1. Booking status for specific voyage", "2. Booking status for a specific date"]

class FlightInfoUI:
    def __init__(self) -> None:
        """ TODO: add docstring """
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()
        self.flight_booking = self.logic_wrapper.flight_fully_booked()


    def flight_info_options(self) -> str:
        """ TODO: add docstring """
        self.menus.display_options("Flight information:", FLIGHT_INFORMATION_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    

    def get_voyage(self) -> str:
        """ TODO: add docstring """
        flight_number = input("Enter flight number: ")
        return flight_number
         

    def get_flight_status_by_voyage(self): #define
        """ Returns a list of upcoming voyages and their booking status. """
        flights = self.logic_wrapper.flight_fully_booked()

        print("Flight status: \n")
        for flight, status in flights:
            if status == "Booked":
                print(f"{flight.departure.date()} - {flight.flight_nr} to {flight.arr_at} = {status}")
            else:
                print(f"{flight.departure.date()} - {flight.flight_nr} to {flight.arr_at} = {status} seats left.")
