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
         

    def get_flight_status(self): #define
        """ Returns a list of upcoming voyages and their booking status. """
        flights = self.logic_wrapper.flight_fully_booked()

        title = "Flight status: \n{} \n{:<16} {:<15} {:<20} {:<15}".format("-"*70, "Departure date", "Flight number", "Flight destination", "Flight status")
        result = ""
        for flight, status in flights:
            if status == "Booked":
                result += "{:^16} {:^15} {:^20} {:^15}\n".format(flight.departure.date, flight.flight_nr, flight.arr_at, status)
            else:
                result += "{:^16} {:^15} {:^20} {:^15}seats left.\n".format(flight.departure.date, flight.flight_nr, flight.arr_at, status)

        self.menus.print_the_info(title, result)