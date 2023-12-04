from model.employee_model import Employee

class FlightAttendant(Employee):
    def __init__(self, name, socialID, email, phonenumber, landline, fligtAttendant_title) -> str:
        super().__init__(name, socialID, email, phonenumber, landline)
        self.flightAttendant_title = fligtAttendant_title
    