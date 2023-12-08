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
        self.upcoming_voyage_lsit = self.data_wrapper.get_upcoming_flights()#TODO: tengja frekar við hinn logic?
    
    def schedule_employee(self):
        """ Returns employee schedule """
        pass

    def employee_working(self, date):
        """ Returns a list of all employees working on a specific day. """    
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
    

    def employee_not_working(self, date):
        """ Returns a list of all eployees not working on a specific day. """
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

    
    def schedule_voyage(self):
        """ Return voyage schedule. """
        pass