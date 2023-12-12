class FlightInformation:
    def __init__(self, logic_wrapper):
        self.logic = logic_wrapper

    def capacity(self):
        capacity = dict()
        airplanes = self.logic.data_wrapper.get_airplanes()
        for keys, plane in airplanes.items():
            capacity[keys] = plane.capacity

        return capacity
      

    def flight_fully_booked(self):
        capacity = self.capacity()
        booked = dict()
        print(capacity)
        upcoming_voyages = self.logic.upcoming_voyages()
        for voyage in upcoming_voyages.values():
          if voyage.aircraft_id != "N/A":
            #print(capacity[voyage.aircraft_id])
            if capacity[voyage.aircraft_id] <= int(voyage.seats_sold):
                booking_status = "Booked"
                #booked[voyage.id] = booking_status
            else:
                booking_status = capacity[voyage.aircraft_id] - int(voyage.seats_sold)
            booked[voyage.flight_nr] = booking_status
            
        return booked
