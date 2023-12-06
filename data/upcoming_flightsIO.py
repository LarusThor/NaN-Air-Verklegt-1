import csv
from model.upcoming_flight_model import UpcomingFlight

class upcomingFlightsIO:

    def __init__(self):
        pass

    def read_past_flights(self):
        upcoming_flights_dict = {}
        with open("files/upcoming_flights.csv", "r", newline='', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                flight_nr, dep_from, arr_at, departure, arrival = line.split(",")
                past_flight = UpcomingFlight(flight_nr, dep_from, arr_at, departure, arrival)
                upcoming_flights_dict[flight_nr] = (past_flight)

        return upcoming_flights_dict

#flight_nr,dep_from,arr_at,departure,arrival
