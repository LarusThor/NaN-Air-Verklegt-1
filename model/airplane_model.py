from dataclasses import dataclass

# TODO: convert to snake_case

@dataclass
class Airplane:
    plane_insignia: str
    plane_type_id: str
    manufacturer: str
    model: str
    capacity: int
