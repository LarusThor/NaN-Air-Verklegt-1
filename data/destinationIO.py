import csv

from model.destination_model import Destination

class DestinationIO():
    def __init__(self):
        pass


    def read_destination(self):
        destination_dict = {}
        with open("files/destinations.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                destination_id, destination_name,  emergency_contact, emergency_number, airport_name, distance_from_iceland = line.split(",")
                destination = Destination(destination_id, destination_name, emergency_contact, emergency_number, airport_name, distance_from_iceland)
                destination_dict[destination_id] = (destination)

        return destination_dict

        
#destination_id -> destinations.csv -> id
#destination -> destinations.csv -> destination
#emergencyContact -> destinations.csv -> emergency_contact_name
#emergencyNumber -> destinations.csv -> emergency_contact_number
#airportName -> destinations.csv -> airport_name
#distanceFromIceland -> destinations.csv -> distance_from_iceland

