from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    socialID: str
    role: str
    rank: str
    license: str
    email: str
    phonenumber: str
    home_address: str
    landline: str | None

#name -> crew.csv -> name
#socialID -> crew.csv -> nid
#email -> crew.csv -> email
#phonenumber -> crew.csv -> phone_nr
#landline is optional
#home_address -> crew.csv -> 

#nid,name,role,rank,licence,address,phone_nr, email