from ui.mainUI import Main
from ui.scheduleUI import ScheduleUI
from datetime import date,datetime
from logic.logic_wrapper import LogicWrapper

#kemur aldrei upp að þau séu að vinna í vikunni


logic = LogicWrapper()

employee = logic.employee_info("2410876598")

print(logic.employee_schedule_by_week(employee.social_id, "2023", "44"))

# ma = Main()
# sc = ScheduleUI()


# dt = date(2023, 11, 2)

# print(sc.who_was_working(dt))
