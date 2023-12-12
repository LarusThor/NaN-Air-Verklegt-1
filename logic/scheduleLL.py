from datetime import date
from model.employee_model import Employee

class ScheduleLL():
    def __init__(self, logic_wrapper) -> None:
        """Instantiate a ScheduleLL object.

        Args:
            logic_wrapper: The logic wrapper object that contains all logic layer objects.
        """
        self.logic = logic_wrapper


    def employee_schedule_by_week(self, employee, year, week_nr) -> str:
        """ Returns employee schedule for a chosen week. """
        flights = []
        voyage_list = self.logic.get_all_voyages()
        for flight in voyage_list:
            weeks = str(flight.departure.isocalendar().week)
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]
            
            if employee in workers and weeks == week_nr:
                if year in flight.departure.strftime('%Y-%m-%d %H:%M:%S'):
                    flights.append(f"{flight.flight_nr} to {flight.arr_at}")

        name = self.logic.employee_info(employee)
        if flights:
            return f"{name.name} is scheduled for these flights: {flights} in week {week_nr}!"
        else:
            return f"{name.name} is not scheduled for any flights in week {week_nr}!"
        
        
    def employee_working(self, date_working: date) -> list[Employee]:
        """ Returns a list of all employees working on a specific day. """    
        #TODO: simplify
        past_voyage_list = self.logic.past_voyages()
        upcoming_voyage_list = self.logic.upcoming_voyages()
        workers_on_day = []
        voyage_list = list(past_voyage_list.values()) + list(upcoming_voyage_list.values())
        #a_date = datetime.strptime(date, "%Y-%m-%d").date()

        for flight in voyage_list:
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]
            departure_date = flight.departure.date()
            arrival_date = flight.arrival.date()
            dates = [departure_date, arrival_date]
            
            if date_working in dates:
                workers_on_day.extend(workers)
        
        return [self.logicr.employee_info(s_id) for s_id in workers_on_day if s_id != 'N/A'] #TODO: laga na bull very ugley
    

    def employee_not_working(self, date_not_working: date) -> set[Employee]:
        """Returns a list of all eployees not working on a specific day. 
        
        Args:
            date: The date the employees are not working
        """
        #TODO: simplify, tengja betur við þá sem eru að virka
        employee_dict = self.logic.data_wrapper.get_all_staff_members()
        past_voyage_list = self.logic.past_voyages()
        upcoming_voyage_list = self.logic.upcoming_voyages()
        all_workers = set()
        all_workers.update(employee_dict)

        workers_on_day = set()
        voyage_list = list(past_voyage_list.values() + list(upcoming_voyage_list.values()))

        for flight in voyage_list:
            workers = [flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2, flight.fa3, flight.fa4, flight.fa5]
            departure_date = flight.departure.date()
            arrival_date = flight.arrival.date()
            dates = [departure_date, arrival_date]
            if date_not_working in dates:
                workers_on_day.update(workers)

        worker_ids =  all_workers-workers_on_day
        return [self.logic.employee_info(s_id) for s_id in worker_ids]
  