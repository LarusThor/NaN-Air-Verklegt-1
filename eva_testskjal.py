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

print(emp.get_employee())



#print(logic.airplane_types())

#print(logic.get_most_experienced_employee())


# airplane_types = logic.airplane_types()
# licences = {(i+1): licence for i, licence in (airplane_types)}
# print(licences)

# print("Licenses:")
# for index, license in licences.items():
#     print(f"{index}. {license}")
    #print(f"{license.keys()}. {licence.values()}")


# sc = ScheduleUI()
# fi = FlightInfoUI()

# print(logic.airplane_types())

#print(fi.get_flight_status_by_voyage())
#print(fi.get_flight_status_by_voyage())

# ma = Main()
# sc = ScheduleUI()



# print(sc.who_was_working(dt))
