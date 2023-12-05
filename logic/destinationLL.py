from data.data_wrapper import DataWrapper

class DestinationLL():
    def __init__(self) -> None:
        #self.data_wrapper = data_connection
        pass
   
    def get_destination_list(self):
        """ Returns a list of destinations within the system. """
        dest = DataWrapper()
        dest_list = dest.get_all_destinations()
        destination_names = []  # New list to store destination names
        # for destination in dest_list:
        for key, value in dest_list.items():
            if key == 'destination':
                destination_names.append(value)
        return destination_names
    
    def add_destination(self, destination):
        """ Adds a destination to the system. """
        pass
   
    def get_most_popular_destination(self): #reyna að stytta nafn
        """ Returns the most popular destination. """
        pass
   
    def change_destination_contact(self): #breyta í klasaritinu
        """ Changes the contact for a destination. """
        pass
        #name
        #number