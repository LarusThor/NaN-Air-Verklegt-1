import csv
from pathlib import Path
from model.past_voyage_model import PastVoyage
from datetime import datetime
from dataclasses import asdict

class PastVoyageIO:
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
