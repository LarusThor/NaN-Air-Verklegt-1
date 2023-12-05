from model.pilot_model import Pilot

class PilotIO:
    def __init__(self):
        pass
    
    def read_pilot(self):
        pilot_dict = {}
        with open("files/crew.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                nid, name, licence, phone_nr, email, licence, rank = line.split(",")
                pilot = Pilot(nid, name, licence, phone_nr, email, licence, rank)                
                pilot_dict[nid] = (pilot)

        return pilot_dict