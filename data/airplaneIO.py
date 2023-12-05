class AirplaneIO:
    def __init__(self):
        pass  

    def aircraft_info(self):
        airplane_list = []
        with open("files/aircraft.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                plane_insignia, plane_type_id, date_of_manufacture, last_maintenance = line.split(",")
                airplane_list.append([plane_insignia, plane_type_id, date_of_manufacture, last_maintenance])
        return airplane_list
    
    def aircraft_types(self):
        aircraft_types_list = []
        with open("files/aircraft_type.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                plane_type_id, manufacturer, model, capacity = line.split(",")
                aircraft_types_list.append([plane_type_id, manufacturer, model, capacity])
        return aircraft_types_list
