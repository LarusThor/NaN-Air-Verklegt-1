from data.data_wrapper import DataWrapper
from logic.voyageLL import VoyageLL
from model.destination_model import Destination

class DestinationLL():
    def __init__(self) -> None:
        #self.data_wrapper = data_connection
        self.data_wrapper = DataWrapper()
        self.past_voyage_list = self.data_wrapper.get_past_flights()
        self.upcoming_voyage_list = self.data_wrapper.get_upcoming_flights()#TODO: tengja frekar við hinn logic?
   
   
    def get_destination_list(self):
        """ Returns a list of destinations within the system. """
        destination_list = []
        destinations = self.data_wrapper.get_all_destinations()
        for destination in destinations:
            destination_list.append(destination.destination)

        return destination_list

    
    def add_destination(self, destination: Destination) -> None:
        """Takes in a customer object and forwards it to the data layer"""
        dest = self.data_wrapper
        dest.add_destinations(destination)
   

    def get_most_popular_destination(self): #reyna að stytta nafn
        """ Returns the most popular destination. """
        destination_list = []
        destination_dict = {}
        voyage_list = self.past_voyage_list
        voyage_list.update(self.upcoming_voyage_list)
        for voyage in voyage_list.values():
            destination_list.append(voyage.dep_from)

        for destination in destination_list:
            counter = destination_list.count(destination)
            destination_dict[destination] = counter
        most_popular = max(set(destination_list), key=destination_list.count)
        return most_popular, destination_dict
   

    def change_destination_contact(self, destination: Destination): #breyta í klasaritinu
        """ Changes the contact for a destination. """
        pass
        #name
        #number