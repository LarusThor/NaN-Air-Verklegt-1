from data.data_wrapper import DataWrapper

class AirplaneLL():
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        self.airplane_list = self.data_wrapper.get_airplanes()
   
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
        pass
   
    def get_airplane_status_by_date_time(self): #laga þetta nafn líka
        """ Returns the status of a plane on a given day and time. """
        pass
   
    def get_airplane_usage(self):
        """ Returns the total usage of a specific plane. """
        pass