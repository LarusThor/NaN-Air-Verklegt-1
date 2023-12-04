#import wrapper

class EmployeeLL():
    def __init__(self, name:str, social_id:str, home_address:str, mobile_number:int, email:str, landline:int = None) -> None:
        #self.data_wrapper = data_connection
        self.name = name
        self.social_id = social_id
        self.home_address = home_address
        self.mobile_number = mobile_number
        self.email = email
        self.landline = landline
    
    def get_employee_list(self):
        """ Returns a list of all employees within the system. """
        pass
    
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