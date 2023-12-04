from model.employee_model import Employee

class Pilot(Employee):
    def __init__(self, name, socialID, email, phonenumber, landline, certification, pilotTitle) -> str:
        super().__init__(name, socialID, email, phonenumber, landline)
        self.certification = certification
        self.pilotTitle = pilotTitle