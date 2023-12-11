from data.data_wrapper import DataWrapper
from model.employee_model import Employee
from model.past_voyage_model import PastVoyage
from datetime import datetime, date

class EmployeeLL:
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()

        # TODO: Do not read and store these here, instead read them again every time you use them :P
        #self.employee_dict = self.data_wrapper.get_all_staff_members()
        #self.past_voyage_dict = self.data_wrapper.get_past_flights()
        # self.voyage_list = self.data_wrapper.read_past_flights()#TODO: tengja frekar við hinn logic?

    def get_employee_dict(self) -> list[str]:
        """ Returns a list of all employees within the system. """
        employee_dict = self.data_wrapper.get_all_staff_members()
        return [employee.name for employee in employee_dict.values()]


    def get_all_pilots(self) -> list[str]:
        """ Returns a list of all pilots. """
        pilot_list = []
        employee_dict = self.data_wrapper.get_all_staff_members()

        for employee_data in employee_dict.values():
            if employee_data.role == "Pilot":
                pilot_list.append(employee_data)
        
        return pilot_list
    

    def get_flight_attendants(self) -> list[str] :
        """ Returns a list of all flight attendants. """
        flight_attendant_list = []
        employee_dict = self.data_wrapper.get_all_staff_members()
        for employee_data in employee_dict.values():
            if employee_data.role == "Cabincrew":
                flight_attendant_list.append(employee_data.name)
        
        return flight_attendant_list

    def get_employee(self, social_id: str) -> Employee:
        """Returns information about a chosen employee."""
        employee_dict = self.data_wrapper.get_all_staff_members()
        return employee_dict[social_id]


    def change_employee_info(self, employee: Employee):
        """Lets user change employee information."""
        # TODO: cannot change name
        employee_dict = self.data_wrapper.get_all_staff_members()

        assert employee.social_id in employee_dict, "Employee does not exist!"

        employee_dict[employee.social_id] = employee

        self.data_wrapper.write_employees(list(employee_dict.values()))


    def add_employee(self, employee: Employee) -> None:
        """Adds employee to the system."""
        employee_dict = self.data_wrapper.get_all_staff_members()

        assert employee.social_id not in employee_dict, "Employee with same social_id already exists!"

        employee_dict[employee.social_id] = employee
        self.data_wrapper.write_employees(list(employee_dict.values()))


    def get_total_hours_worked(self, employee: Employee, start: datetime, end: datetime):
        """Returns total hours an employee has worked."""
        #TODO: laga listann af voyages: fáum bara fyrstu 10
        flights_list = []
        total_hours = 0
        employee_dict = self.data_wrapper.get_all_staff_members()
        past_voyage_dict = self.data_wrapper.get_past_flights()
        
        for flight in past_voyage_dict.values():
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]

            if employee.social_id not in workers:
                continue

            arrival = flight.arrival
            departure = flight.departure

            if arrival > end or departure < start:
                continue

            if arrival > end:
                arrival = end

            if departure < start:
                departure = start

            work_hours = (arrival - departure).total_seconds() / 3600
            
            flights_list.append(f"{flight.flight_nr}: {employee.name} worked {work_hours} hours")
            total_hours += work_hours

        return employee.name, flights_list, total_hours