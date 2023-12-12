from data.data_wrapper import DataWrapper

class FlightInformation:
    def __init__(self, logic_wrapper):
        self.logic = logic_wrapper

    def capacity(self):
        pass

    def flight_fully_booked(self):
        plane_types = self.logic.airplane_insignia_by_types()
        capacity = self.capacity
        upcoming_voyages = self.logic.upcoming_voyages()
        return upcoming_voyages