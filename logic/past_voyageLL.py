from data.data_wrapper import DataWrapper
from dataclasses import asdict
from model.past_voyage_model import PastVoyage

class PastVoyageLL:
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def get_past_voyages(self):
        """ TODO: add docstring"""
        past_voyages_dict = self.data_wrapper.get_past_flights()
        return past_voyages_dict