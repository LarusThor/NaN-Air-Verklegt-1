from dataclasses import dataclass

@dataclass
class Schedule:
    scheduled_flight: str
    scheduled_employee: str
    scheduled_destination: str
    


#scheduledFlight -> upcoming_flights.csv -> flight_nr
#scheduledDestination -> upcoming_flights.csv -> arr_at
#scheduledEmployee past_flights = captain/copilot/fsm/fa1/fa2


