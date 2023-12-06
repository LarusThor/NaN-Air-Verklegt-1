from logic.LogicWrapper import LogicWrapper
from model.destination_model import Destination

dest = Destination(
destination_id = "Logi",
destination = "er",
emergencyContact = "bestur",
emergencyNumber = "that's",
airportName = "on",
distanceFromIceland = "god"
)

d = LogicWrapper()

dest_list = d.add_destination(dest)
print(dest_list)
'd.add_destination(dest)'
