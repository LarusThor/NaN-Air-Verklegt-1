import csv
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
                social_id, name, role, rank, license, address, phone_nr, email, landline = line.split(",")
                employee = Employee(name, social_id, role, rank, license, email, phone_nr, address, landline)
                employee_dict[social_id] = (employee)

        return employee_dict

    def add_employee(self, employee):
        with open('files\crew.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['nid', 'name', 'role', 'rank', 'licence', 'address', 'phone_nr', 'email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'nid': employee.socialID, 'name': employee.name, 'role': employee.role, 'rank': employee.rank, 'licence': employee.license, 'address': employee.home_address, 'phone_nr': employee.phonenumber, 'email': employee.email, 'landline': employee.landline})

#name -> crew.csv -> name
#socialID -> crew.csv -> nid
#email -> crew.csv -> email
#phonenumber -> crew.csv -> phone_nr
#home_address -> crew.csv -> 
#landline is optional

##nid,name,role,rank,licence,address,phone_nr, email


