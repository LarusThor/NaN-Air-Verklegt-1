from dataclasses import dataclass

# TODO: convert to snake_case

@dataclass
class Airplane:
    plane_insignia: str
    plane_type_id: str
    manufacturer: str
    model: str
    capacity: int

    # TODO: make methods to get usage and total flight time
    #airplaneUsage -> past_flights.csv -> (aircraft_id)
    #airplaneTotalFlightTime -> past_flights.csv -> (departure, arrival)
    # maybe this should be in logic layer instead though?

