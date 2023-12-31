from itertools import chain
from collections import defaultdict
from datetime import datetime
from model.airplane_model import Airplane
from collections import defaultdict


class AirplaneLL:
    def __init__(self, logic_wrapper) -> None:
        """Instantiate a AirplaneLL object.

        Args:
            logic_wrapper: The logic wrapper object that contains all logic layer objects.
        """
        self.logic = logic_wrapper

    def get_airplanes_info_overview(self, plane_insignia: str) -> dict:
        """Returns a dictionary containing information about every airplane in the system"""
        airplane_dict = self.logic.data_wrapper.get_airplanes()

        return airplane_dict[plane_insignia]

    def get_furthest_flown_plane(self) -> tuple[str, int]:
        """Returns the plane that has flown the furthest"""
        past_voyage_list = self.logic.data_wrapper.get_past_flights()
        destination_distance = self.logic.distance_from_iceland()

        distance_dict = defaultdict(int)

        for voyage in past_voyage_list.values():
            destination = voyage.arr_at
            dep_from = voyage.dep_from

            distance = (
                destination_distance[destination] + destination_distance[dep_from]
            )

            distance_dict[voyage.aircraft_id] += distance

        furthest_flown_plane = None
        furthest_distance = -1

        for plane, distance in distance_dict.items():
            if distance > furthest_distance:
                furthest_flown_plane = plane
                furthest_distance = distance

        return furthest_flown_plane, furthest_distance

    def get_all_airplane_types(self) -> set:
        """Returns a list of all the airplane types in the system."""
        airplane_types = self.logic.data_wrapper.get_airplane_types()
        type_set = set()
        for plane in airplane_types:
            type_set.update(
                [(plane.plane_type_id, plane.manufacturer, plane.model, plane.capacity)]
            )

        return type_set

    def get_airplane_usage(self) -> tuple[str, dict]:
        """Returns the total number of voyages for a specific plane."""
        past_voyage_list = self.logic.data_wrapper.get_past_flights()
        upcoming_voyage_list = self.logic.data_wrapper.get_upcoming_flights()
        airplane_list = []
        airplane_dict = {}

        all_voyages = list(
            chain(upcoming_voyage_list.values(), past_voyage_list.values())
        )

        for voyage in all_voyages:
            if voyage.aircraft_id != "N/A":
                airplane_list.append(voyage.aircraft_id)

        for destination in airplane_list:
            counter = (airplane_list.count(destination)) // 2
            airplane_dict[destination] = counter
        most_popular = max(set(airplane_list), key=airplane_list.count)

        return most_popular, airplane_dict

    def add_airplane(self, airplane: Airplane) -> None:
        """Adds airplane to the system."""
        self.logic.data_wrapper.add_airplane(airplane)

    def pilots_by_license(self) -> dict:
        """Returns a dictionary where the key is the airplane type and the value is a list of
        all licenced pilots for that airplane type."""
        pilots_by_license = dict()
        pilots = self.logic.pilot_list()

        for pilot in pilots:
            license_key = pilot.licence
            pilot_name = pilot.name

            if license_key in pilots_by_license:
                pilots_by_license[license_key].append(pilot_name)
            else:
                pilots_by_license[license_key] = [pilot_name]

        return pilots_by_license

    def get_total_future_hours_for_airplane(self, airplane: Airplane, start: datetime, end: datetime) -> float:
        """Takes an instance of the model class Airplane, start time, and end as datetime and
        returns total hours an employee has worked."""
        total_hours_flown = 0
        upcoming_voyage_dict = self.logic.upcoming_voyages()

        for flight in upcoming_voyage_dict.values():
            workers = [
                flight.captain,
                flight.copilot,
                flight.fsm,
                flight.fa1,
                flight.fa2,
                flight.fa3,
                flight.fa4,
                flight.fa5,
            ]

            if airplane.plane_insignia not in workers:
                continue

            arrival = flight.arrival
            departure = flight.departure

            if arrival > end or departure < start:
                continue

            if arrival > end:
                arrival = end

            if departure < start:
                departure = start

            flown_hours = (arrival - departure).total_seconds() / 3600

            total_hours_flown += flown_hours

        return total_hours_flown

    def get_available_airplanes_over_period(self, period_start: datetime, period_end: datetime) -> list[Airplane]:
        """Returns a list of all airplanes that are available over a given period.

        Args:
            period_start: Start of the period.
            period_end: End of the period.
        """

        plane_voyages = defaultdict(list)
        for voyage in self.logic.upcoming_voyages().values():
            plane_voyages[voyage.aircraft_id].append(voyage)

        available_planes = []
        for airplane in self.logic.data_wrapper.get_airplanes().values():
            for voyage in plane_voyages[airplane.plane_insignia]:
                if voyage.departure <= period_end and voyage.arrival >= period_start:
                    # plane is not available
                    break
            else:
                available_planes.append(airplane)
        return available_planes

    def airplane_insignia_by_type(self) -> dict:
        """Dictionary which sorts airplanes in use by their types"""
        airplane_list = self.logic.data_wrapper.get_airplanes()
        airplane_insignia_by_type_dict = dict()

        for plane in airplane_list.values():
            insignia = plane.plane_insignia
            plane_type = plane.plane_type_id
            if plane_type in airplane_insignia_by_type_dict:
                airplane_insignia_by_type_dict[plane_type].append(insignia)
            else:
                airplane_insignia_by_type_dict[plane_type] = [insignia]

        return airplane_insignia_by_type_dict
