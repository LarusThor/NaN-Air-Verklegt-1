import csv
from model.airplane_model import Airplane

class AirplaneIO:
    def __init__(self):
        pass  
    
    def aircraft_info(self):
        airplane_dict = {}
        with open("files/aircraft.csv", "r", newline='', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                plane_insignia, plane_type_id, date_of_manufacture, last_maintenance = line.split(",")
                aircraft = Airplane(plane_insignia, plane_type_id, date_of_manufacture, last_maintenance)
                airplane_dict[plane_insignia] = (aircraft)
    
    def aircraft_types(self):
        aircraft_types_dict = {}
        with open("files/aircraft.csv", "r", newline='', encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                plane_type_id, manufacturer, model, capacity = line.split(",")
                aircraft_type = Airplane(plane_type_id, manufacturer, model, capacity)
                aircraft_types_dict[plane_type_id] = (aircraft_type)        
    
    def add_aircraft(self, aircraft):
        with open('files/upcoming_flights.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['flight_nr','dep_from','arr_at','departure','arrival','captain','copilot','fsm','fa1','fa2','fa3','fa4','fa5']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(aircraft)
