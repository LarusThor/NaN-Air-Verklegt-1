from model.employee_model import Employee
from datetime import datetime

class EmployeeLL:
    def __init__(self, logic_wrapper) -> None:
        """Instantiate a EmployeeLL object.

        Args:
            logic_wrapper: The logic wrapper object that contains all logic layer objects.
        """
        self.logic = logic_wrapper


    def get_employee_dict(self) -> list[str]:
        """ Returns a list of all employees within the system. """
        employee_dict = self.logic.data_wrapper.get_all_staff_members()
        
        return [employee.name for employee in employee_dict.values()]


    def get_all_pilots(self) -> list[str]:
        """ Returns a list of all pilots. """
        pilot_list = []
        employee_dict = self.logic.data_wrapper.get_all_staff_members()

        for employee_data in employee_dict.values():
            if employee_data.role == "Pilot":
                pilot_list.append(employee_data)
        
        return pilot_list
    

    def get_flight_attendants(self) -> list[str] :
        """ Returns a list of all flight attendants. """
        flight_attendant_list = []
        employee_dict = self.logic.data_wrapper.get_all_staff_members()
        for employee_data in employee_dict.values():
            if employee_data.role == "Cabincrew":
                flight_attendant_list.append(employee_data.name)
        
        return flight_attendant_list


    def get_employee(self, social_id: str) -> Employee:
        """Returns information about a chosen employee."""
        employee_dict = self.logic.data_wrapper.get_all_staff_members()
        
        return employee_dict[social_id]


    def change_employee_info(self, employee: Employee) -> None:
        """Lets user change employee information."""
        # TODO: cannot change name
        employee_dict = self.logic.data_wrapper.get_all_staff_members()

        assert employee.social_id in employee_dict, "Employee does not exist!"

        employee_dict[employee.social_id] = employee

        self.logic.data_wrapper.write_employees(list(employee_dict.values()))


    def add_employee(self, employee: Employee) -> None:
        """Adds employee to the system."""
        employee_dict = self.logic.data_wrapper.get_all_staff_members()

        assert employee.social_id not in employee_dict, "Employee with same social_id already exists!"

        employee_dict[employee.social_id] = employee
        self.logic.data_wrapper.write_employees(list(employee_dict.values()))


    def get_total_hours_worked(self, employee: Employee, start: datetime, end: datetime) -> tuple[list[str], float]:
        """Returns total hours an employee has worked."""
        #TODO: laga listann af voyages: fáum bara fyrstu 10
        flights_list = []
        total_hours = 0
        past_voyage_dict = self.logic.get_past_voyages()

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
            
            flights_list.append((flight.flight_nr, flight.arr_at))
            total_hours += work_hours

        return flights_list, total_hours
    
    def get_total_future_hours_worked(self, social_id: str, start: datetime, end: datetime) -> tuple[list[str], float]:
        """Returns total hours an employee has worked."""
        #TODO: laga listann af voyages: fáum bara fyrstu 10
        total_hours = 0
        upcoming_voyage_dict = self.logic.upcoming_voyages()
        employee = self.logic.employee_info(social_id)

        for flight in upcoming_voyage_dict.values():
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
            
            total_hours += work_hours

        return total_hours