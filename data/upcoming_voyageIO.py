import csv
from pathlib import Path
from model.upcoming_voyage_model import UpcomingVoyage
from datetime import datetime
from dataclasses import asdict


class UpcomingVoyageIO:
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
        file_path = Path('files/upcoming_flights.csv')

        with open(file_path, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['id','flight_nr', 'dep_from', 'arr_at', 'departure', 'arrival', 'aircraft_id', 'captain','copilot','fsm','fa1','fa2','fa3','fa4','fa5',"seats_sold"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(asdict(upcoming_voyage))
            

    def add_staff_to_voyage(self, added_staff_to_voyage: UpcomingVoyage) -> None:
        """ Updates voyage information to add staff to the voyage in the system. """
        voyage_list = self.read_upcoming_flights()

        for voyage_id, voyage in voyage_list.items():
            #if voyage_name == added_staff_to_voyage.id:
            if voyage_id == added_staff_to_voyage.id:    
                voyage_list[voyage_id] = added_staff_to_voyage
                break
        else:
            raise ValueError("Voyage does not exist")
        
        with open('files/upcoming_flights.csv', 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['id','flight_nr', 'dep_from', 'arr_at', 'departure', 'arrival', 'aircraft_id', 'captain','copilot','fsm','fa1','fa2','fa3','fa4','fa5',"seats_sold"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for voyage in voyage_list.values():
                writer.writerow(asdict(voyage))
                    #         ({'id': voyage.id,
                    # 'flight_nr': voyage.flight_nr, 
                    # 'dep_from': voyage.dep_from, 
                    # 'arr_at': voyage.arr_at, 
                    # 'departure': voyage.departure, 
                    # 'arrival': voyage.arrival, 
                    # 'captain': voyage.captain, 
                    # 'copilot': voyage.copilot,
                    # 'aircraft_id': 
                    # 'fsm': voyage.fsm, 
                    # 'fa1': voyage.fa1, 
                    # 'fa2': voyage.fa2, 
                    # 'fa3': voyage.fa3, 
                    # 'fa4':voyage.fa4, 
                    # 'fa5':voyage.fa5,
                    # 'seats_sold':voyage.seats_sold
                    #  })
    
   
    