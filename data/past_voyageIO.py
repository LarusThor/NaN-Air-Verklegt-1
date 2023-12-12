import csv
from pathlib import Path
from model.past_voyage_model import PastVoyage
from datetime import datetime

class PastVoyageIO:
    def __init__(self):
        pass


    def read_past_flights(self) -> dict[str, PastVoyage]:
        """ Returns a dictionary of all past flights from csv file. """
        past_flights_dict = {}
        with open("files/past_flights.csv", "r", newline='', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                id, flight_nr, dep_from, arr_at, departure, arrival, aircraft_id, captain, copilot, fsm, fa1, fa2, fa3, fa4, fa5, seats_sold = line.split(",")
                past_flight = PastVoyage(id,flight_nr,dep_from,arr_at,datetime.strptime(departure, "%Y-%m-%d %H:%M:%S"),datetime.strptime(arrival, "%Y-%m-%d %H:%M:%S"),aircraft_id,captain,copilot,fsm,fa1,fa2,fa3,fa4,fa5, seats_sold)
                past_flights_dict[id] = past_flight

        return past_flights_dict
    

    def add_past_voyage(self, past_flights) -> None:
        """ Adds a past voyage to the system. """
        file_path = Path('files/past_flights.csv')

        fieldnames = ['flight_nr', 'dep_from', 'arr_at', 'departure', 'arrival', 'captain','copilot','fsm','fa1','fa2','fa3','fa4','fa5', "seats_sold"]

        with open(file_path, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for upcoming_flight in past_flights:
                writer.writerow(
                    {
                    'flight_nr': upcoming_flight.flight_nr, 
                     'dep_from': upcoming_flight.dep_from, 
                     'arr_at': upcoming_flight.arr_at, 
                     'departure': upcoming_flight.departure, 
                     'arrival': upcoming_flight.arrival, 
                     'captain': upcoming_flight.captain, 
                     'copilot': upcoming_flight.copilot, 
                     'fsm': upcoming_flight.fsm, 
                     'fa1': upcoming_flight.fa1, 
                     'fa2': upcoming_flight.fa2, 
                     'fa3': upcoming_flight.fa3, 
                     'fa4':upcoming_flight.fa4, 
                     'fa5':upcoming_flight.fa5,
                     "seats_sold":upcoming_flight.seats_sold
                     })