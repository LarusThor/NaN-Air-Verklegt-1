from dataclasses import dataclass

@dataclass
class Destination:
    destination_id: str
    destination: str
    emergency_contact: str
    emergency_number: str
    airport_name: str
    distance_from_iceland: str
        
    
#destination_id -> destinations.csv -> id
#destination -> destinations.csv -> destination
#emergencyContact -> destinations.csv -> emergency_contact_name
#emergencyNumber -> destinations.csv -> emergency_contact_number
#airportName -> destinations.csv -> airport_name
#distanceFromIceland -> destinations.csv -> distance_from_iceland

