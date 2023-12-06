from data.data_wrapper import DataWrapper
from dataclasses import asdict
from model.employee_model import Employee

class EmployeeLL:
    def __init__(self):
        self.data_wrapper = DataWrapper()
        self.employee_list = self.data_wrapper.get_all_staff_members()


    def get_employee_list(self) -> list[str]:
        """ Returns a list of all employees within the system. """
        return [employee.name for employee in self.employee_list.values()]

    def get_all_pilots(self) -> list[str]:
        """ Returns a list of all pilots. """
        name_list = []
        for employee_data in self.employee_list.values():
            if employee_data.role == "Pilot":
                name_list.append(employee_data.name)
        return name_list
    
    def get_flight_attendants(self):
        """ Returns a list of all flight attendants. """
        name_list = []
        for key, employee_data in self.employee_list.items():
            name = employee_data.name
            role = employee_data.role
            if role == "Cabincrew":
                name_list.append(name)
        return name_list

    def get_employee(self, social_id: str) -> Employee:
        """Returns information about a chosen employee."""
        return self.employee_list[social_id]

    def change_employee_info(self):
        """Lets user change employee information."""
        pass

    def add_employee(self, employee: Employee) -> None:
        """Adds employee to the system."""
        self.employee_list.append(employee)
        #TODO: ask datawrapper to write the employee



    def get_total_hours_worked(self):
        """Returns total hours an employee has worked."""
        pass


