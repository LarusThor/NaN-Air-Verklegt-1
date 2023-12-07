import csv
from model.upcoming_voyage_model import UpcomingVoyage

class UpcomingVoyageIO:

    def __init__(self):
        pass

    def read_upcoming_flights(self):
        upcoming_flights_dict = {}
        with open("files/upcoming_flights.csv", "r", newline='', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                flight_nr, dep_from, arr_at, departure, arrival, captain, copilot, fsm, fa1, fa2, fa3, fa4, fa5 = line.split(",")
                past_flight = UpcomingVoyage(flight_nr, dep_from, arr_at, departure, arrival, captain, copilot, fsm, fa1, fa2, fa3, fa4, fa5)
                upcoming_flights_dict[flight_nr] = (past_flight)

        return upcoming_flights_dict
    
    def add_upcoming_voyage(self, upcoming_flight):
        with open('files/upcoming_flights.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['flight_nr','dep_from','arr_at','departure','arrival','captain','copilot','fsm','fa1','fa2','fa3','fa4','fa5']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(upcoming_flight)
