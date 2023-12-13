from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    social_id: str
    role: str
    rank: str
    licence: str
    email: str
    phonenumber: str
    home_address: str
    landline: str = "N/A"
