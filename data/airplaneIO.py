import csv
from model.airplane_model import Airplane
from model.airplane_type_model import AirplaneType

class AirplaneIO:
    def aircraft_info(self) -> dict:
        """ Reads a csv file about the aircrafts and returns an aircraft dictionary. """
        airplane_dict = {}
        with open("files/aircraft.csv", "r", newline="", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                plane_insignia, plane_type_id, manufacturer, model, capacity = line.split(",")
                aircraft = Airplane(
                   plane_insignia=plane_insignia,
                   plane_type_id=plane_type_id,
                   manufacturer=manufacturer,
                   model=model,
                   capacity=int(capacity)
                )
                airplane_dict[plane_insignia] = aircraft
        
        return airplane_dict


    def airplane_types(self) -> list[AirplaneType]:
        """ Reads a csv file about airplane types and returns a list of airplane type models. """
        airplane_types = []

        with open("files/aircraft_type.csv", "r", newline="", encoding="utf-8") as f:
            lines = f.readlines()
            header_names = lines[0].strip().split(",")
            for line in lines[1:]:
                line = line.strip()
                values = line.split(",")
                args = {
                    argname: value 
                    for argname, value 
                    in zip(header_names, values)
                }
                airplane_types.append(AirplaneType(**args))
        
        return airplane_types



    def add_aircraft(self, aircraft) -> None:
        """ Adds an airplane to the system by writing it into the csv file about aircrafts. """
        with open("files/aircraft.csv", "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["plane_insignia", "plane_type_id", "manufacturer", "model", "capacity"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {"plane_insignia": aircraft.plane_insignia, 
                 "plane_type_id": aircraft.plane_type_id, 
                 "manufacturer": aircraft.manufacturer, 
                 "model": aircraft.model, 
                 "capacity": aircraft.capacity
                 })
