class PastVoyageLL:
    def __init__(self, logic_wrapper):
        self.logic = logic_wrapper


    def get_past_voyages(self) -> dict:
        """ TODO: add docstring"""
        past_voyages_dict = self.logic.data_wrapper.get_past_flights()
        
        return past_voyages_dict
    