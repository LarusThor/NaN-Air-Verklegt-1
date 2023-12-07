from data.destinationIO import DestinationIO
from model.destination_model import Destination

dest = Destination(
destination_id = "KEF",
destination = "luigiboys",
airport_name = "luigiboys",
distance_from_iceland = "luigiboys",
emergency_contact_name = "luigiboys",
emergency_contact_number = "luigiboys")


d = DestinationIO()


d.update_destination(dest)

