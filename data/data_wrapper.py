from data.employeeIO import EmployeeIO
from data.destinationIO import DestinationIO
from data.airplaneIO import AirplaneIO
from data.flight_attendantIO import FlightAttendantIO
from data.pilotIO import PilotIO
from data.scheduleIO import ScheduleIO
from data.voyageIO import VoyageIO

class DataWrapper:
    def __init__(self):
        self.employeeIO = EmployeeIO()
        self.destinationIO = DestinationIO()
        self.airplaneIO = AirplaneIO()

    def get_all_staff_members(self):
        return self.employeeIO.read_employee()

    def get_all_destinations(self):
        return self.destinationIO.read_destination()
    
    def add_new_employee(self, employee):
        return self.employeeIO.add_employee(employee)
    
    def get_airplanes(self):
        return self.airplaneIO.aircraft_info()
    
    def get_airplane_types(self):
        return self.airplaneIO.aircraft_types()