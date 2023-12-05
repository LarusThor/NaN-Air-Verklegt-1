class Airplane:
    def __init__(self, airplaneID, airplaneManufacturer, airplaneType, airplaneCapacity, airplaneInsignia ,airplaneUsage,airplaneTotalFlightTime) -> str:
        self.airplaneID = airplaneID
        self.airplaneManufacturer = airplaneManufacturer
        self.airplaneType = airplaneType
        self.airplaneInsignia = airplaneInsignia
        self.airplaneCapacity = airplaneCapacity
        self.airplaneUsage = airplaneUsage
        self.airplaneTotalFlightTime = airplaneTotalFlightTime

#airplaneID -> aircraft_type.csv -> plane_type_id
#airplaneManufacturer -> aircraft_type.csv -> manufacturer
#airplaneType -> aircraft_type.csv -> model
#airplaneInsignia -> aircraft.csv -> plane_insignia
#airplaneCapacity -> aircraft_type.csv -> capacity
#airplaneUsage -> past_flights.csv -> (aircraft_id)
#airplaneTotalFlightTime -> past_flights.csv -> (departure, arrival)
