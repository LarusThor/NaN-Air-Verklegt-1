from dataclasses import dataclass

@dataclass
class UpcomingFlight:
    flight_nr: str
    dep_from: str
    arr_at: str
    departure: str
    arrival: str

#flight_nr,dep_from,arr_at,departure,arrival
