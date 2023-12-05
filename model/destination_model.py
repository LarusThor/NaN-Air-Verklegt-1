class Destination:
    def __init__(self, destination_id, destination, emergencyContact, emergencyNumber, 
                 airportName, distanceFromIceland) -> str:
        self.destination_id = destination_id
        self.destination = destination
        self.emergencyContact = emergencyContact
        self.emergencyNumber = emergencyNumber
        self.airportName = airportName
        self.distanceFromIceland = distanceFromIceland
    
#destination_id -> destinations.csv -> id
#destination -> destinations.csv -> destination
#emergencyContact -> destinations.csv -> emergency_contact_name
#emergencyNumber -> destinations.csv -> emergency_contact_number
#airportName -> destinations.csv -> airport_name
#distanceFromIceland -> destinations.csv -> distance_from_iceland