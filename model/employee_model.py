class Employee:
    def __init__(self, name, socialID, role, rank, license, email, phonenumber, home_address) -> str:
        self.name = name
        self.socialID = socialID
        self.role = role
        self.rank = rank
        self.license = license
        self.email = email
        self.phonenumber = phonenumber
        self.home_address = home_address
#name -> crew.csv -> name
#socialID -> crew.csv -> nid
#email -> crew.csv -> email
#phonenumber -> crew.csv -> phone_nr
#landline is optional
#home_address -> crew.csv -> 

#nid,name,role,rank,licence,address,phone_nr, email