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