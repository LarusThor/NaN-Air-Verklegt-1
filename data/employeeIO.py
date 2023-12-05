class EmployeeIO:
    def __init__(self):
        pass

    def read_employee(self):
        employee_dict = {}
        with open("files/crew.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                social_id, name, role, rank, licence, address, phone_nr, email = line.split(",")
                employee_dict[social_id] = [name, role, rank, licence, address, phone_nr, email]
                
        return employee_dict