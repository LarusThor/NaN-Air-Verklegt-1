import csv
from pathlib import Path
from model.upcoming_voyage_model import UpcomingVoyage
from datetime import datetime


class UpcomingVoyageIO:
    def __init__(self):
        pass


    def read_upcoming_flights(self) -> dict[str, UpcomingVoyage]:
        """ Returns a dictionary of all upcoming fligths from the csv file. """
        upcoming_flights_dict = {}
        with open("files/upcoming_flights.csv", "r", newline='', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                id, flight_nr, dep_from, arr_at, departure, arrival, aircraft_id, captain, copilot, fsm, fa1, fa2, fa3, fa4, fa5, seats_sold = line.split(",")
                
                upcoming_flight = UpcomingVoyage(id, flight_nr, dep_from, arr_at, datetime.strptime(departure, "%Y-%m-%d %H:%M:%S"), datetime.strptime(arrival, "%Y-%m-%d %H:%M:%S"),aircraft_id, captain, copilot, fsm, fa1, fa2, fa3, fa4, fa5, seats_sold)
                upcoming_flights_dict[id] = upcoming_flight

        return upcoming_flights_dict
    

    def add_upcoming_voyage(self, upcoming_voyage) -> None:
        """ Adds an upcoming voyage to the system. """
        print("saving_files")
        file_path = Path('files/upcoming_flights.csv')

        with open(file_path, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['id','flight_nr', 'dep_from', 'arr_at', 'departure', 'arrival', 'aircraft_id', 'captain','copilot','fsm','fa1','fa2','fa3','fa4','fa5',"seats_sold"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                'id': upcoming_voyage.id, 
                'flight_nr': upcoming_voyage.flight_nr, 
                'dep_from': upcoming_voyage.dep_from, 
                'arr_at': upcoming_voyage.arr_at, 
                'departure': upcoming_voyage.departure, 
                'arrival': upcoming_voyage.arrival, 
                'aircraft_id': upcoming_voyage.aircraft_id,
                'captain': upcoming_voyage.captain, 
                'copilot': upcoming_voyage.copilot, 
                "seats_sold": upcoming_voyage.seats_sold,
                'fsm': upcoming_voyage.fsm, 
                'fa1': upcoming_voyage.fa1, 
                'fa2': upcoming_voyage.fa2, 
                'fa3': upcoming_voyage.fa3, 
                'fa4':upcoming_voyage.fa4, 
                'fa5':upcoming_voyage.fa5
                })
            