from ui.mainUI import Main
from ui.scheduleUI import ScheduleUI
from datetime import date,datetime
from logic.logic_wrapper import LogicWrapper
from ui.scheduleUI import ScheduleUI
from ui.flight_infoUI import FlightInfoUI

#kemur aldrei upp að þau séu að vinna í vikunni



sc = ScheduleUI()
fi = FlightInfoUI()
logic = LogicWrapper()


print(fi.get_flight_status_by_voyage())
#print(fi.get_flight_status_by_voyage())

# ma = Main()
# sc = ScheduleUI()



# print(sc.who_was_working(dt))
