from data.data_wrapper import DataWrapper
from dataclasses import asdict
from model.upcoming_voyage_model import UpcomingVoyage
from logic.airplaneLL import AirplaneLL

class UpcomingVoyageLL:
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        self.airplane = AirplaneLL()

        self.upcoming_flights_dict = self.data_wrapper.get_upcoming_flights()
        self.pilots_by_license = self.airplane.pilots_by_license()
        self.planes_by_type = self.airplane.airplane_insignia_by_type()
        # self.airplane_insignias_sorted = self.airplane.airplane_insignia_by_type()


    def get_upcoming_voyages(self):
        return self.upcoming_flights_dict


    def add_upcoming_voyage(self, upcoming_voyage):
        self.data_wrapper.add_upcoming_flights(upcoming_voyage)

    def valid_pilot(self, aircraft_id, pilot):
        license_check = self.planes_by_type.keys(aircraft_id)
        if license_check in self.pilots_by_license.keys() and pilot in self.pilots_by_license.values(license_check):
            return True

    def aircraft_availability():
        pass

    def staff_availability():
        pass


#flightnr
