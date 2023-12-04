class AirplaneIO:
    def __init__(self):
        pass  

    def read_airplane(self):
        airplane_dict = {}
        with open("files/aircraft.csv", "r") as f:
            for line in lines[1:]:
                line = line.strip()
                plane_insignia, plane_type_id, date_of_manufacture, last_maintenance = line.split(",")
                airplane_dict[plane_insignia] = [plane_type_id, date_of_manufacture, last_maintenance]
        return airplane_dict