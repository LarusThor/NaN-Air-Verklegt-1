import csv
from model.destination_model import Destination

class DestinationIO():
    def __init__(self):
        pass


    def read_all_destinations(self):
        destination_list = []
        with open('files\destinations.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                destination_list.append(row)
        destination_names = []  # New list to store destination names
        for destination in destination_list:
            for key, value in destination.items():
                if key == 'destination':
                    destination_names.append(value)
        return destination_names
    
    def add_destination(self, destination):
        with open('files\destinations.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['id','destination', 'emergency_contact_name', 'emergency_contact_number', 'airport_name', 'distance_from_iceland']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'id': destination.destination_id, 'destination': destination.destination, 'emergency_contact_name': destination.emergencyContact, 'emergency_contact_number': destination.emergencyNumber, 'airport_name': destination.airportName, 'distance_from_iceland': destination.distanceFromIceland})
        


        
#destination_id -> destinations.csv -> id
#destination -> destinations.csv -> destination
#emergencyContact -> destinations.csv -> emergency_contact_name
#emergencyNumber -> destinations.csv -> emergency_contact_number
#airportName -> destinations.csv -> airport_name
#distanceFromIceland -> destinations.csv -> distance_from_iceland

'''destination_id, destination, emergencyContact, emergencyNumber, 
                 airportName, distanceFromIceland'''