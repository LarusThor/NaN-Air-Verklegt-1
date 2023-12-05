from data.data_wrapper import DataWrapper
from airplaneLL import AirplaneLL
from destinationLL import DestinationLL
from employeeLL import EmployeeLL
from flightattendantLL import FlightAttendant
from pilotLL import PilotLL
from scheduleLL import ScheduleLL
from voyageLL import VoyageLL
from validationLL import ValidationLL

class LogicWrapper():
    def __init__(self, data_connection) -> None:
        self.DataWrapper = DataWrapper()
        pass