from logic.employeeLL import EmployeeLL
from data.data_wrapper import DataWrapper
from logic.airplaneLL import AirplaneLL


# Assuming your class definition and method implementations are in the same module
# If not, you need to adjust the import statements accordingly


# Create an instance of AirplaneLL
airplane_ll = AirplaneLL()

# Test the get_all_airplane_types method
airplane_types = airplane_ll.get_all_airplane_types()

# Print the result
print("All Airplane Types:", airplane_types)


"""
social_id_to_test = "1405853585"  # Replace with an existing social ID in your data
employee_info = EmployeeLL.get_employee_info(social_id_to_test, 1405853585)

print(employee_info)
"""





"""
employee_manager = EmployeeLL()

# Test get_employee_list method
employee_list = employee_manager.get_employee_list(options=None)
print("All employees:")
print(employee_list)

# Test get_all_pilots method
pilots_list = employee_manager.get_flight_attendants()
print("\nPilots:")
print(pilots_list)
"""


""""
# Create an instance of EmployeeLL
employee_ll_instance = EmployeeLL()

# Call the get_employee_list method
employees = employee_ll_instance.get_employee_list()

# Print the result
print("Employee List:")
for employee in employees:
    print(employee)

"""
