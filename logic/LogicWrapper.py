from data.data_wrapper import DataWrapper
from logic.airplaneLL import AirplaneLL
from logic.destinationLL import DestinationLL
from logic.employeeLL import EmployeeLL
from logic.scheduleLL import ScheduleLL
from logic.voyageLL import VoyageLL
from model.employee_model import Employee
from model.destination_model import Destination
#from logic.validationLL import ValidationLL

class LogicWrapper():
    def __init__(self) -> None:
        self.DataWrapper = DataWrapper()
        self.employee = EmployeeLL() 
        self.airplane = AirplaneLL()
        self.destination = DestinationLL()
        self.schedule = ScheduleLL()
        self.voyage = VoyageLL()
    
    #Employee:
    def employee_list(self) -> list[str]:
        """ Returns a list of all employees. """
        return self.employee.get_employee_list()
    
    def pilot_list(self) -> list[str]:
        """ Returns a list of all pilots within the system. """
        return self.employee.get_all_pilots()
    
    def flight_attendant_list(self) -> list[str]:
        """ Returns a list of all flight attendats within the system. """
        return self.employee.get_flight_attendants()

    def add_employee(self, employee: Employee) -> None:
         """ Adds employee to the system. """
         return self.employee.add_employee(employee)
    
    def employee_info(self, employee: Employee) -> Employee:
        """ Returns information about a specific employee. """
        return self.employee.get_employee(employee)
    
    #Destinations:
    def destination_list(self) -> list:
        """ Returns a list of all destinations within the system. """
        return self.destination.get_destination_list()
    
    def add_destination(self, destination: Destination) -> None:
        """Takes in a customer object and forwards it to the data layer"""
        return self.destination.add_destination(destination)
    
    def add_destination(self, destination: Destination) -> None:
        """Takes in a customer object and forwards it to the data layer"""
        return self.destination.add_destination(destination)
    
    #Airplanes:
    def airplane_types(self) -> list:
        """ Returns all airplane types within the system. """
        return self.airplane.get_all_airplane_types()
    