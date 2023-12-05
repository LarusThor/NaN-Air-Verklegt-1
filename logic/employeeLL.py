from data.data_wrapper import DataWrapper

class EmployeeLL:
    def __init__(self):
        self.data_wrapper = DataWrapper()
        self.employee_list = self.data_wrapper.get_all_staff_members()


    def get_employee_list(self, options):
        """ Returns a list of all employees within the system. """
        name_list = []
        for social_id, employee_data in self.employee_list.items():
            name = employee_data[0]
            name_list.append(name)
        return name_list

    def get_all_pilots(self):
        name_list = []
        for key, value in self.employee_list.items():
            name = value[0]
            role = value[1]
            if role == "Pilot":
                name_list.append(name)
        return name_list
    
    def get_flight_attendants(self):
        name_list = []
        for key, value in self.employee_list.items():
            name = value[0]
            role = value[1]
            rank = value[2]
            if rank == "Flight Attendant":
                name_list.append(name)
        return name_list

    def get_employee_info(self, social_id):
        """Returns information about a chosen employee."""
        for key, value in self.employee_list.items():
            name = value[0]
            role = value[1]
            rank = value[2]
            licence = value[3]
            address = value[4]
            phone_nr = value[5]
            email = value[6]
            if key == social_id:
                return f"{name}, {social_id}, {phone_nr}, {email}, {address}, {role}, {licence}"

    def change_employee_info(self):
        """Lets user change employee information."""
        pass

    def add_employee(self):
        """Adds employee to the system."""
        pass

    def get_total_hours_worked(self):
        """Returns total hours an employee has worked."""
        pass


