from dataclasses import dataclass
from datetime import datetime

@dataclass
class PastVoyage:
    flight_id: str
    flight_nr: str
    dep_from: str
    arr_at: str
    departure: datetime
    arrival: datetime
    aircraft_id: str
    captain: str
    copilot: str
    fsm: str
    fa1:str
    fa2: str
    fa3: str
    fa4: str
    fa5: str
    seats_sold: str

#flight_nr,dep_from,arr_at,departure,arrival,aircraft_id,captain,copilot,fsm,fa1,fa2, seats_sold
