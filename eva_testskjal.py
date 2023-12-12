from logic.logic_wrapper import LogicWrapper
from ui.employeesUI import EmployeeUI
from logic.flight_informationLL import FlightInformation
from data.data_wrapper import DataWrapper
from data.upcoming_voyageIO import UpcomingVoyageIO

# logic = LogicWrapper()
# print(logic.pilot_list())

voyage = UpcomingVoyageIO()
print(voyage.read_upcoming_flights().values())
