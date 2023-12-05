from model.employee_model import Employee

class FlightAttendant(Employee):
    def __init__(self, name, socialID, email, phonenumber, landline, fligtAttendant_title) -> str:
        super().__init__(name, socialID, email, phonenumber, landline)
        self.flightAttendant_title = fligtAttendant_title

#name -> crew.csv -> name
#socialID -> crew.csv -> nid
#email -> crew.csv -> email
#phonenumber -> crew.csv -> phone_nr
#landline is optional
#flightAttendant_title -> crew.csv -> rank
    