from dataclasses import dataclass
from datetime import datetime

UNSTAFFED = 'N/A'
@dataclass
class PastVoyage:
    flight_id: str
    flight_nr: str
    dep_from: str
    arr_at: str
    departure: datetime
    arrival: datetime
    aircraft_id: str
    captain: str = UNSTAFFED
    copilot: str = UNSTAFFED
    fsm: str = UNSTAFFED
    fa1:str = UNSTAFFED
    fa2: str = UNSTAFFED
    fa3: str = UNSTAFFED
    fa4: str = UNSTAFFED
    fa5: str = UNSTAFFED
    seats_sold: str

#flight_nr,dep_from,arr_at,departure,arrival,aircraft_id,captain,copilot,fsm,fa1,fa2, seats_sold
