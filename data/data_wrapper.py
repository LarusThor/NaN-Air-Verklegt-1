from data.employeeIO import EmployeeIO
from data.destinationIO import DestinationIO
from data.airplaneIO import AirplaneIO
from data.scheduleIO import ScheduleIO
from data.voyageIO import VoyageIO
from data.past_flightsIO import pastFlightIO
from data.upcoming_flightsIO import upcomingFlightsIO

class DataWrapper:
    def __init__(self):
        self.employeeIO = EmployeeIO()
        self.destinationIO = DestinationIO()
        self.airplaneIO = AirplaneIO()
        self.past_flightIO = pastFlightIO()
        self.upcoming_flightIO = upcomingFlightsIO()

    #Employee:
    def get_all_staff_members(self) -> dict:
        return self.employeeIO.read_employee()
    
    def add_new_employee(self, employee) -> None:
        return self.employeeIO.add_employee(employee)
    
    #airplanes
    def get_airplanes(self) -> list[list]: 
        return self.airplaneIO.aircraft_info()
    
    def get_airplane_types(self) -> list:
        return self.airplaneIO.aircraft_types()
    

    #destinations
    def get_all_destinations(self) -> list:
        return self.destinationIO.read_all_destinations()
    
    def add_destinations(self, destination):
        return self.destinationIO.add_destination(destination)
    
    #past_flights
    def read_past_flights(self):
        return self.past_flightIO.read_past_flights()

    def add_past_flights(self, past_flight):
        return self.past_flightIO.add_past_flight(past_flight)
    
    #upcoming_flights
    def get_upcoming_flights(self):
        return self.upcoming_flightIO.read_upcoming_flights()
    
    def add_upcoming_flights(self, upcoming_flight):
        return self.upcoming_flightIO.add_upcoming_flight(upcoming_flight)
