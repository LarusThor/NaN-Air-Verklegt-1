from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper

FLIGHT_STATUS_OPTIONS = ["1. Booking status for specific voyage", "2. Booking status for a specific date"]

class FlightInfoUI:
    def __init__(self) -> None:
        """ TODO: add docstring """
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()
        self.flight_booking = self.logic_wrapper.flight_fully_booked()


    def flight_info_options(self) -> str:
        """ TODO: add docstring """
        self.menus.display_options("Flight information:", FLIGHT_STATUS_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    

    def get_voyage(self) -> str:
        """ TODO: add docstring """
        flight_number = input("Enter flight number: ")
        return flight_number
         

    def get_flight_status(self) -> None: #define
        """ Returns a list of upcoming voyages and their booking status. """
        flights = self.logic_wrapper.flight_fully_booked()
        title = f"Flight status: \n{'-'*70}\n{'Departure date':<16} {'Flight number':<15} {'Flight destination':<20} {'Flight status':<15}"
        result = ""
        for flight, status in flights:
            date =str(flight.departure.date())
            print(type(date))
            if status == "Booked":
                result += f"{date:^16} {flight.flight_nr:^15} {flight.arr_at:^20} {status:^15}\n"
                
            else:
                result += f"{date:^16} {flight.flight_nr:^15} {flight.arr_at:^20} {status:^15} seats left.\n"


        self.menus.print_the_info(title, result)