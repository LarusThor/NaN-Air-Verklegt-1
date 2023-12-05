class Destination:
    def __init__(self, destination, destinationDate, emergencyContact, emergencyNumber, 
                 airportName, estimatedFlightDuration, distanceFromIceland) -> str:
        self.destination = destination
        self.destinationDate = destinationDate
        self.emergencyContact = emergencyContact
        self.emergencyNumber = emergencyNumber
        self.airportName = airportName
        self.estimatedFlightDuration = estimatedFlightDuration
        self.distanceFromIceland = distanceFromIceland
    
#estimatedFlightDuration - > past_flights.csv -> (departure, arrival)
#destinationDate -> past_flights.csv -> (departure, arrival)
#destination -> destinations.csv -> destination
#emergencyContact -> destinations.csv -> emergency_contact_name
#emergencyNumber -> destinations.csv -> emergency_contact_number
#airportName -> destinations.csv -> airport_name
#distanceFromIceland -> destinations.csv -> distance_from_iceland