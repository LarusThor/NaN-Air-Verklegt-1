import csv
from pathlib import Path
from model.past_voyage_model import PastVoyage

class PastVoyageIO:

    def __init__(self):
        pass

    def read_past_flights(self):
        past_flights_dict = {}
        with open("files/past_flights.csv", "r", newline='', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                flight_nr, dep_from, arr_at, departure, arrival, aircraft_id, captain, copilot, fsm, fa1, fa2, fa3, fa4, fa5, seats_sold = line.split(",")
                past_flight = PastVoyage(flight_nr, dep_from, arr_at, departure, arrival, aircraft_id, captain, copilot, fsm, fa1, fa2, fa3, fa4, fa5, seats_sold)
                past_flights_dict[flight_nr] = (past_flight)

        return past_flights_dict
    
    def add_past_voyage(self, past_flights):
        file_path = Path('files/past_flights.csv')

        fieldnames = ['flight_nr', 'dep_from', 'arr_at', 'departure', 'arrival', 'captain','copilot','fsm','fa1','fa2','fa3','fa4','fa5']

        with open(file_path, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for upcoming_flight in past_flights:
                writer.writerow({'flight_nr': upcoming_flight.flight_nr, 'dep_from': upcoming_flight.dep_from, 'arr_at': upcoming_flight.arr_at, 'departure': upcoming_flight.departure, 'arrival': upcoming_flight.arrival, 
                                 'captain': upcoming_flight.captain, 'copilot': upcoming_flight.copilot, 'fsm': upcoming_flight.fsm, 'fa1': upcoming_flight.fa1, 'fa2': upcoming_flight.fa2, 'fa3': upcoming_flight.fa3, 'fa4':upcoming_flight.fa4, 'fa5':upcoming_flight.fa5})


        #  with open('files/upcoming_flights.csv', 'a', newline='', encoding="utf-8") as csvfile:
        #     fieldnames = ['flight_nr','dep_from','arr_at','departure','arrival','captain','copilot','fsm','fa1','fa2','fa3','fa4','fa5']
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #     writer.writerow(past_flight)

#flight_nr,dep_from,arr_at,departure,arrival,aircraft_id,captain,copilot,fsm,fa1,fa2, fa3, fa4, fa5, seats_sold