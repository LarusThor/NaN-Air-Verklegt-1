from dataclasses import dataclass

@dataclass
class Airplane:
    airplaneID: str
    airplaneManufacturer: str
    airplaneType: str
    airplaneCapacity: str
    airplaneInsignia: str
    airplaneUsage: str
    airplaneTotalFlightTime: str
        

#airplaneID -> aircraft_type.csv -> plane_type_id
#airplaneManufacturer -> aircraft_type.csv -> manufacturer
#airplaneType -> aircraft_type.csv -> model
#airplaneInsignia -> aircraft.csv -> plane_insignia
#airplaneCapacity -> aircraft_type.csv -> capacity
#airplaneUsage -> past_flights.csv -> (aircraft_id)
#airplaneTotalFlightTime -> past_flights.csv -> (departure, arrival)
