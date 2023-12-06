from dataclasses import dataclass

@dataclass
class Voyage:
    destination: str
    estimatedFlightDuration: str
    departureDate: str
    depatureTimeFromIceland: str
    arrivalDate: str
    arrivalTime: str
    flightNumberArrival: str
    flightNumberDeparture: str
    seatSales: str
    availableSeats: str
    status: str
    bookingStatus: str
        

#destination -> upcoming_flights.csv -> arr_at
#departureDate -> upcoming_flights.csv -> departure
#departureTimeFromIceland -> upcoming_flights.csv -> departure
#arrivalDate -> upcoming_flights.csv -> arrival
#arrivalTime -> upcoming_flights.csv -> arrival
#flightNumberArrival -> upcoming_flights.csv -> flight_nr
#flightNumberDeparture -> upcoming_flights.csv -> flight_nr
#seatSales -> past_flights.csv -> seats_sold