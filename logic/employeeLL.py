from data.data_wrapper import DataWrapper
from dataclasses import asdict
from model.employee_model import Employee

class EmployeeLL:
    def __init__(self):
        self.data_wrapper = DataWrapper()
        self.employee_list = self.data_wrapper.get_all_staff_members()


    def get_employee_list(self):
        """ Returns a list of all employees within the system. """
        name_list = []
        for social_id, employee_data in self.employee_list.items():
            name = employee_data.name
            name_list.append(name)
        return name_list

    def get_all_pilots(self):
        """ Returns a list of all pilots. """
        name_list = []
        for key, employee_data in self.employee_list.items():
            name = employee_data.name
            role = employee_data.role
            if role == "Pilot":
                name_list.append(name)
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

    def add_employee(self, employee_info):
        """Adds employee to the system."""
        pass

    def get_total_hours_worked(self):
        """Returns total hours an employee has worked."""
        pass


