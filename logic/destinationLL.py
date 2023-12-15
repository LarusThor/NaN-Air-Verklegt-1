from model.destination_model import Destination


class DestinationLL:
    def __init__(self, logic_wrapper) -> None:
        self.logic = logic_wrapper

    def get_destination_info(self) -> dict:
        """Returns dictionary with their id's as keys and destination models as values. """
        return self.logic.data_wrapper.get_all_destinations_info()

    def get_destination_list(self) -> list:
        """Returns a list of destinations within the system."""
        return self.logic.data_wrapper.get_all_destinations()

    def get_only_destinations(self) -> list:
        """ Returns a lsit of only destinations. """
        destinations = []
        dest_list = self.logic.data_wrapper.get_all_destinations()
        for destination in dest_list:
            destinations.append(destination.destination)

        return destinations

    def add_destination(self, destination: Destination) -> None:
        """Takes in a customer object and forwards it to the data layer"""
        dest = self.logic.data_wrapper
        dest.add_destinations(destination)

    def get_most_popular_destination(self, ) -> tuple[str, dict]:
        """Returns the most popular destination."""
        destination_list = []
        destination_dict = {}
        past_voyage_list = self.logic.data_wrapper.get_past_flights()
        upcoming_voyage_list = self.logic.data_wrapper.get_upcoming_flights()
        voyage_list = past_voyage_list
        voyage_list.update(upcoming_voyage_list)
        for voyage in voyage_list.values():
            if voyage.dep_from != "KEF":
                destination_list.append(voyage.dep_from)

        for destination in destination_list:
            if destination != "KEF":
                counter = destination_list.count(destination)
                destination_dict[destination] = counter
            else:
                continue
            
        most_popular = max(set(destination_list), key=destination_list.count)
        return most_popular

    def change_destination_info(self, destination: Destination) -> None:  # breyta í klasaritinu
        """Changes destination info"""
        return self.logic.data_wrapper.change_destination_info(destination)

    def distance_from_iceland(self) -> dict:
        destinations = self.logic.data_wrapper.get_all_destinations_info()
        distance = dict()
        for destination_id, destination_info in destinations.items():
            distance[destination_id] = int(destination_info.distance_from_iceland)

        return distance

    def update_contact_info(self, destination: Destination) -> None:
        """Changes the contact name and number for a destination."""
        return self.logic.data_wrapper.update_contacts(destination)
