#import wrapper

class EmployeeLL():
    def __init__(self, name, social_id, home_address, mobile_number, email, landline = None) -> None:
        #self.data_wrapper = data_connection
        self.name = name
        self.social_id = social_id
        self.home_address = home_address
        self.mobile_number = mobile_number
        self.email = email
        self.landline = landline
    
    def get_employee_list(self):
        pass
    
    def get_employee_info(self):
        pass
    
    def change_employee_info(self):
        pass

    def add_employee(self):
        pass

    def get_tottal_hours_worked(self):
        pass