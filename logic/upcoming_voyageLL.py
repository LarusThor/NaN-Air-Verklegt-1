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
                
    def detect_voyage_info_return_flight(self, voyage_flight_number: str, voyage_date: str): #TODO: typehint, mögulega skila sem lista
        flight_info = self.logic.upcoming_voyages()
        for key, item in flight_info.items():
            # for id_key, some in key: #1, (UPcomingVoyage(id=1, flight=Na021))
            if voyage_flight_number == item.flight_nr and voyage_date in item.departure.strftime("%Y-%m-%d %H:%M:%S"):
                id_of_flight = key
        return_flight_id = int(id_of_flight) + 1
        return_flight_values = flight_info[str(return_flight_id)] 
        return_flight_id = return_flight_values.id
        return_flight_number = return_flight_values.flight_nr
        return_flight_dep_from = return_flight_values.dep_from
        return_flight_arr_at = return_flight_values.arr_at
        return_flight_date_departure = return_flight_values.departure
        return_flight_arrival = return_flight_values.arrival
        return return_flight_id, return_flight_number, return_flight_dep_from, return_flight_arr_at, return_flight_date_departure, return_flight_arrival 

    def add_staff_for_voyage(self, staff_to_add: str) -> None:
        """ Adds staff to a voyage. """
        return self.logic.data_wrapper.add_staff(staff_to_add)
    

    def aircraft_availability(self, plane_insignia: Airplane, start: datetime, end: datetime):
        total_hours_flown = self.logic.get_total_future_hours_for_airplane(plane_insignia, start, end)
        return total_hours_flown

    def staff_availability(self, captain: Employee, departure: date, return_flight_arrival: date) -> int:
        """ Checks wether an employee is scheduled to work during a specified time period. """
        total_hours_worked = self.logic.get_total_future_hours_worked(captain, departure, return_flight_arrival)
        return total_hours_worked

    
    def captain_availability(self, captain:str, employee_information:dict, plane_insignia:str, employee:dict, voyages_info:dict, return_flight_arrival:str) -> bool:
        """ Takes captains social id, info about the employee, a specific airplanes insignia or id, 
        a specific instance of an employee, voyages information which checks departure time and time of return flights arrival """
        available_for_date = True
        valid_license = True
        valid_rank = True
        employee_information = self.logic.show_employee_info()
        if employee_information[captain].rank == "Captain":
            if self.logic.check_pilot_qualifications(plane_insignia, captain):
                if self.logic.staff_availability_check(employee, voyages_info.departure, return_flight_arrival) == 0:
                    available_for_date = True  
                    valid_license = True 
                    valid_rank = True
                else:
                    available_for_date = False
            else:
                valid_license = False
        else:
            valid_rank = False
        return valid_rank, available_for_date, valid_license
    

    def copilot_availability(self, copilot:str, employee_information:dict, plane_insignia:str, employee:dict, voyages_info:dict, return_flight_arrival:str) -> bool:
        """ Takes copilot social id, info about the employee, a specific airplanes insignia or id, 
        a specific instance of an employee, voyages information which checks departure time and time of return flights arrival """
        employee_information = self.logic.show_employee_info()
        if employee_information[copilot].rank == "Copilot":
            if self.logic.check_pilot_qualifications(plane_insignia, copilot):
                if self.logic.staff_availability_check(employee, voyages_info.departure, return_flight_arrival) == 0:
                    available_for_date = True  
                    valid_license = True 
                    valid_rank = True
                else:
                    available_for_date = False
            else:
                valid_license = False
        else:
            valid_rank = False
        return valid_rank, available_for_date, valid_license
        
    
    def flight_service_manager_availability(self, flight_service_manager:str, employee_information:dict, employee:dict, voyages_info:dict, return_flight_arrival:str) -> bool:
        """  Takes flight service manager social id, info about the employee, a specific instance of an employee, 
        voyages information which checks departure time and time of return flights arrival """
        employee_information = self.logic.show_employee_info()
        if employee_information[flight_service_manager].rank == "Flight Service Manager":
            if self.logic.staff_availability_check(employee, voyages_info.departure, return_flight_arrival) == 0:
                available_for_date = True  
                valid_rank = True
            else:
                available_for_date = False
        else:
            valid_rank = False
        return valid_rank, available_for_date
          
