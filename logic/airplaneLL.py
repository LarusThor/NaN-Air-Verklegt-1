from data.data_wrapper import DataWrapper
from itertools import chain

class AirplaneLL():
    def __init__(self, logic_wrapper) -> None:
        self.data_wrapper = DataWrapper()
        self.logic = logic_wrapper
        #self.emlployees = EmployeeLL()
        #self.airplane_list = self.data_wxrapper.get_airplanes()
        #self.airplane_types = self.data_wrapper.get_airplane_types()
        #self.past_voyage_list = self.data_wrapper.get_past_flights()
        #self.upcoming_voyage_list = self.data_wrapper.get_upcoming_flights() #TODO: tengja frekar við hinn logic?
        #self.pilots = self.emlployees.get_all_pilots()
   
    def get_furthest_flown_plane(self):
        """ Returns the plane that has flown the furthest"""
        past_voyage_list = self.data_wrapper.get_past_flights() #TODO: tékka hvort það sé hægt að tengja í logic wrapper frekar
        destination_distance = self.logic.distance_from_iceland()
        print(destination_distance)
        distance_dict = dict()


        for voyage in past_voyage_list.values():
            print(voyage.arr_at)
            #distance_dict[voyage.destination] = 9

        return distance_dict


        #for destination in destination_distance.items():
            #print(destination)
        # airplane_list = []
        # airplane_dict = {}


        # for voyage in all_voyages:
        #     if voyage.aircraft_id != "N/A":
        #         airplane_list.append(voyage.aircraft_id)

        # for destination in airplane_list:
        #     counter = (airplane_list.count(destination))//2
        #     airplane_dict[destination] = counter
        # most_popular = max(set(airplane_list), key=airplane_list.count)
        # #TODO: finna út hvernig ég raða listan í stærðarröð út frá dicts
        # return most_popular, airplane_dict
   
    def get_all_airplane_types(self):
        """ Returns a list of all the airplane types in the system. """
        airplane_types = self.data_wrapper.get_airplane_types()
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
        past_voyage_list = self.data_wrapper.get_past_flights()
        upcoming_voyage_list = self.data_wrapper.get_upcoming_flights()
        airplane_list = []
        airplane_dict = {}

        all_voyages = list(chain(
            upcoming_voyage_list.values(), 
            past_voyage_list.values()
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
        """ Returns a dictionary where the key is the airplane type and the value is a list of
          all licenced pilots for that airplane type. """
        pilots_by_license = dict()
        pilots = self.emlployees.get_all_pilots()

        for pilot in pilots:
            license_key = pilot.licence
            pilot_name = pilot.name

            if license_key in pilots_by_license:
                pilots_by_license[license_key].append(pilot_name)
            else:
                pilots_by_license[license_key] = [pilot_name]

        return pilots_by_license
    
    def airplane_insignia_by_type(self):
        """ Dictionary which sorts airplanes in use by their types """
        airplane_list = self.data_wrapper.get_airplanes()
        airplane_insignia_by_type_dict = dict()

        for plane in airplane_list.values():
            insignia = plane.plane_insignia
            plane_type = plane.plane_type_id
            if plane_type in airplane_insignia_by_type_dict:
                airplane_insignia_by_type_dict[plane_type].append(insignia)
            else:
                airplane_insignia_by_type_dict[plane_type] = [insignia]
        return airplane_insignia_by_type_dict
