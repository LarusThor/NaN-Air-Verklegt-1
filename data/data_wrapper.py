from data.employeeIO import EmployeeIO
from data.destinationIO import DestinationIO
from data.airplaneIO import AirplaneIO


class DataWrapper:
    def __init__(self):
        self.employeeIO = EmployeeIO()
        self.destinationIO = DestinationIO()
        self.airplaneIO = AirplaneIO

    def get_all_staff_members(self):
        return self.employeeIO.read_employee()

    def get_all_destinations(self):
        return self.destinationIO.read_destination()
    
    def get_airplanes(self):
        return self.airplaneIO.read_airplane()