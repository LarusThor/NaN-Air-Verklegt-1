from data.destinationIO import DestinationIO
from model.destination_model import Destination

dest = Destination(
destination_id = "FAE",
destination = "test",
airportName = "test",
distanceFromIceland = "test",
emergencyContact = "test",
emergencyNumber = "test")


d = DestinationIO()


d.update_destination(dest)
