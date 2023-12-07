from logic.employeeLL import EmployeeLL
from model.employee_model import Employee
from data.airplaneIO import AirplaneIO
from logic.airplaneLL import AirplaneLL

plane_io = AirplaneIO()

print(plane_io.airplane_types())


plane_ll = AirplaneLL()

print(plane_ll.get_all_airplane_types())