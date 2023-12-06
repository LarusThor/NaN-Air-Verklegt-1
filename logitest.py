from data.destinationIO import DestinationIO
from model.destination_model import Destination

dest = Destination(
destination_id = "test",
destination = "test",
airportName = "test",
distanceFromIceland = "test",
emergencyContact = "test",
emergencyNumber = "test")

d = DestinationIO()

d.add_destination(dest)
