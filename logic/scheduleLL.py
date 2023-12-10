from data.data_wrapper import DataWrapper
from model.schedule_model import Schedule
from model.past_voyage_model import PastVoyage
from logic.past_voyageLL import PastVoyageLL
from model.upcoming_voyage_model import UpcomingVoyage
from logic.upcoming_voyageLL import UpcomingVoyage
from datetime import datetime, date
from model.employee_model import Employee

class ScheduleLL():
    def __init__(self, logic_wrapper) -> None:
        self.data_wrapper = DataWrapper()
        self.logic_wrapper = logic_wrapper
        self.employee_dict = self.data_wrapper.get_all_staff_members()
        self.past_voyage_list = self.data_wrapper.get_past_flights() #TODO: tengja frekar við hinn logic?
        self.upcoming_voyage_list = self.data_wrapper.get_upcoming_flights()#TODO: tengja frekar við hinn logic?


    def employee_schedule_by_week(self, employee, year, week_nr) -> str:
        """ Returns employee schedule """
        flights = []
        voyage_list = self.past_voyage_list
        voyage_list.update(self.upcoming_voyage_list)
        for flight in voyage_list.values():
            weeks = str(flight.departure.isocalendar().week)
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]
            
            if employee in workers and weeks == week_nr:
                if year in flight.departure.strftime('%Y-%m-%d %H:%M:%S'):
                    flights.append(f"{flight.flight_nr} to {flight.arr_at}")

        name = self.logic_wrapper.employee_info(employee)
        if flights:
            return f"{name.name} is scheduled for these flights: {flights} in week {week_nr}!"
        else:
            return f"{name.name} is not scheduled for any flights in week {week_nr}!"
        
        
    def employee_working(self, date_working: date) -> list:
        """ Returns a list of all employees working on a specific day. """    
        #TODO: simplify
        workers_on_day = []
        voyage_list = self.past_voyage_list
        voyage_list.update(self.upcoming_voyage_list)
        #a_date = datetime.strptime(date, "%Y-%m-%d").date()

        for flight in voyage_list.values():
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]
            departure_date = flight.departure.date()
            arrival_date = flight.arrival.date()
            dates = [departure_date, arrival_date]
            
            if date_working in dates:
                workers_on_day.append([flight.flight_nr, workers])
        
        return [self.logic_wrapper.employee_info(s_id) for s_id in workers_on_day]
    

    def employee_not_working(self, date_not_working: date) -> set[Employee]:
        """Returns a list of all eployees not working on a specific day. 
        
        Args:
            date: The date the employees are not working
        """
        #TODO: simplify, tengja betur við þá sem eru að virka
        all_workers = set()
        all_workers.update(self.employee_dict)
        workers_on_day = set()
        voyage_list = self.past_voyage_list
        voyage_list.update(self.upcoming_voyage_list)

        for flight in voyage_list.values():
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]
            departure_date = flight.departure.date()
            arrival_date = flight.arrival.date()
            dates = [departure_date, arrival_date]
            if date_not_working in dates:
                workers_on_day.update(workers)

        worker_ids =  all_workers-workers_on_day
        return [self.logic_wrapper.employee_info(s_id) for s_id in worker_ids]