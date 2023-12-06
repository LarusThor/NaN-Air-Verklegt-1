from dataclasses import dataclass

@dataclass
class Voyage:
    destination: str
    estimated_flight_duration: str
    departure_date: str
    depature_time_from_iceland: str
    arrival_date: str
    arrival_time: str
    flight_number_arrival: str
    flight_number_departure: str
    seat_sales: str
    available_seats: str
    status: str
    booking_status: str
        

#destination -> upcoming_flights.csv -> arr_at
#departureDate -> upcoming_flights.csv -> departure
#departureTimeFromIceland -> upcoming_flights.csv -> departure
#arrivalDate -> upcoming_flights.csv -> arrival
#arrivalTime -> upcoming_flights.csv -> arrival
#flightNumberArrival -> upcoming_flights.csv -> flight_nr
#flightNumberDeparture -> upcoming_flights.csv -> flight_nr
#seatSales -> past_flights.csv -> seats_sold