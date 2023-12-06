from data.destinationIO import DestinationIO
from model.destination_model import Destination

'''dest = Destination(
destination_id = "test",
destination = "test",
airportName = "test",
distanceFromIceland = "test",
emergencyContact = "test",
emergencyNumber = "test")'''


d = DestinationIO()

dest_list = d.read_all_destinations()
print(dest_list)
'd.add_destination(dest)'
