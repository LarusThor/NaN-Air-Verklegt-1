from dataclasses import dataclass


@dataclass
class Airplane:
    plane_insignia: str
    plane_type_id: str
    manufacturer: str
    model: str
    capacity: int
