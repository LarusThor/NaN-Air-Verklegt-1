from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper

FLIGHT_STATUS_OPTIONS = ["1. Booking status for specific voyage", "2. Booking status for a specific date"]

class FlightInfoUI:
    def __init__(self) -> None:
        """"Instantiate a ArplaneUI object."""
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()         


    def get_flight_status(self) -> None: #define
        """ Gets information about the upcoming voyages from the logic wrapper. Makes a title and the results 
        (which is the information that will be printed out). Calls the function in the menu_manager that takes care of 
        prints out the title and the information.
        """
        flights = self.logic_wrapper.flight_fully_booked()
        
        title = f"Flight status: \n{'='*70}\n{'Departure date':<16} {'Flight number':<15} {'Flight destination':<20} {'Flight status':<15}"
        result = ""

        for flight, status in flights:
            date = str(flight.departure.date())
            if status == "Booked":
                booked = "Fully booked!"
                result += f"{date:^15} {flight.flight_nr:^15} {flight.arr_at:^21} {booked}\n"
            else:
                result += f"{date:^15} {flight.flight_nr:^15} {flight.arr_at:^21} {status:<3} seats left\n"

        user_input = self.menus.print_the_info(title, result) #TODO validate, can just be b or q
        return user_input
