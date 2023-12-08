from data.data_wrapper import DataWrapper
from dataclasses import asdict
from model.employee_model import Employee
from model.past_voyage_model import PastVoyage
from datetime import datetime

class EmployeeLL:
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()

        self.employee_dict = self.data_wrapper.get_all_staff_members()
        self.voyage_list = self.data_wrapper.read_past_flights()

    def get_employee_dict(self) -> list[str]:
        """ Returns a list of all employees within the system. """
        return [employee.name for employee in self.employee_dict.values()]


    def get_all_pilots(self) -> list[str]:
        """ Returns a list of all pilots. """
        pilot_list = []
        for employee_data in self.employee_dict.values():
            if employee_data.role == "Pilot":
                pilot_list.append(employee_data.name)
        return pilot_list
    

    def get_flight_attendants(self) -> list[str] :
        """ Returns a list of all flight attendants. """
        flight_attendant_list = []
        for employee_data in self.employee_dict.values():
            if employee_data.role == "Cabincrew":
                flight_attendant_list.append(employee_data.name)
        return flight_attendant_list


    def get_employee(self, social_id: str) -> Employee:
        """Returns information about a chosen employee."""
        return self.employee_dict[social_id]


    def change_employee_info(self, employee: Employee):
        """Lets user change employee information."""
        # TODO: cannot change name

        assert employee.social_id in self.employee_dict, "Employee does not exist!"

        self.employee_dict[employee.social_id] = employee

        self.data_wrapper.write_employees(list(self.employee_dict.values()))


    def add_employee(self, employee: Employee) -> None:
        """Adds employee to the system."""

        assert employee.social_id not in self.employee_dict, "Employee with same social_id already exists!"

        self.employee_dict[employee.social_id] = employee
        self.data_wrapper.write_employees(list(self.employee_dict.values()))

    def get_total_hours_worked(self, employee: Employee):
        """Returns total hours an employee has worked."""
        flights_list = []
        total_hours = 0
        for flight in self.voyage_list.values():
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]
            print("TEEEST", workers)
            if employee.social_id in workers:
                departure = datetime.strptime(flight.departure, "%Y-%m-%d %H:%M:%S")
                arrival = datetime.strptime(flight.arrival, "%Y-%m-%d %H:%M:%S") 
                hours = (arrival - departure)
                flights_list.append(f"{employee.name} worked {hours} hours")
                total_hours += hours.total_seconds() / 3600

        return employee.name, flights_list, total_hours


#3009907461,William Carillo,Pilot,Captain,NAFokkerF100,Fellsmúli 1,8998801, bruck@comcast.net, 7854878