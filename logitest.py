from data.destinationIO import DestinationIO
from model.destination_model import Destination
from logic.destinationLL import DestinationLL

all_dests = DestinationIO().read_all_destinations()


id = input()
counter = 0

for destination in all_dests:
    if destination.destination_id == id:
        break
    else:
        counter += 1
print(counter)

dest = all_dests[counter]
dest.emergency_contact_name = input()
dest.emergency_contact_number = input()

# dest = Destination(
# destination_id = "LWK",
# emergency_contact_name = "luigiboys",
# emergency_contact_number = "luigiboys")


d = DestinationIO()

dest_lidt = d.update_destination(dest)
print(dest_lidt)

