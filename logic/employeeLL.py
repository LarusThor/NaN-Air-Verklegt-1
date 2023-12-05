from data.data_wrapper import DataWrapper

class EmployeeLL:
    def __init__(self):
        self.employee_list = DataWrapper.get_all_staff_members()

    def get_employee_list(self):
        """ Returns a list of all employees within the system. """
        name_list = []
        for key, value in self.employee_list.items():
            social_id = key
            name = value[0]
            role = value[1]
            rank = value[2]
            licence = value[3]
            address = value[4]
            phone_nr = value[5]
            name_list.append(name)
        return name_list

         
    def get_employee_info(self):
        """ Returns information about a chosen employee. """
        pass
    
    def change_employee_info(self):
        """ Lets user change employee information. """
        pass

    def add_employee(self):
        """ Adds employee to the system. """
        pass

    def get_total_hours_worked(self):
        """ Returns total hours an employee has worked. """
        pass