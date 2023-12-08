from data.data_wrapper import DataWrapper
from model.schedule_model import Schedule
from model.past_voyage_model import PastVoyage
from logic.past_voyageLL import PastVoyageLL
from model.upcoming_voyage_model import UpcomingVoyage
from logic.upcoming_voyageLL import UpcomingVoyage
from datetime import datetime

class ScheduleLL():
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        self.employee_dict = self.data_wrapper.get_all_staff_members()
        self.past_voyage_list = self.data_wrapper.get_past_flights() #TODO: tengja frekar við hinn logic?
        self.upcoming_voyage_list = self.data_wrapper.get_upcoming_flights()#TODO: tengja frekar við hinn logic?
    
    def schedule_employee_by_week(self, employee, year, week_nr):
        """ Returns employee schedule """
        employee_list = []
        voyage_list = self.past_voyage_list
        voyage_list.update(self.upcoming_voyage_list)
        for flight in voyage_list.values():
            weeks = str(flight.departure.isocalendar().week)
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]
            if employee in workers and weeks == week_nr:
                if year in flight.departure.strftime('%Y-%m-%d %H:%M:%S'):
                    employee_list.append(flight.flight_nr)

        if employee_list:
            return f"{employee} is scheduled for these flights: {employee_list} in week 4"
        else:
            return f"{employee} is not scheduled for any flights in week {week_nr}"
        



    def employee_working(self, date:datetime) -> list:
        """ Returns a list of all employees working on a specific day. """    
        #TODO: simplify
        workers_on_day = []
        voyage_list = self.past_voyage_list
        voyage_list.update(self.upcoming_voyage_lsit)
        a_date = datetime.strptime(date, "%Y-%m-%d").date()

        for flight in voyage_list.values():
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]
            departure_date = flight.departure.date()
            arrival_date = flight.arrival.date()
            dates = [departure_date, arrival_date]
            if a_date in dates:
                for worker in workers:
                    #TODO: tengja við að finna employee frá social id
                    pass
                workers_on_day.append([flight.flight_nr, workers])
        
        return workers_on_day
    

    def employee_not_working(self, date: datetime) -> set:
        """ Returns a list of all eployees not working on a specific day. """
        #TODO: simplify, tengja betur við þá sem eru að virka
        all_workers = set()
        all_workers.update(self.employee_dict)
        workers_on_day = set()
        voyage_list = self.past_voyage_list
        voyage_list.update(self.upcoming_voyage_lsit)
        a_date = datetime.strptime(date, "%Y-%m-%d").date()

        for flight in voyage_list.values():
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]
            departure_date = flight.departure.date()
            arrival_date = flight.arrival.date()
            dates = [departure_date, arrival_date]
            if a_date in dates:
                workers_on_day.update(workers)
        
        return all_workers-workers_on_day