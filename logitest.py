from data.destinationIO import DestinationIO
from model.destination_model import Destination
from logic.destinationLL import DestinationLL

all_dests = DestinationIO().read_all_destinations()
dest = all_dests[3]

dest.emergency_contact_name = "luigiboys"
dest.emergency_contact_number = "luigiboys"

# dest = Destination(
# destination_id = "LWK",
# emergency_contact_name = "luigiboys",
# emergency_contact_number = "luigiboys")


d = DestinationIO()

dest_lidt = d.update_destination(dest)
print(dest_lidt)

