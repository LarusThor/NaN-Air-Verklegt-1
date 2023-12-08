from data.data_wrapper import DataWrapper
from dataclasses import asdict
from model.employee_model import Employee
from model.past_voyage_model import PastVoyage
from datetime import datetime

class EmployeeLL:
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()

        self.employee_dict = self.data_wrapper.get_all_staff_members()


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

    def get_total_hours_worked(self, employee: Employee, past_voyage: PastVoyage):
        """Returns total hours an employee has worked."""
        flights_list = []
        total_hours = 0
        workers = [past_voyage.captain, past_voyage.copilot, past_voyage.fsm, past_voyage.fa1, past_voyage.fa2, past_voyage.fa3, past_voyage.fa4, past_voyage.fa5]
        departure = datetime.strptime(past_voyage.departure, "%Y-%m-%d %H:%M:%S")
        arrival = datetime.strptime(past_voyage.arrival, "%Y-%m-%d %H:%M:%S") 
        hours = (arrival - departure)
        if employee.social_id in workers:
            flights_list.append(f"{employee.name} worked {hours} hours")
            total_hours += hours.total_seconds() / 3600

        return employee.name, flights_list, total_hours


#3009907461,William Carillo,Pilot,Captain,NAFokkerF100,Fellsmúli 1,8998801, bruck@comcast.net, 7854878