from dataclasses import dataclass

@dataclass
class Schedule:
    scheduledFlight: str
    scheduledEmployee: str
    scheduledDestination: str
    


#scheduledFlight -> upcoming_flights.csv -> flight_nr
#scheduledDestination -> upcoming_flights.csv -> arr_at
#scheduledEmployee past_flights = 


