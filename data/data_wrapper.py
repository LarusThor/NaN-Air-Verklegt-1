from data.employeeIO import EmployeeIO
from data.destinationIO import DestinationIO
from data.airplaneIO import AirplaneIO
from data.flight_attendantIO import FlightAttendantIO
from data.pilotIO import PilotIO
from data.scheduleIO import ScheduleIO
from data.voyageIO import VoyageIO


class DataWrapper:
    def __init__(self):
        self.employeeIO = EmployeeIO()

    def get_all_staff_members(self):
        return self.employeeIO.read_employee()
