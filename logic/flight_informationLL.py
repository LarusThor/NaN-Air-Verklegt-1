from data.data_wrapper import DataWrapper

class FlightInformation:
    def __init__(self, logic_wrapper):
        self.logic = logic_wrapper

    def capacity(self):
        capacity = dict()
        airplanes = self.logic.data_wrapper.get_airplanes()
        for keys, plane in airplanes.items():
            capacity[keys] = plane.capacity

        return capacity
      

    def flight_fully_booked(self):
        capacity = self.capacity
        upcoming_voyages = self.logic.upcoming_voyages()
        for voyage in upcoming_voyages.items():
            print(voyage)

        #return upcoming_voyages