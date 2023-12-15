from datetime import datetime, timedelta
from model.employee_model import Employee
from datetime import date, timedelta
from model.upcoming_voyage_model import UpcomingVoyage
from model.airplane_model import Airplane
from model.destination_model import Destination


class UpcomingVoyageLL:
    def __init__(self, logic_wrapper) -> None:
        """Instantiate a UpcomingVoyageLL object.

        Args:
            logic_wrapper: The logic wrapper object that contains all logic layer objects.
        """
        self.logic = logic_wrapper


    def get_upcoming_voyages(self) -> dict:
        """ Returns a dictionary of all upcoming flights. """
        upcoming_flights_dict = self.logic.data_wrapper.get_upcoming_flights()
        return upcoming_flights_dict


    def add_upcoming_voyage(self, upcoming_voyage: UpcomingVoyage) -> None:
        """ Adds an upcoming voyage to the system. """
        self.logic.data_wrapper.add_upcoming_flights(upcoming_voyage)


    def calculate_flight_time(self, arr_at: Destination, departure_date_time: datetime) -> datetime: #TODO: change name to calculate arrival time
        """ Calculates the flight time. """

        estimated_flight_time_str = arr_at.estimated_flight_time.strip()
        estimated_flight_time_delta = datetime.strptime(estimated_flight_time_str, "%H:%M:%S").time()

        arrival = departure_date_time + timedelta(
            hours=estimated_flight_time_delta.hour,
            minutes=estimated_flight_time_delta.minute,
            seconds=estimated_flight_time_delta.second
        )

        return arrival


    def valid_pilot(self, aircraft_id: str, pilot: str) -> bool:  # TF-XUP, 34928348392
        """ Checks if pilot is valid to fly the voyage. """
        pilots_by_license = self.logic.pilots_by_license()  # {Fokkerf100: jón, kalli}
        planes_by_type = (self.logic.airplane_insignia_by_types())  # {Fokkerf100: TF-XZ, TF-XUP}
        employee_dict = (self.logic.data_wrapper.get_all_staff_members())  # {293919999: Jón, Pilot...}
        for employee, value in employee_dict.items():  # 36585298, [(djxhfj)]
            if employee == pilot and value.role == "Pilot":
                # pilot_info = list(employee_dict) # ["74284353454", "jon", "pilot", ... ]
                pilot_name = value.name  # Jón Jóns.

        for key, value in planes_by_type.items():  # Fokkerf100, (jón, kalli)
            if aircraft_id in planes_by_type[key]:
                license_check = key
                if pilot_name in pilots_by_license[license_check]:
                #license_check in pilots_by_license.keys() and pilot_name in pilots_by_license.values():
                    return True
                
    def detect_voyage_info_return_flight(self, voyage_flight_number: str, voyage_date: str) -> UpcomingVoyage: #TODO: typehint, mögulega skila sem lista
        flight_info = self.logic.upcoming_voyages()
        for key, item in flight_info.items():
            # for id_key, some in key: #1, (UPcomingVoyage(id=1, flight=Na021))
            if voyage_flight_number == item.flight_nr and voyage_date in item.departure.strftime("%Y-%m-%d %H:%M:%S"):
                id_of_flight = key

        return_flight_id = int(id_of_flight) + 1
        return flight_info[str(return_flight_id)]
    
    def get_voyage_by_flight_nr_and_date(self, flight_nr: str, departure_date: str) -> UpcomingVoyage:
        voyages = self.logic.data_wrapper.get_upcoming_flights()

        for voyage in voyages.values():
            if voyage.flight_nr == flight_nr and voyage.departure.strftime("%Y-%m-%d") == departure_date:
                return voyage

        raise ValueError("Voyage not found")


    def add_staff_for_voyage(self, staff_to_add: str) -> None:
        """ Adds staff to a voyage. """
        return self.logic.data_wrapper.add_staff(staff_to_add)
    
