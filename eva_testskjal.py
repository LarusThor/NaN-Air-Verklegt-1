from logic.employeeLL import EmployeeLL
from model.employee_model import Employee
from logic.destinationLL import DestinationLL


dest_ll = DestinationLL()

print(dest_ll.get_most_popular_destination())

"""
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

emp_ll.change_employee_info(employee)
"""