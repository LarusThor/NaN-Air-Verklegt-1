from data.data_wrapper import DataWrapper
from logic.airplaneLL import AirplaneLL
from logic.destinationLL import DestinationLL
from logic.employeeLL import EmployeeLL
from logic.scheduleLL import ScheduleLL
from logic.voyageLL import VoyageLL
from logic.upcoming_voyageLL import UpcomingVoyageLL
from logic.past_voyageLL import PastVoyageLL
#from logic.validationLL import ValidationLL

class LogicWrapper():
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        self.employee = EmployeeLL() 
        self.airplane = AirplaneLL()
        self.destination = DestinationLL()
        self.schedule = ScheduleLL(self)
        self.voyage = VoyageLL()
        self.list_upcoming_voyage = UpcomingVoyageLL()
        self.list_past_voyages = PastVoyageLL()


    #Employee:
    def employee_list(self):
        """ Returns a list of all employees. """
        return self.employee.get_employee_dict()
    
    def pilot_list(self):
        """ Returns a list of all pilots within the system. """
        return self.employee.get_all_pilots()
    
    def flight_attendant_list(self):
        """ Returns a list of all flight attendats within the system. """
        return self.employee.get_flight_attendants()

    def add_employee(self, employee):
         """ Adds employee to the system. """
         return self.employee.add_employee(employee)
    
    def employee_info(self, employee_social_id: str):
        """ Returns information about a specific employee. 
        
        Args:
            employee_social_id: The social ID of the employee
        """
        return self.employee.get_employee(employee_social_id)
    
    def change_employee_info(self, employee):
        """ doc """
        return self.employee.change_employee_info(employee)
    
    def total_hours_worked(self, employee):
        """ doc """
        return self.employee.get_total_hours_worked(employee)


    #Destinations:
    def destination_list(self):
        """ Returns a list of all destinations within the system. """
        return self.destination.get_destination_list()
    
    def add_destination(self, destination):
        """Takes in a customer object and forwards it to the data layer. """
        return self.destination.add_destination(destination)
    
    def add_destination(self, destination):
        """ Takes in a customer object and forwards it to the data layer. """
        return self.destination.add_destination(destination)

    #Airplanes:
    def airplane_types(self):
        """ Returns all airplane types within the system. """
        return self.airplane.get_all_airplane_types()
    
    def add_airplane(self, airplane):
        return self.airplane.add_airplane(airplane)
    
    def pilots_by_license(self):
        return self.airplane.pilots_by_license()

    def airplane_insignia_by_types(self):
        return self.airplane.airplane_insignia_by_type()

    #Upcoming voyages:
    def upcoming_voyages(self):
        """ doc. """
        return self.list_upcoming_voyage.get_upcoming_voyages()
    
    def add_upcoming_voyages(self, upcoming_voyage):
        return self.list_upcoming_voyage.add_upcoming_voyage(upcoming_voyage)


    #Past voyages:

    def past_voyages(self):
        """ doc """
        return self.list_past_voyages.get_past_voyages()
    

    #schedule

    def employee_schedule_by_week(self, employee:str, year:str, week:str):
        """ Returns an employees schedule on a specific week. """
        return self.schedule.employee_schedule_by_week(employee, year, week)
 
    def employee_working(self, date):
        """ doc """
        return self.schedule.employee_working(date)

    def employee_not_working(self, date):
        """ doc """
        return self.schedule.employee_not_working(date)
