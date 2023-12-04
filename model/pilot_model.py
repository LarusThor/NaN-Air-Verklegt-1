from model.employee_model import Employee

class Pilot(Employee):
    def __init__(self, name="", socialID="", email="", phonenumber=5812345, homephone=None, certification="", pilotTitle=""):
        super().__init__(name, socialID, email, phonenumber, homephone, certification)
        self.certification = certification
        self.pilotTitle = pilotTitle