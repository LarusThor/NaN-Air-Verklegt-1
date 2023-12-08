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
        self.past_voyage_list = self.data_wrapper.read_past_flights() #TODO: tengja frekar við hinn logic?
        self.upcoming_voyage_lsit = self.data_wrapper.get_upcoming_flights()#TODO: tengja frekar við hinn logic?
    
    def schedule_employee(self):
        """ Returns employee schedule """
        pass

    def employee_working(self, date):
        """ Returns a list of all employees working on a specific day. """    
        workers_on_day = []
        flight_list = []
        voyage_list = self.past_voyage_list
        voyage_list.update(self.upcoming_voyage_lsit)
        date = datetime.strptime(date, "%Y-%m-%d")
        #print(voyage_list)
        
        for flight in voyage_list.values():
            dates = [datetime.strptime(flight.departure.date()), flight.arrival.date()]
            if date in dates:
                flight_list.append(flight.flight_nr)
        
            return flight_list
        
            """
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]
            if date in dates:
                departure = datetime.strptime(flight.departure, "%Y-%m-%d %H:%M:%S")
                arrival = datetime.strptime(flight.arrival, "%Y-%m-%d %H:%M:%S") 
                hours = (arrival - departure)
                #flights_list.append(f"{flight.flight_nr}: {employee.name} worked {hours} hours")
                total_hours += hours.total_seconds() / 3600
            return(flight)
            """
        

        #return employee.name, flights_list, total_hours
    

    def employee_not_working(self, date):
        """ Returns a list of all eployees not working on a specific day. """
        pass

    
    def schedule_voyage(self):
        """ Return voyage schedule. """
        pass