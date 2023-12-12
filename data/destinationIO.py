import csv
from model.destination_model import Destination

class DestinationIO():
    def __init__(self):
        pass
<<<<<<< HEAD
=======


    def read_destinations_info(self) -> dict:
        destinations_overview = {}
        with open("files/destinations.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                id,destination,emergency_contact_name,emergency_contact_number,airport_name,distance_from_iceland, estimated_flight_time = line.split(",")
                destination = Destination(id,destination,emergency_contact_name,emergency_contact_number,airport_name,distance_from_iceland, estimated_flight_time)
                destinations_overview[id] = destination

        return destinations_overview
>>>>>>> 5ad538937367e6ee823d8879e55681f0a586ee8f
    

    def read_all_destinations(self) -> list:
        dest_list = []
        with open('files/destinations.csv', 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
<<<<<<< HEAD
                dest_list.append(Destination(row["id"], row["destination"], row["emergency_contact_name"], row["emergency_contact_number"], row["airport_name"], row["distance_from_iceland"]))
            #id,destination,emergency_contact_name,emergency_contact_number,airport_name,distance_from_iceland
        return dest_list
=======
                dest_list.append(Destination(row["id"], row["destination"], row["emergency_contact_name"], row["emergency_contact_number"], row["airport_name"], row["distance_from_iceland"], row["estimated_flight_time"]))
            #id,destination,emergency_contact_name,emergency_contact_number,airport_name,distance_from_iceland, estimated_flight_time
            return dest_list
>>>>>>> 5ad538937367e6ee823d8879e55681f0a586ee8f


    def add_destination(self, destination) -> None:
        with open('files/destinations.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['id','destination', 'emergency_contact_name', 'emergency_contact_number', 'airport_name', 'distance_from_iceland','estimated_flight_time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

<<<<<<< HEAD
            writer.writerow({'id': destination.destination_id, 'destination': destination.destination, 'emergency_contact_name': destination.emergencyContact, 'emergency_contact_number': destination.emergencyNumber, 'airport_name': destination.airport_name, 'distance_from_iceland': destination.distanceFromIceland})
=======
            writer.writerow({'id': destination.destination_id, 'destination': destination.destination, 'emergency_contact_name': destination.emergency_contact_name, 'emergency_contact_number': destination.emergency_contact_number, 'airport_name': destination.airport_name, 'distance_from_iceland': destination.distance_from_iceland, 'estimated_flight_time': destination.estimated_flight_time})
>>>>>>> 5ad538937367e6ee823d8879e55681f0a586ee8f
        

    def update_destination(self, updated_destination) -> None:
        dest_list = self.read_all_destinations()

        for i, dest in enumerate(dest_list):
            if dest.destination_id == updated_destination.destination_id:
                dest_list[i] = updated_destination
                break
        
        with open('files/destinations.csv', 'w+', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['id','destination', 'emergency_contact_name', 'emergency_contact_number', 'airport_name', 'distance_from_iceland','estimated_flight_time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for destination in dest_list:
<<<<<<< HEAD
                writer.writerow({'id': destination.destination_id, 'destination': destination.destination, 'emergency_contact_name': destination.emergency_contact_name, 'emergency_contact_number': destination.emergency_contact_number, 'airport_name': destination.airport_name, 'distance_from_iceland': destination.distance_from_iceland})

    def update_contacts(self, updated_contacts):
        dest_list = self.read_all_destinations()

        for i, dest in enumerate(dest_list):
            if dest.destination_id == updated_contacts.destination_id:
                dest_list[i] = updated_contacts
                break
        
        with open('files/destinations.csv', 'w+', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['id','destination', 'emergency_contact_name', 'emergency_contact_number', 'airport_name', 'distance_from_iceland']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for destination in dest_list:
                writer.writerow({'id': destination.destination_id, 'destination': destination.destination, 'emergency_contact_name': destination.emergency_contact_name, 'emergency_contact_number': destination.emergency_contact_number, 'airport_name': destination.airport_name, 'distance_from_iceland': destination.distance_from_iceland})
        
#destination_id -> destinations.csv -> id
#destination -> destinations.csv -> destination
#emergencyContact -> destinations.csv -> emergency_contact_name
#emergencyNumber -> destinations.csv -> emergency_contact_number
#airportName -> destinations.csv -> airport_name
#distanceFromIceland -> destinations.csv -> distance_from_iceland

'''destination_id, destination, emergencyContact, emergencyNumber, 
                 airportName, distanceFromIceland'''
=======
                writer.writerow(
                    {
                    'id': destination.destination_id, 
                    'destination': destination.destination, 
                    'emergency_contact_name': destination.emergency_contact_name, 
                    'emergency_contact_number': destination.emergency_contact_number, 
                    'airport_name': destination.airport_name, 
                    'distance_from_iceland': destination.distance_from_iceland, 
                    'estimated_flight_time':destination.estimated_flight_time
                     })
        

    def write_destination(self, destination: list[Destination]):
        pass
        
>>>>>>> 5ad538937367e6ee823d8879e55681f0a586ee8f
