from data.data_wrapper import DataWrapper
#from airplaneLL import AirplaneLL
#from destinationLL import DestinationLL
from logic.employeeLL import EmployeeLL
#from flightattendantLL import FlightAttendant
#from pilotLL import PilotLL
#from scheduleLL import ScheduleLL
#from voyageLL import VoyageLL
#from validationLL import ValidationLL

class LogicWrapper():
    def __init__(self) -> None:
        self.DataWrapper = DataWrapper()
        self.employee = EmployeeLL() 
    
    def employee_list(self):
        return self.employee.get_employee_list()
    
    def pilot_list(self):
        return self.employee.get_all_pilots()
    
    def flight_attendant_list(self):
        return self.employee.get_flight_attendants()