from data.data_wrapper import DataWrapper
from logic.airplaneLL import AirplaneLL
from logic.destinationLL import DestinationLL
from logic.employeeLL import EmployeeLL
from logic.scheduleLL import ScheduleLL
from logic.voyageLL import VoyageLL
from logic.upcoming_voyageLL import UpcomingVoyageLL
from logic.past_voyageLL import PastVoyageLL
from datetime import datetime
from model.employee_model import Employee
from model.past_voyage_model import PastVoyage
from model.upcoming_voyage_model import UpcomingVoyage
from logic.validationLL import ValidationLL

class LogicWrapper():
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        self.employee = EmployeeLL(self) 
        self.airplane = AirplaneLL(self)
        self.destination = DestinationLL(self)
        self.schedule = ScheduleLL(self)
        self.voyage = VoyageLL(self)
        self.list_upcoming_voyage = UpcomingVoyageLL(self)
        self.list_past_voyages = PastVoyageLL(self)
        self.validation = ValidationLL()


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
    
    def total_hours_worked(self, employee: Employee, start: datetime, end: datetime):
        """ doc """
        return self.employee.get_total_hours_worked(employee, start, end)


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

    def popular_destination(self):
        return self.destination.get_most_popular_destination()

    def destination_info(self):
        return self.destination.destination_info()
    
    def distance_from_iceland(self):
        return self.destination.distance_from_iceland()
    
    #Airplanes:
    def airplane_types(self):
        """ Returns all airplane types within the system. """
        return self.airplane.get_all_airplane_types()
    
    def add_airplane(self, airplane):
        return self.airplane.add_airplane(airplane)
    
    def pilots_by_license(self):
        return self.airplane.pilots_by_license()
    
    def furthest_flown(self):
        return self.airplane.get_furthest_flown_plane()

    # def airplane_insignia_by_types(self):
    #     return self.airplane.airplane_insignia_by_type()

    #Upcoming voyages:
    def upcoming_voyages(self):
        """ doc. """
        return self.list_upcoming_voyage.get_upcoming_voyages()
    
    def add_upcoming_voyages(self, upcoming_voyage):
        return self.list_upcoming_voyage.add_upcoming_voyage(upcoming_voyage)

    def check_pilot_qualifications(self, aircraft_id, pilot):
        return self.list_upcoming_voyage.valid_pilot(aircraft_id, pilot)
    
    def flight_time(self, arr_at, departure_date_time):
        return self.list_upcoming_voyage.calculate_flight_time(arr_at, departure_date_time)

    #Past voyages:

    def get_all_voyages(self) -> list[PastVoyage | UpcomingVoyage]:
        """All voyages, past and upcoming.

        Returns:
            voyages: A list of all voyages.
        """
        
        return  (
            list(self.list_upcoming_voyage.get_upcoming_voyages().values()) 
            + list(self.list_past_voyages.get_past_voyages().values())
        )

    def past_voyages(self):
        """ doc 
        TODO: Typehint
        """
        return self.past_voyages.get_past_voyages()
    

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


    #validation
    def validate_name(self, name: str) -> bool:
        self.validation.validate_name(name)

    def validate_social_ID(self, socialID: str) -> bool:
        self.validation.validate_social_ID(socialID)

    def validate_flight(self, flight: str) -> bool:
        self.validation.validate_flight(flight)

    def validate_address(self, address: str) -> bool:
        self.validation.validate_address(address)

    def validate_phone_number(self, number: str) -> bool:
        self.validation.validate_number(number)

    def validate_email(self, email: str) -> bool:
        self.validation.validate_email(email)

    def validate_flight_nr(self, flight_nr: str) -> bool:
        self.validation.validate_flight_nr(flight_nr)

    def validate_voyage(self, voyage: str) -> bool:
        self.validation.validate_voyage(voyage)

    def date_validation(self, departure: datetime) -> bool:
        self.validation.date_validation(departure)