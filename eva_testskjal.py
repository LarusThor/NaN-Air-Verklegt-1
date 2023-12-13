from ui.mainUI import Main
from ui.scheduleUI import ScheduleUI
from datetime import date,datetime
from logic.logic_wrapper import LogicWrapper


logic = LogicWrapper()

date_input = "2023/12/21" 
date_format = "%Y/%m/%d"
a_date = datetime.strptime(date_input, date_format)
dh = a_date.date()
print(dh)
# dt = a_date.strptime(date_format)
# print(dt)


print(logic.employee_working(dh))

# ma = Main()
# sc = ScheduleUI()


# dt = date(2023, 11, 2)

# print(sc.who_was_working(dt))
