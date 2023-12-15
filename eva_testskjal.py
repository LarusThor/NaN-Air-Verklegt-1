from ui.mainUI import Main
from ui.scheduleUI import ScheduleUI
from datetime import date,datetime
from logic.logic_wrapper import LogicWrapper
from ui.scheduleUI import ScheduleUI
from ui.flight_infoUI import FlightInfoUI
from ui.airplaneUI import AirplaneUI
from ui.destinationsUI import DestinationsUI
from ui.employeesUI import EmployeeUI
#kemur aldrei upp að þau séu að vinna í vikunni
emp = EmployeeUI()
logic = LogicWrapper()

print(logic.employee_schedule_by_week("3009907461", "2023", "51"))
