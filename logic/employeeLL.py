from data.data_wrapper import DataWrapper
from dataclasses import asdict
from model.employee_model import Employee

class EmployeeLL:
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()

        # TODO: don't store employees here, always ask data 
        self.employee_dict = self.data_wrapper.get_all_staff_members()
        print(self.employee_dict)


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

    def get_total_hours_worked(self):
        """Returns total hours an employee has worked."""
        pass


