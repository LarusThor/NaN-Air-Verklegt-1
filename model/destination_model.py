from dataclasses import dataclass


@dataclass
class Destination:
    destination_id: str
    destination: str
    emergency_contact_name: str
    emergency_contact_number: str
    airport_name: str
    distance_from_iceland: str
    estimated_flight_time: str
