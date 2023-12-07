from logic.employeeLL import EmployeeLL
from model.employee_model import Employee

emp_ll = EmployeeLL()

employee = Employee(
    social_id="broseph",
    name="Bruh Johnson",
    role="test_role",
    rank="test_rank",
    licence="f",
    email="f@f.f",
    phonenumber="0.5",
    home_address="bruh street 69",
    landline="??"
)

emp_ll.add_employee(employee)