from dataclasses import dataclass

@dataclass
class PastVoyage:
    flight_nr: str
    dep_from: str
    arr_at: str
    departure: str
    arrival: str
    aircraft_id: str
    captain: str
    copilot: str
    fsm: str
    fa1:str
    fa2: str
    fa3: str
    fa4: str
    fa5: str

#flight_nr,dep_from,arr_at,departure,arrival,aircraft_id,captain,copilot,fsm,fa1,fa2, seats_sold