from data.data_wrapper import DataWrapper

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

    def get_employee_info(self, social_id):
        """Returns information about a chosen employee."""
        social_id = str(social_id)
        for key, employee_data in self.employee_list.items():
            name = employee_data.name
            role = employee_data.role
            rank = employee_data.rank
            licence = employee_data.license
            address = employee_data.address
            phone_nr = employee_data.phone_nr
            email = employee_data.email
            if str(key) == str(social_id):
                return name
                #return f"{name}, {social_id}, {phone_nr}, {email}, {address}, {role}, {licence}"

    def change_employee_info(self):
        """Lets user change employee information."""
        pass

    def add_employee(self):
        """Adds employee to the system."""
        pass

    def get_total_hours_worked(self):
        """Returns total hours an employee has worked."""
        pass


