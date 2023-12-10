from data.data_wrapper import DataWrapper
from dataclasses import asdict
from model.upcoming_voyage_model import UpcomingVoyage
from logic.logic_wrapper import LogicWrapper

class UpcomingVoyageLL:
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        self.logic_wrapper = LogicWrapper()

        self.upcoming_flights_dict = self.data_wrapper.get_upcoming_flights()
        self.airplane_insignias_sorted = self.logic_wrapper.airplane_insignia_by_types()


    def get_upcoming_voyages(self):
        return self.upcoming_flights_dict


    def add_upcoming_voyage(self, upcoming_voyage):
        self.data_wrapper.add_upcoming_flights(upcoming_voyage)

    def aircraft_availability():
        pass

    def staff_availability():
        pass


#flightnr
