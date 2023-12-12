import csv
from model.destination_model import Destination

class DestinationIO():
    def __init__(self):
        pass


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
    

    def read_all_destinations(self) -> list:
        dest_list = []
        with open('files/destinations.csv', 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dest_list.append(Destination(row["id"], row["destination"], row["emergency_contact_name"], row["emergency_contact_number"], row["airport_name"], row["distance_from_iceland"], row["estimated_flight_time"]))
            #id,destination,emergency_contact_name,emergency_contact_number,airport_name,distance_from_iceland, estimated_flight_time
            return dest_list


    def add_destination(self, destination) -> None:
        with open('files/destinations.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['id','destination', 'emergency_contact_name', 'emergency_contact_number', 'airport_name', 'distance_from_iceland','estimated_flight_time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'id': destination.destination_id, 'destination': destination.destination, 'emergency_contact_name': destination.emergency_contact_name, 'emergency_contact_number': destination.emergency_contact_number, 'airport_name': destination.airport_name, 'distance_from_iceland': destination.distance_from_iceland, 'estimated_flight_time': destination.estimated_flight_time})
        

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
                writer.writerow(
                    {'id': destination.destination_id, 
                     'destination': destination.destination, 
                     'emergency_contact_name': destination.emergency_contact_name, 
                     'emergency_contact_number': destination.emergency_contact_number, 
                     'airport_name': destination.airport_name, 
                     'distance_from_iceland': destination.distance_from_iceland, 
                     'estimated_flight_time':destination.estimated_flight_time
                     })
        

    def write_destination(self, destination: list[Destination]):
        pass
        