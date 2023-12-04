class Voyage:
    def __init__(self, destination, departureDate, depatureTimeFromIceland, 
                 arrivalDate, arrivalTime, flightNumberArrival, flightNumberDeparture, 
                 seatSales, availableSeats, status, bookingStatus) -> str:
        self.destination = destination
        self.departureDate = departureDate
        self.departureTimeFromIceland = depatureTimeFromIceland
        self.arrivalDate = arrivalDate
        self.arrivalTime = arrivalTime
        self.flightNumberArrival = flightNumberArrival
        self.flightNumberDeparture = flightNumberDeparture
        self.seatSales = seatSales
        self.availableSeats = availableSeats
        self.status = status
        self.bookingStatus = bookingStatus

#destination -> upcoming_flights.csv -> arr_at
#departureDate -> upcoming_flights.csv -> departure
#departureTimeFromIceland -> upcoming_flights.csv -> departure
#arrivalDate -> upcoming_flights.csv -> arrival
#arrivalTime -> upcoming_flights.csv -> arrival
#flightNumberArrival -> upcoming_flights.csv -> flight_nr
#flightNumberDeparture -> upcoming_flights.csv -> flight_nr