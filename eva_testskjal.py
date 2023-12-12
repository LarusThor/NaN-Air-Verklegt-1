from ui.mainUI import Main
from ui.scheduleUI import ScheduleUI
from datetime import date
from logic.logic_wrapper import LogicWrapper


logic = LogicWrapper()
dt = date(2023,11,2)

print(logic.employee_working(dt))

# ma = Main()
# sc = ScheduleUI()


# dt = date(2023, 11, 2)

# print(sc.who_was_working(dt))