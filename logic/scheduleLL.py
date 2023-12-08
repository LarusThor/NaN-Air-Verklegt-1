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

    def employee_working(self, a_date):
        """ Returns a list of all employees working on a specific day. """    
        workers_on_day = []
        flight_list = []
        voyage_list = self.past_voyage_list
        voyage_list.update(self.upcoming_voyage_lsit)
        date = datetime.strptime(a_date, "%Y-%m-%d").date()
        #print(voyage_list)
        
        for flight in voyage_list.values():
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]
            departure_date = datetime.strptime(flight.departure,  "%Y-%m-%d %H:%M:%S").date()
            arrival_date = datetime.strptime(flight.arrival,  "%Y-%m-%d %H:%M:%S").date()

            dates = [departure_date, arrival_date]
            #print(date)
            #print(dates)
            if date in dates:
                workers_on_day.append(workers)
                flight_list.append(flight.flight_id)
                #print(flight)
        
        return flight_list, workers_on_day
        
        

        #return employee.name, flights_list, total_hours
    

    def employee_not_working(self, date):
        """ Returns a list of all eployees not working on a specific day. """
        pass

    
    def schedule_voyage(self):
        """ Return voyage schedule. """
        pass