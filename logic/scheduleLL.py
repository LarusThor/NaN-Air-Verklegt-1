from datetime import date
from model.employee_model import Employee


class ScheduleLL:
    def __init__(self, logic_wrapper) -> None:
        """Instantiate a ScheduleLL object.

        Args:
            logic_wrapper: The logic wrapper object that contains all logic layer objects.
        """
        self.logic = logic_wrapper

    def employee_schedule_by_week(self, employee: str, year: str, week_nr: str) -> str:
        """Returns employee schedule for a chosen week."""
        flights = []
        past_voyage_list = self.logic.get_past_voyages()
        upcoming_voyage_list = self.logic.upcoming_voyages()

        voyage_list = past_voyage_list | upcoming_voyage_list

        for flight in voyage_list.values():
            weeks = str(flight.departure.isocalendar().week)
            workers = [
                flight.captain,
                flight.copilot,
                flight.fsm,
                flight.fa1,
                flight.fa2,
                flight.fa3,
                flight.fa4,
                flight.fa5,
            ]

            if employee in workers and weeks == week_nr:
                if year in flight.departure.strftime("%Y-%m-%d %H:%M:%S"):
                    flights.append((flight.flight_nr, flight.arr_at))

        result = ""
        for voyage, destination in flights:
            if destination != "KEF":
                result += f"Flight{voyage}: From KEF to {destination} \n"
            else:
                result += f"Flight{voyage}: From {prev_destination} to {destination} \n"
            prev_destination = destination

        name = self.logic.employee_info(employee)
        if flights:
            return f"{name.name} is scheduled for these flights in week {week_nr}:\n{result} "
        else:
            return f"{name.name} is not scheduled for any flights in week {week_nr}!"

    def employee_working(self, date_working: date) -> set[tuple[Employee, str]]:
        """Returns a list of all eployees not working on a specific day.

        Args:
            date: The date the employees are working
        """
        employee_dict = self.logic.data_wrapper.get_all_staff_members()
        past_voyage_list = self.logic.get_past_voyages()
        upcoming_voyage_list = self.logic.upcoming_voyages()
        all_workers = set()
        all_workers.update(employee_dict)

        workers_on_day = list()
        voyage_list = past_voyage_list | upcoming_voyage_list

        for flight in voyage_list.values():
            workers = [
                flight.captain,
                flight.copilot,
                flight.fsm,
                flight.fa1,
                flight.fa2,
                flight.fa3,
                flight.fa4,
                flight.fa5,
            ]
            departure_date = flight.departure.date()
            arrival_date = flight.arrival.date()
            dates = [departure_date, arrival_date]
            if date_working in dates:
                for worker in workers:
                    if worker != "N/A":
                        employee = self.logic.employee_info(worker)

                        workers_on_day.append((employee, flight.arr_at))

        return workers_on_day


    def employee_not_working(self, date_not_working: date) -> set[Employee]:
        """Returns a list of all eployees not working on a specific day.

        Args:
            date: The date the employees are not working
        """
        employee_dict = self.logic.data_wrapper.get_all_staff_members()
        past_voyage_list = self.logic.get_past_voyages()
        upcoming_voyage_list = self.logic.upcoming_voyages()
        all_workers = set()
        all_workers.update(employee_dict)

        workers_on_day = set()
        voyage_list = past_voyage_list | upcoming_voyage_list

        for flight in voyage_list.values():
            workers = [
                flight.captain,
                flight.copilot,
                flight.fsm,
                flight.fa1,
                flight.fa2,
                flight.fa3,
                flight.fa4,
                flight.fa5,
            ]
            departure_date = flight.departure.date()
            arrival_date = flight.arrival.date()
            dates = [departure_date, arrival_date]
            if date_not_working in dates:
                workers_on_day.update(workers)

        worker_ids = all_workers - workers_on_day
        return [self.logic.employee_info(social_id) for social_id in worker_ids]
