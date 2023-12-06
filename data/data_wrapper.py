from data.employeeIO import EmployeeIO
from data.destinationIO import DestinationIO
from data.airplaneIO import AirplaneIO
from data.scheduleIO import ScheduleIO
from data.voyageIO import VoyageIO
from model.employee_model import Employee
from model.destination_model import Destination

class DataWrapper:
    def __init__(self):
        self.employeeIO = EmployeeIO()
        self.destinationIO = DestinationIO()
        self.airplaneIO = AirplaneIO()

    #Employee:
    def get_all_staff_members(self) -> dict:
        return self.employeeIO.read_employee()
    
    def add_new_employee(self, employee: Employee) -> None:
        return self.employeeIO.add_employee(employee)
    
    #airplanes
    def get_airplanes(self) -> list[list]: 
        return self.airplaneIO.aircraft_info()
    
    def get_airplane_types(self) -> list:
        return self.airplaneIO.aircraft_types()
    

    #destinations
    def get_all_destinations(self) -> list:
        return self.destinationIO.read_all_destinations()
    
    def add_destinations(self, destination: Destination) -> None: #TODO: check if Destination er rétt 
        return self.destinationIO.add_destination(destination)