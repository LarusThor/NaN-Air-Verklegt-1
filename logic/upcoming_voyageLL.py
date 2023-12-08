from data.data_wrapper import DataWrapper
from dataclasses import asdict
from model.upcoming_voyage_model import UpcomingVoyage

class UpcomingVoyageLL:
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()

        self.upcoming_flights_dict = self.data_wrapper.get_upcoming_flights()

    def get_upcoming_voyages(self):
        return self.upcoming_flights_dict

 


#flightnr
