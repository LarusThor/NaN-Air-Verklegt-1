from model.employee_model import Employee

class Pilot(Employee):
    def __init__(self, name, socialID, email, phonenumber, landline, certification, pilotTitle) -> str:
        super().__init__(name, socialID, email, phonenumber, landline)
        self.certification = certification
        self.pilotTitle = pilotTitle


#name -> crew.csv -> name
#socialID -> crew.csv -> nid
#email -> crew.csv -> email
#phonenumber -> crew.csv -> phone_nr
#landline is optional
#certification -> crew.csv -> licence
#pilotTitle -> crew.csv -> rank