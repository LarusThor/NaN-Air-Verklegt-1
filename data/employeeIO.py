from model.employee_model import Employee

class EmployeeIO:
    def __init__(self):
        pass

    def read_employee(self):
        employee_dict = {}
        with open("files/crew.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                social_id, name, _, _, _, address, phone_nr, email = line.split(",")
                #employee_dict[social_id] = [name, role, rank, licence, address, phone_nr, email]

                employee = Employee(name, social_id, email, phone_nr, address, landline=None)
                employee_dict[social_id] = (employee)

        return employee_dict

#name -> crew.csv -> name
#socialID -> crew.csv -> nid
#email -> crew.csv -> email
#phonenumber -> crew.csv -> phone_nr
#home_address -> crew.csv -> 
#landline is optional

