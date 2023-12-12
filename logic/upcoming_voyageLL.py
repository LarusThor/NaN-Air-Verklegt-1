from datetime import datetime, timedelta


class UpcomingVoyageLL:
    def __init__(self, logic_wrapper) -> None:
        self.logic = logic_wrapper


    def get_upcoming_voyages(self) -> dict:
        """ Returns a dictionary of all upcoming flights. """
        upcoming_flights_dict = self.logic.data_wrapper.get_upcoming_flights()
        return upcoming_flights_dict


    def add_upcoming_voyage(self, upcoming_voyage) -> None:
        """ Adds an upcoming voyage to the system. """
        self.logic.data_wrapper.add_upcoming_flights(upcoming_voyage)


    def calculate_flight_time(self, arr_at, departure_date_time) -> datetime:
        """ Calculates the flight time. """
        destinations_info = self.logic.data_wrapper.get_all_destinations_info()
        estimated_flight_time_overview = list(destinations_info.values())
        destination_values = destinations_info[arr_at]
        estimated_flight_time = destination_values.estimated_flight_time
        hour_duration, min_duration, sec_duration = estimated_flight_time.split(":")
        departure_date, departure_time = departure_date_time.split()
        hour, minute, sec = departure_time.split(":")
        year, month, day = departure_date.split("-")
        original_date_time = datetime(*map(int, [year, month, day, hour, minute, sec]))

        min_added = int(hour_duration) * 60 + int(min_duration)
        time_change = timedelta(minutes=min_added)
        arrival_time = original_date_time + time_change

        return arrival_time


    def valid_pilot(self, aircraft_id, pilot) -> bool:  # TF-XUP, 34928348392
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

    def add_staff_for_voyage(self, staff_to_add) -> None:
        """ Adds staff to a voyage. """
        return self.logic.data_wrapper.add_staff(staff_to_add)

    def aircraft_availability():
        pass


    def staff_availability():
        pass
