from logic.logic_wrapper import LogicWrapper
from ui.employeesUI import EmployeeUI
from logic.flight_informationLL import FlightInformation
from data.data_wrapper import DataWrapper
from data.upcoming_voyageIO import UpcomingVoyageIO
from datetime import date

logic = LogicWrapper()
# print(logic.pilot_list())

day = date(2023, 11, 2)
print(logic.employee_working(day))
