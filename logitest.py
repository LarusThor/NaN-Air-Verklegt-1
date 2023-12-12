from data.destinationIO import DestinationIO
from model.destination_model import Destination
from logic.destinationLL import DestinationLL

dest = Destination(
destination_id = "LWK",
emergency_contact_name = "luigiboys",
emergency_contact_number = "luigiboys")


d = DestinationIO()

dest_lidt = d.update_contacts(dest)
print(dest_lidt)

