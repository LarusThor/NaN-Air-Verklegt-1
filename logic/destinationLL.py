from data.data_wrapper import DataWrapper

class DestinationLL():
    def __init__(self) -> None:
        #self.data_wrapper = data_connection
        self.data_wrapper = DataWrapper()
   
    def get_destination_list(self):
        """ Returns a list of destinations within the system. """
        return self.data_wrapper.get_all_destinations()
    
    def add_destination(self, destination):
        """Takes in a customer object and forwards it to the data layer"""
        dest = self.data_wrapper
        dest.add_destinations(destination)
   
    def get_most_popular_destination(self): #reyna að stytta nafn
        """ Returns the most popular destination. """
        #TODO: laga
        destination_list = []
        destinations = self.get_destination_list()
        for elem in destinations:
             destination_list.append(elem.destination)
        return max(set(destination_list), key=destination_list.count)
   
    def change_destination_contact(self): #breyta í klasaritinu
        """ Changes the contact for a destination. """
        pass
        #name
        #number