class FlightInformationLL:
    def __init__(self, logic_wrapper):
        """Instantiate a FlightInformationLL object.

        Args:
            logic_wrapper: The logic wrapper object that contains all logic layer objects.
        """
        self.logic = logic_wrapper

    def capacity(self):
        capacity = dict()
        airplanes = self.logic.data_wrapper.get_airplanes()
        for keys, plane in airplanes.items():
            capacity[keys] = plane.capacity

        return capacity
      

    def flight_fully_booked(self):
        capacity = self.capacity()
        booked = list()
        upcoming_voyages = self.logic.upcoming_voyages()
        for voyage in upcoming_voyages.values():
          if voyage.aircraft_id != "N/A":
            if capacity[voyage.aircraft_id] <= int(voyage.seats_sold):
                booking_status = "Booked"
            else:
                booking_status = capacity[voyage.aircraft_id] - int(voyage.seats_sold)
            booked.append((voyage, booking_status))
        return booked
    