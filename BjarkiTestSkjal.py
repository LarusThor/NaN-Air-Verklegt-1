from logic.employeeLL import EmployeeLL
from data.data_wrapper import DataWrapper

# Create an instance of EmployeeLL
employee_ll_instance = EmployeeLL()

# Call the get_employee_list method
employees = employee_ll_instance.get_employee_dict()

# Print the result
print("Employee List:")
for employee in employees:
    print(employee)
