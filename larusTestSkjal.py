from data.data_wrapper import DataWrapper
from itertools import chain
from logic.employeeLL import EmployeeLL

class AirplaneLL():
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        self.emlployees = EmployeeLL()
        self.airplane_list = self.data_wrapper.get_airplanes()
        self.airplane_types = self.data_wrapper.get_airplane_types()
        self.past_voyage_list = self.data_wrapper.get_past_flights()
        self.upcoming_voyage_list = self.data_wrapper.get_upcoming_flights() #TODO: tengja frekar við hinn logic?
        self.pilots = self.emlployees.get_all_pilots()

    def airplane_insignia_by_type(self):
            """ Dictionary which sorts airplanes in use by their types """
            airplanes_by_type_dict = dict()

            for plane_insignia, plane_type_id, manufacturer, model, capacity in self.airplane_list.items():
                if model in plane_type_id:
                    airplanes_by_type_dict[plane_type_id].append(plane_insignia)

            return airplanes_by_type_dict

d = AirplaneLL()

print(d.airplane_insignia_by_type())
