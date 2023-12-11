from data.data_wrapper import DataWrapper
from dataclasses import asdict
from model.upcoming_voyage_model import UpcomingVoyage
from datetime import datetime

class UpcomingVoyageLL:
    def __init__(self, logic_wrapper) -> None:
        self.logic = logic_wrapper
        self.data_wrapper = DataWrapper()
        #self.airplane = AirplaneLL()

        #self.upcoming_flights_dict = self.data_wrapper.get_upcoming_flights()
        #self.pilots_by_license = self.airplane.pilots_by_license()
        #self.planes_by_type = self.airplane.airplane_insignia_by_type()
        # self.airplane_insignias_sorted = self.airplane.airplane_insignia_by_type()


    def get_upcoming_voyages(self):
        upcoming_flights_dict = self.data_wrapper.get_upcoming_flights()
        return upcoming_flights_dict


    def add_upcoming_voyage(self, upcoming_voyage):
        self.data_wrapper.add_upcoming_flights(upcoming_voyage)

    def calculate_flight_time(self, arr_at, return_flight_time):
        #Need to implement addition of time from destinations dictionary
        arrival_time_flight_duration = self.data_wrapper.get_all_destinations_info()
        estimated_flight_time = (arrival_time_flight_duration.keys(arr_at))[-1]
        return_flight_time = return_flight_time.split()
        flight_time_to_calculate = int(return_flight_time[0])
        arrival_flight_time = flight_time_to_calculate + estimated_flight_time
        return_flight_time[0] = arrival_flight_time
        # estimated_flight_time = list(arrival_time_flight_duration[arr_at])
        # int(estimated_flight_time[-1]) #þá er þetta t.d. 4



        
        return 
        # start = datetime.strptime({departure_time}, "%H:%M:%S") 
        # end = datetime.strptime({arrival_time}, "%H:%M:%S")

        # time_difference = end - start
        # seconds = time_difference.total_seconds()

        # minutes, seconds = divmod(seconds, 60)
        # hours, minutes = divmod(minutes, 60)

        # return(hours, minutes, seconds)


    def valid_pilot(self, aircraft_id, pilot):
        pilots_by_license = self.airplane.pilots_by_license()
        planes_by_type = self.airplane.airplane_insignia_by_type()

        license_check = planes_by_type.keys(aircraft_id)
        if license_check in pilots_by_license.keys() and pilot in pilots_by_license.values(license_check):
            return True

    def aircraft_availability():
        pass

    def staff_availability():
        pass



#flightnr
