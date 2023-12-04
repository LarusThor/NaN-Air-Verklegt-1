class Destination:
    def __init__(self, destination:str, destinationTime:str, destinationDate:str, emergencyContact:str, emergencyNumber:str, 
                 airportName:str, estimatedFlightDuration:str, distanceFromIceland:str) -> None:
        self.destination = destination
        self.destinationTime = destinationTime
        self.destinationDate = destinationDate
        self.emergencyContact = emergencyContact
        self.emergencyNumber = emergencyNumber
        self.airportName = airportName
        self.estimatedFlightDuration = estimatedFlightDuration
        self.distanceFromIceland = distanceFromIceland