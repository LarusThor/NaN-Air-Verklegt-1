from data.data_wrapper import DataWrapper
from logic.airplaneLL import AirplaneLL
from logic.destinationLL import DestinationLL
from logic.employeeLL import EmployeeLL
from logic.scheduleLL import ScheduleLL
from logic.upcoming_voyageLL import UpcomingVoyageLL
from logic.past_voyageLL import PastVoyageLL
from datetime import datetime, date
from model.employee_model import Employee
from model.past_voyage_model import PastVoyage
from model.upcoming_voyage_model import UpcomingVoyage
from logic.validationLL import ValidationLL
from logic.flight_informationLL import FlightInformationLL
from model.destination_model import Destination
from model.airplane_model import Airplane


class LogicWrapper:
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        self.employee = EmployeeLL(self)
        self.airplane = AirplaneLL(self)
        self.destination = DestinationLL(self)
        self.schedule = ScheduleLL(self)
        self.list_upcoming_voyage = UpcomingVoyageLL(self)
        self.past_voyages = PastVoyageLL(self)
        self.validation = ValidationLL()
        self.flight_information = FlightInformationLL(self)

    # Employee:
    def employee_dict(self) -> list[str]:
        """Returns a list of all employees."""
        return self.employee.get_employee_dict()

    def pilot_list(self) -> list[str]:
        """Returns a list of all pilots within the system."""
        return self.employee.get_all_pilots()

    def flight_attendant_list(self) -> list[str]:
        """Returns a list of all flight attendats within the system."""
        return self.employee.get_flight_attendants()

    def add_employee(self, employee: Employee) -> None:
        """Adds employee to the system."""
        return self.employee.add_employee(employee)

    def employee_info(self, employee_social_id: str) -> Employee:
        """Returns information about a specific employee.

        Args:
            employee_social_id: The social ID of the employee
        """
        return self.employee.get_employee(employee_social_id)

    def change_employee_info(self, employee: Employee) -> None:
        """Changes specific information about an employee."""
        return self.employee.change_employee_info(employee)

    def total_hours_worked(self, employee: Employee, start: datetime, end: datetime) -> tuple[list[str], float]:
        """Returns hours worked by an employee for a specific time frame."""
        return self.employee.get_total_hours_worked(employee, start, end)

    def get_total_future_hours_worked(self, employee: Employee, start: datetime, end: datetime) -> tuple[list[str], float]:
        """Takes a specific instance of an employee from the model class, a start, end date in datetime
        and returns hours to be worked by an employee for a specific time frame."""
        return self.employee.get_total_future_hours_worked(employee, start, end)

    def get_most_experienced_employee(self) -> list[tuple]:
        """Returns the employee who has gone on the most voyages."""
        return self.employee.get_most_experienced_employee()

    def get_available_employees_over_period(self, period_start: datetime, period_end: datetime) -> list[Employee]:
        """Returns available employees over a certain period of time."""
        return self.employee.get_available_employees_over_period(period_start, period_end)

    def get_qualified_captains_for_plane_type(self, plane_type_id: str) -> dict[str, Employee]:
        """Returns qualified captaind for a specific plane type"""
        return self.employee.get_qualified_captains_for_plane_type(plane_type_id)

    def get_qualified_copilots_for_plane_type(self, plane_type_id: str) -> dict[str, Employee]:
        """Returns qualified copilots for plane type"""
        return self.employee.get_qualified_copilots_for_plane_type(plane_type_id)

    # Destinations:
    def destination_info_overview(self) -> dict:
        """Returns a list of information about the destinations in the system."""
        return self.destination.get_destination_info()

    def only_destinations(self) -> list:
        """Returns a list of destinations."""
        return self.destination.get_only_destinations()

    def destination_list(self) -> list:
        """Returns a list of all destinations within the system."""
        return self.destination.get_destination_list()

    def add_destination(self, destination: Destination) -> None:
        """Takes in a customer object and forwards it to the data layer."""
        return self.destination.add_destination(destination)

    def popular_destination(self) -> dict:
        """Returns the most popular destination."""
        return self.destination.get_most_popular_destination()

    def destination_info(self) -> list:
        """Returns information about the destination."""
        return self.destination.destination_info()

    def distance_from_iceland(self) -> dict:
        """returns a dictionary of destinations and their distance from iceland in km."""
        return self.destination.distance_from_iceland()

    def update_destination_info(self, destination: Destination) -> None:
        """Updates a specific destination's information."""
        return self.destination.change_destination_info(destination)

    def update_contact_info(self, destination: Destination) -> None:
        """Updates a specific emergency contact information."""
        return self.destination.update_contact_info(destination)

    # Airplanes:
    def get_airplanes_info_overview(self, airplane_insignia: str):
        """Returns information about a specific airplane by its insignia."""
        return self.airplane.get_airplanes_info_overview(airplane_insignia)

    def airplane_types(self) -> set:
        """Returns all airplane types within the system."""
        return self.airplane.get_all_airplane_types()

    def add_airplane(self, airplane: Airplane) -> None:
        """Adds airplane to the system."""
        return self.airplane.add_airplane(airplane)

    def pilots_by_license(self) -> dict:
        """Returns a dictionary of all pilots based on their license."""
        return self.airplane.pilots_by_license()

    def furthest_flown(self) -> tuple[str, int]:
        """Returns the plane that has flown the furthest."""
        return self.airplane.get_furthest_flown_plane()

    def airplane_insignia_by_types(self) -> dict:
        """Returns a dictionary by insignia and its values"""
        return self.airplane.airplane_insignia_by_type()

    def airplane_usage(self) -> tuple[str, dict]:
        """Returns how much each airplane has been used."""
        return self.airplane.get_airplane_usage()

    def get_total_future_hours_for_airplane(self, plane_insignia: str, start: datetime, end: datetime) -> float:
        """Gets future hours an employee will fly."""
        return self.airplane.get_total_future_hours_for_airplane(plane_insignia, start, end)

    # Upcoming voyages:
    def upcoming_voyages(self) -> dict[str, UpcomingVoyage]:
        """Returns a dictionary of upcoming voyage models."""
        return self.list_upcoming_voyage.get_upcoming_voyages()

    def add_upcoming_voyages(self, upcoming_voyage: UpcomingVoyage) -> None:
        """Adds a new voyage to the system."""
        return self.list_upcoming_voyage.add_upcoming_voyage(upcoming_voyage)

    def check_pilot_qualifications(self, aircraft_id: str, pilot) -> bool:
        """Verifies a pilots qualifications."""
        return self.list_upcoming_voyage.valid_pilot(aircraft_id, pilot)

    def flight_time(self, arr_at, departure_date_time: datetime) -> datetime:
        """Returns calculated flight time for each destination."""
        return self.list_upcoming_voyage.calculate_flight_time(
            arr_at, departure_date_time
        )

    def add_staff_to_voyage(self, added_staff) -> None:
        """Deff adds staff to an existing voyage."""
        return self.list_upcoming_voyage.add_staff_for_voyage(added_staff)

    def staff_availability_check(self, captain, departure, return_flight_arrival):
        """Checks what staff is available over a specific time period."""
        return self.list_upcoming_voyage.staff_availability(
            captain, departure, return_flight_arrival
        )

    def voyage_info_for_return_flight(self, voyage_flight_number: str, voyage_date: str) -> UpcomingVoyage:
        """Gets return flight information by checking next flight from original flight."""
        return self.list_upcoming_voyage.detect_voyage_info_return_flight(
            voyage_flight_number, voyage_date
        )

    def get_available_airplanes_over_period(self, period_start: datetime, period_end: datetime) -> dict[str, Employee]:
        """Returns a list of all airplanes that are available over a given period.

        Args:
            period_start: Start of the period.
            period_end: End of the period.
        """
        return self.airplane.get_available_airplanes_over_period(
            period_start, period_end
        )

    def get_upcoming_voyage_by_flight_nr_and_date(self, flight_nr: str, departure_date: str) -> UpcomingVoyage:
        """Gets upcoming flights on a specific day with a specific flight number."""
        return self.list_upcoming_voyage.get_voyage_by_flight_nr_and_date(
            flight_nr, departure_date
        )

    # Past voyages:

    def get_past_voyages(self) -> dict:
        """Returns all past voyages"""
        return self.past_voyages.get_past_voyages()

    def get_all_voyages(self) -> list[PastVoyage | UpcomingVoyage]:
        """All voyages, past and upcoming.

        Returns:
            voyages: A list of all voyages.
        """

        return self.upcoming_voyages() | self.get_past_voyages()

    # schedule
    def employee_schedule_by_week(self, employee: str, year: str, week: str) -> str:
        """Returns an employees schedule on a specific week."""
        return self.schedule.employee_schedule_by_week(employee, year, week)

    def employee_working(self, date: date)  -> set[tuple[Employee, str]]:
        """Checks what employees are working on a specific day"""
        return self.schedule.employee_working(date)

    def employee_not_working(self, date: date) -> set[Employee]:
        """Returns a set of employees not working on a specific date."""
        return self.schedule.employee_not_working(date)

    # flight information
    def flight_fully_booked(self):
        """Returns information about flights and wether they are fully booked."""
        return self.flight_information.flight_fully_booked()

    def capacity(self):
        """Returns plane capacity."""
        return self.flight_information.capacity()

    # validation
    def validate_choice(self, input: int, length: int) -> bool:
        """Validates numerical action input."""
        self.validation.validate_choice(input, length)

    def validate_name(self, name: str) -> bool:
        """Validates name input."""
        self.validation.validate_name(name)

    def validate_social_ID(self, socialID: str) -> bool:
        """Validates social ID input."""
        self.validation.validate_social_ID(socialID)

    def validate_flight(self, flight: str) -> bool:
        """Validates flight. #TODO: skrifa betur, ég skil ekki þennan almennilega."""
        self.validation.validate_flight(flight)

    def validate_address(self, address: str) -> bool:
        """Validates address input."""
        self.validation.validate_address(address)

    def validate_phone_number(self, number: str) -> bool:
        """Validates phone number input."""
        self.validation.validate_number(number)

    def validate_email(self, email: str) -> bool:
        """Validates email input."""
        self.validation.validate_email(email)

    def validate_flight_nr(self, flight_nr: str) -> bool:
        """Validates flight number input."""
        self.validation.validate_flight_nr(flight_nr)

    def validate_voyage(self, voyage: str) -> bool:
        """TODO: einhver sem skilur þennan skilgreina."""
        self.validation.validate_voyage(voyage)

    # def date_validation(self, date: datetime) -> bool:
    #     """validates date."""
    #     self.validation.date_validation(date)

    def validate_date(self, date:str) -> bool:
        """ Validates a date """
        self.validation.validate_date(date)
    
    def validate_destination_id(self, destination_id: str) -> bool:
        """ Validates a destination ID input from user """
        self.validation.validate_destination_id(destination_id)

    def validation_destination_name(self, destination_name: str) -> bool:
        """ Validate name of a destination that the user inputs """
        self.validation.validate_destination_name(destination_name)