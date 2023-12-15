class PastVoyageLL:
    def __init__(self, logic_wrapper):
        """Instantiate a PastVoyageLL object.

        Args:
            logic_wrapper: The logic wrapper object that contains all logic layer objects.
        """
        self.logic = logic_wrapper

    def get_past_voyages(self) -> dict:
        """Returns a dictionary with all past voyages."""
        past_voyages_dict = self.logic.data_wrapper.get_past_flights()

        return past_voyages_dict
