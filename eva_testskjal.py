from ui.mainUI import Main
from ui.scheduleUI import ScheduleUI
from datetime import date,datetime
from logic.logic_wrapper import LogicWrapper
from ui.scheduleUI import ScheduleUI
from ui.flight_infoUI import FlightInfoUI
from ui.airplaneUI import AirplaneUI
from ui.destinationsUI import DestinationsUI

#kemur aldrei upp að þau séu að vinna í vikunni

logic = LogicWrapper()
de = DestinationsUI()

dd = datetime(2023, 11, 6, 0, 0, 0)
dt = datetime(2023, 11, 7, 0, 0, 0)

print(logic.airplane_insignia_by_types())

print(logic.pilots_by_license())


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
