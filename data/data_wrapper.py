from data.employeeIO import EmployeeIO
from data.destinationIO import DestinationIO
from data.airplaneIO import AirplaneIO
from data.past_voyageIO import PastVoyageIO
from data.upcoming_voyageIO import UpcomingVoyageIO
from model.destination_model import Destination
from model.past_voyage_model import PastVoyage
from model.upcoming_voyage_model import UpcomingVoyage
from model.airplane_type_model import AirplaneType

class DataWrapper:
    def __init__(self):
        self.employeeIO = EmployeeIO()
        self.destinationIO = DestinationIO()
        self.airplaneIO = AirplaneIO()
        self.past_flightIO = PastVoyageIO()
        self.upcoming_flightIO = UpcomingVoyageIO()
        self.destination = DestinationIO()

    #Employee:
    def get_all_staff_members(self) -> dict:
        """ Returns a dictionary for every employee. 
        key: employee social ID
        values: employee info
        """
        return self.employeeIO.read_employee()
    

    def write_employees(self, employees) -> None:
        """ Both adds a new employee to the system, and allows to change employees information. """
        return self.employeeIO.write_employees(employees)
    
    #airplanes
    def get_airplanes(self) -> dict:
        """ Reads a csv file about the aircrafts and returns an aircraft dictionary. """
        return self.airplaneIO.aircraft_info()
    
    def get_airplane_types(self) -> list[AirplaneType]:
        """ Reads a csv file about airplane types and returns a list of airplane type models. """
        return self.airplaneIO.airplane_types()
    

    #destinations
    def get_all_destinations_info(self) -> dict:
        """ Returns a dictionary of all destinations. """
        return self.destinationIO.read_destinations_info()

    def get_all_destinations(self) -> list: 
        """ TODO: add doc. """
        return self.destinationIO.read_all_destinations()
    
    def add_destinations(self, destination) -> None:
        """"""
        return self.destinationIO.add_destination(destination)
   
    def change_destination_info(self, destination: Destination) -> None:
        return self.destinationIO.update_destination(destination)

    def destination_info(self) -> list:
        return self.destination.read_all_destinations()

    #past_flights
    def get_past_flights(self)-> dict[str, PastVoyage]:
        return self.past_flightIO.read_past_flights()

    def add_past_flights(self, past_flight) -> None:
        return self.past_flightIO.add_past_voyage(past_flight)
    
    #upcoming_flights
    def get_upcoming_flights(self) -> dict[str, UpcomingVoyage]:
        return self.upcoming_flightIO.read_upcoming_flights()
    
    def add_upcoming_flights(self, upcoming_flight) -> None:
        return self.upcoming_flightIO.add_upcoming_voyage(upcoming_flight)
    
    def add_airplane(self, airplane) -> None:
        return self.airplaneIO.add_aircraft(airplane)