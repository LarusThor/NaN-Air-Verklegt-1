from data.data_wrapper import DataWrapper
from dataclasses import asdict
from model.employee_model import Employee

class EmployeeLL:
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        self.employee_list = self.data_wrapper.get_all_staff_members()


    def get_employee_list(self) -> list[str]:
        """ Returns a list of all employees within the system. """
        return [employee.name for employee in self.employee_list.values()]


    def get_all_pilots(self) -> list[str]:
        """ Returns a list of all pilots. """
        pilot_list = []
        for employee_data in self.employee_list.values():
            if employee_data.role == "Pilot":
                pilot_list.append(employee_data.name)
        return pilot_list
    

    def get_flight_attendants(self) -> list[str] :
        """ Returns a list of all flight attendants. """
        flight_attendant_list = []
        for employee_data in self.employee_list.values():
            if employee_data.role == "Cabincrew":
                flight_attendant_list.append(employee_data.name)
        return flight_attendant_list


    def get_employee(self, social_id: str) -> Employee:
        """Returns information about a chosen employee."""
        return self.employee_list[social_id]


    def change_employee_info(self):
        """Lets user change employee information."""
        pass


    def add_employee(self, employee: Employee) -> None:
        """Adds employee to the system."""
        self.employee_list.append(employee)
        self.add_employee(Employee)


    def get_total_hours_worked(self):
        """Returns total hours an employee has worked."""
        pass


