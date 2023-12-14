from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from datetime import date, datetime

SCHEDULE_OPTIONS = ["1. Schedule for a specific day", "2. Schedule for specific employee"]
SCHEDULE_FOR_EMPLOYEE = ["1. View their weekly schedule", "2. View their total work hours over a specific time"]
SCHEDULE_FOR_A_DAY_OPTIONS = ["1. See who was working", "2. See who was not working"]


class ScheduleUI:
    def __init__(self) -> None:
        self.menus = Menu()
        self.logic_wrapper = LogicWrapper()

    def schedule_options(self) -> str:
        """Shows the options the user can choose from when they choose schedule from the main menu"""
        self.menus.display_options("Schedule:", SCHEDULE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action

    def schedule_for_employee_options(self) -> str:
        """Shows the options the user can choose from when they enter in the employee social id"""
        self.menus.display_options("Schedule for employee:", SCHEDULE_FOR_EMPLOYEE)
        action = str(input("Enter your action: ").lower())
        return action


    def schedule_for_a_day_options(self) -> str:
        """ TODO: add docstring """
        self.menus.display_options("Schedule for a specific day:", SCHEDULE_FOR_A_DAY_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action

    def get_schedule_by_day(self) -> str:
        """TODO: add docsting"""
        date_input = input("Input date (year-month-day): ").strip()
        date_format = "%Y-%m-%d"
        a_date = datetime.strptime(date_input, date_format)
        return a_date.date()

    def who_was_working(self, date_working: date) -> None:
        """ TODO: add docstring """
        title = f"The people that were working on {date_working}:"
        result = ""
        employees = self.logic_wrapper.employee_working(date_working)
        for employee in employees:
            result += employee.name + "\n"

        self.menus.print_the_info(title, result)


    def get_who_was_not_working(self, date_not_working: date) -> None:
        """Gets the people that where not working on a specific date"""
        title = f"The people that were not working on {date_not_working}:"
        result = ""
        employees = self.logic_wrapper.employee_not_working(date_not_working)
        for employee in employees:
            result += employee.name + "\n"
        
        self.menus.print_the_info(title, result)

    def get_employee(self) -> str:
        """TODO: add docstring"""
        employee = input("Enter the employees social ID: ")
        return employee

    def get_schedule_for_employee(self, employee: str) -> None:
        """TODO: add docstring"""
        year = input("Enter year: ")
        week = input("Enter week: ")
        title = "Week schedule: "
        result = self.logic_wrapper.employee_schedule_by_week(employee, year, week)
        self.menus.print_the_info(title, result)

    
    def get_datetime(self) -> date:
        date_input = input("Input date (year-month-day): ").strip()
        date_format = "%Y-%m-%d"
        a_date = datetime.strptime(date_input, date_format)
        return a_date


    def get_total_hours_worked(self) -> None:
        print("See total hours an employee has worked! ")
        social_id = input("Enter social ID: ").strip()
        employee = self.logic_wrapper.employee_info(social_id)


        print(f"Choose what dates to see {employee.name}'s work schedule for.")
        print("\nStart of time period. ")
        start_date = self.get_datetime()
        print("\nEnd of time period. ")
        end_date = self.get_datetime()

        voyages, hours = self.logic_wrapper.total_hours_worked(employee, start_date, end_date)
        # print(f"{employee.name} worked {hours} hours within {start_date.date()} - {end_date.date()}")
        # print(f"Voyages worked by {employee.name}: ")
        hours_int = int(hours)
        title = f"{employee.name} worked {hours_int} hours within {start_date.date()} - {end_date.date()}"
        result = ""
        for voyage, destination in voyages:
            result += f"{voyage} to {destination} \n"

        self.menus.print_the_info(title, result)
        
