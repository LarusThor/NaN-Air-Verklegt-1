from data.data_wrapper import DataWrapper
from itertools import chain
from logic.employeeLL import EmployeeLL

class AirplaneLL():
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        self.emlployees = EmployeeLL()
        self.airplane_list = self.data_wrapper.get_airplanes()
        self.airplane_types = self.data_wrapper.get_airplane_types()
        self.past_voyage_list = self.data_wrapper.get_past_flights()
        self.upcoming_voyage_list = self.data_wrapper.get_upcoming_flights() #TODO: tengja frekar við hinn logic?
        self.pilots = self.emlployees.get_all_pilots()

    def get_most_used_plane(self):
        """ Returns the most used plane. """
        pass
   
    def get_furthest_flown_plane(self):
        """ Returns the plane that has flown the furthest"""
        pass
   
    def get_plane_gone_on_most_voyages(self): #laga nafn omg
        """ Returns the plane that has gone on the most voyages. """
        pass
   
    def get_all_airplane_types(self):
        """ Returns a list of all the airplane types in the system. """
        airplane_types = self.airplane_types
        type_set = set()
        for plane in airplane_types:
            type_set.update([plane.plane_type_id])

        return type_set

    def get_airplane_status_by_date_time(self): #laga þetta nafn líka
        """ Returns the status of a plane on a given day and time. """
        pass
   
    def get_airplane_usage(self):
        """ Returns the total number of voyages for a specific plane. """
        #TODO: laga, erum ekki að fá allan listan, bara 52 ferðir
        airplane_list = []
        airplane_dict = {}

        all_voyages = list(chain(
            self.upcoming_voyage_list.values(), 
            self.past_voyage_list.values()
        ))

        for voyage in all_voyages:
            if voyage.aircraft_id != "N/A":
                airplane_list.append(voyage.aircraft_id)

        for destination in airplane_list:
            counter = (airplane_list.count(destination))//2
            airplane_dict[destination] = counter
        most_popular = max(set(airplane_list), key=airplane_list.count)
        #TODO: finna út hvernig ég raða listan í stærðarröð út frá dicts
        return most_popular, airplane_dict
          
    
    def add_airplane(self, airplane):
        """ Adds airplane to the system. """
        self.data_wrapper.add_airplane(airplane)

    def pilots_by_license(self):
        pilots_by_license = dict()
        pilots = self.pilots

        for pilot in pilots:
            license_key = pilot.licence
            pilot_name = pilot.name

            if license_key in pilots_by_license:
                pilots_by_license[license_key].append(pilot_name)
            else:
                pilots_by_license[license_key] = [pilot_name]

        print(pilots_by_license)
