class PilotIO():
    def __init__():
        pass
    
    def read_pilot(self):
        pilot_dict = {}
        with open("files/crew.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                nid, name, licence, phone_nr, email, licence, rank = line.split(",")
                pilot_dict[nid] = [name, licence, phone_nr, email, licence, rank]

        return pilot_dict