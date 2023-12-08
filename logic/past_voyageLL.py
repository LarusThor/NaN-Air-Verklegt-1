from data.data_wrapper import DataWrapper


class PastVoyageLL:
    def __init__(self):
        self.data_wrapper = DataWrapper()
        self.voyage_list = self.data_wrapper.read_past_flights()

    def past_flight_list(self):
        return self.voyage_list