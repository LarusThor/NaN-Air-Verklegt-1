from data.employeeIO import EmployeeIO
from data.destinationIO import DestinationIO
from data.airplaneIO import AirplaneIO
from data.scheduleIO import ScheduleIO
from data.voyageIO import VoyageIO

class DataWrapper:
    def __init__(self):
        self.employeeIO = EmployeeIO()
        self.destinationIO = DestinationIO()
        self.airplaneIO = AirplaneIO()

    #Employee:
    def get_all_staff_members(self):
        return self.employeeIO.read_employee()
    
    def create_new_staff_member(self):
        return self.employeeIO.add_employee()

    #Destinations:
    def get_all_destinations(self):
        return self.destinationIO.read_destination()
    
    #Airplanes:
    def get_airplanes(self):
        return self.airplaneIO.aircraft_info()
    
    def get_airplane_types(self):
        return self.airplaneIO.aircraft_types()
    

    #destinations
    def add_destinations(self, destination):
        return self.destinationIO.add_destination(destination)