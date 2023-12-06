class ScheduleIO():
    def __init__(self) -> None:
        pass
    
    def read_schedule(self) -> dict:
        schedule_dict = {}
        with open("files/upcoming_flights.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                flight_nr, arr_at,  = line.split(",")
                schedule_dict[flight_nr] = [arr_at]

        return schedule_dict
    
    def read_schedule(self) -> dict:
        schedule_dict = {}
        with open("files/past_flights.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                captain, copilot, fsm, fa1, fa2 = line.split(",")
                schedule_dict[captain] = [copilot,fsm,fa1,fa2]

        return schedule_dict
    