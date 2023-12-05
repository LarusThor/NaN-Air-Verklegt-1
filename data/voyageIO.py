class VoyageIO():
    def __init__(self):
        pass
    
    
    def read_voyage(self):
        voyage_dict = {}
        with open("files/upcoming_flights.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                social_id, name, role, rank, licence, address, phone_nr, email = line.split(",")
                voyage_dict[social_id] = [name, role, rank, licence, address, phone_nr, email]

        return voyage_dict