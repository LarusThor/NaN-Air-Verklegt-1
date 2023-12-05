from data.employeeIO import EmployeeIO

class DataWrapper():
    def __init__(self):
        self.employeeIO = EmployeeIO()

    def get_all_staff_memmbers(self):
        return self.employeeIO.read_employee()