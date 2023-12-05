class ScheduleIO():
    def __init__(self):
        pass
    
    def read_pilot(self):
        schedule_dict = {}
        with open("files/upcoming_flights.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                flight_nr, arr_at, licence = line.split(",")
                schedule_dict[flight_nr] = [arr_at, licence]

        return schedule_dict