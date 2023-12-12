from data.data_wrapper import DataWrapper
from model.destination_model import Destination

class DestinationLL():
    def __init__(self, logic_wrapper) -> None:
        #self.data_wrapper = data_connection
        self.data_wrapper = DataWrapper()
        self.logic = logic_wrapper
   
   
    def get_destination_list(self) -> list:
        """ Returns a list of destinations within the system. """
        destinations = []
        dest_list = self.data_wrapper.get_all_destinations()
        for destination in dest_list:
            destinations.append(destination.destination)
        return destinations
    
    def add_destination(self, destination):
        """Takes in a customer object and forwards it to the data layer"""
        dest = self.data_wrapper
        dest.add_destinations(destination)
   

    def get_most_popular_destination(self) -> dict: #TODO: eyna að stytta nafn
        """ Returns the most popular destination. """
        destination_list = []
        destination_dict = {}
        past_voyage_list = self.data_wrapper.get_past_flights()
        upcoming_voyage_list = self.data_wrapper.get_upcoming_flights()
        voyage_list = past_voyage_list
        voyage_list.update(upcoming_voyage_list)
        for voyage in voyage_list.values():
            destination_list.append(voyage.dep_from)

        for destination in destination_list:
            counter = destination_list.count(destination)
            destination_dict[destination] = counter
        most_popular = max(set(destination_list), key=destination_list.count)

        return most_popular, destination_dict
   

    def change_destination_info(self, destination: Destination) -> None: #breyta í klasaritinu
        ''' Changes destination info '''
        return self.data_wrapper.change_destination_info(destination)
        #name
        #number


    def distance_from_iceland(self):
        destinations = self.destination_info()
        distance = dict()
        for destination in destinations:
            distance[destination.destination_id] = int(destination.distance_from_iceland) 
        
        return distance
    
    def update_contact_info(self, destination: Destination):
        """ Changes the contact name and number for a destination. """
        return self.data_wrapper.update_contacts(destination)
  