import csv
from model.past_flight_model import pastFlight

class pastFlightsIO:

    def __init__(self):
        pass

    def read_past_flights(self):
        past_flights_dict = {}
        with open("files/past_flights.csv", "r", newline='', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                flight_nr, dep_from, arr_at, departure, arrival, aircraft_id, captain, copilot, fsm, fa1, fa2, fa3, fa4, fa5, seats_sold = line.split(",")
                past_flight = pastFlight(flight_nr, dep_from, arr_at, departure, arrival, aircraft_id, captain, copilot, fsm, fa1, fa2, fa3, fa4, fa5, seats_sold)
                past_flights_dict[flight_nr] = (past_flight)

        return past_flights_dict
    
#flight_nr,dep_from,arr_at,departure,arrival,aircraft_id,captain,copilot,fsm,fa1,fa2, fa3, fa4, fa5, seats_sold