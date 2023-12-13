from ui.mainUI import Main
from ui.scheduleUI import ScheduleUI
from datetime import date,datetime
from logic.logic_wrapper import LogicWrapper


logic = LogicWrapper()

print(logic.employee_info("1234567899"))

# ma = Main()
# sc = ScheduleUI()


# dt = date(2023, 11, 2)

# print(sc.who_was_working(dt))
