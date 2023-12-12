from dataclasses import dataclass


@dataclass
class AirplaneType:
    plane_type_id: str
    manufacturer: str
    model: str
    capacity: int
    empty_weight: int
    max_takeoff_weight: int
    unit_thrust: float
    service_ceiling: int
    length: float
    height: float
    wingspan: float