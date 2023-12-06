from data.data_wrapper import DataWrapper
from logic.airplaneLL import AirplaneLL
from logic.destinationLL import DestinationLL
from logic.employeeLL import EmployeeLL
#from logic.flightattendantLL import FlightAttendant
#from logic.pilotLL import PilotLL
from logic.scheduleLL import ScheduleLL
from logic.voyageLL import VoyageLL
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
    def employee_list(self):
        return self.employee.get_employee_list()
    
    def pilot_list(self):
        return self.employee.get_all_pilots()
    
    def flight_attendant_list(self):
        return self.employee.get_flight_attendants()

    def add_employee(self, employee):
         return self.employee.add_employee(employee)
    
    #Destinations:
    def destination_list(self):
        return self.destination.get_destination_list()
    
    #Airplanes:
    def airplane_types(self):
        return self.airplane.get_all_airplane_types()