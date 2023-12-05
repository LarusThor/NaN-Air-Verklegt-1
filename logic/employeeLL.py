from data.data_wrapper import DataWrapper

class EmployeeLL():
    def __init__(self, employee_list:list) -> None:
        #self.data_wrapper = data_connection
        self.employee_list = DataWrapper.get_all_staff_memmbers()
        for key, value in employee_list:
            self.social_id = key
            self.name = value[0]
            self.role = value[1]
            self.rank = value[2]
            self.licence = value[3]
            self.address = value[4]
            self.phone_nr = value[5]

    def get_employee_list(self):
        """ Returns a list of all employees within the system. """
        name_list = []
        for key, value in self.employee_list:
            self.social_id = key
            self.name = value[0]
            name_list.append(self.name)
         
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