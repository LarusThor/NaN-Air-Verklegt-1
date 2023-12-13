from ui.mainUI import Main
from ui.scheduleUI import ScheduleUI
from datetime import date,datetime
from logic.logic_wrapper import LogicWrapper
from ui.scheduleUI import ScheduleUI

#kemur aldrei upp að þau séu að vinna í vikunni

logic = LogicWrapper()
start = datetime(2022, 11, 2)
end = datetime(2023, 11, 2)
employee = logic.employee_info("3009907461")


print(logic.total_hours_worked(employee, start, end))



# ma = Main()
# sc = ScheduleUI()



# print(sc.who_was_working(dt))
