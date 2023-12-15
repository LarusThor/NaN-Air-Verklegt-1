from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from datetime import date, datetime
from ui.employeesUI import EmployeeUI

SCHEDULE_OPTIONS = [
    "1. Schedule for a specific day",
    "2. Schedule for specific employee",
]
SCHEDULE_FOR_EMPLOYEE = [
    "1. View their weekly schedule",
    "2. View their total work hours over a specific time",
]
SCHEDULE_FOR_A_DAY_OPTIONS = ["1. See who was working", "2. See who was not working"]


class ScheduleUI:
    """ "Instantiate a ScheduleUI object."""

    def __init__(self) -> None:
        self.menus = Menu()
        self.logic_wrapper = LogicWrapper()
        self.employeeUI = EmployeeUI()
        self.validation = self.logic_wrapper.validation

    def schedule_options(self) -> str:
        """Shows the options the user can choose from when they choose schedule from the main menu"""
        self.menus.display_options("Schedule:", SCHEDULE_OPTIONS)
        action = input("Enter your action: ").lower().strip()

        return action

    def schedule_for_employee_options(self) -> str:
        """Shows the options the user can choose from when they enter in the employee social id"""
        self.menus.display_options("Schedule for employee:", SCHEDULE_FOR_EMPLOYEE)
        action = input("Enter your action: ").lower().strip()

        return action

    def schedule_for_a_day_options(self, date) -> str:
        """Lets user pick options to see for the day they chose."""
        self.menus.display_options(f"Schedule for {date}:", SCHEDULE_FOR_A_DAY_OPTIONS)
        action = input("Enter your action: ").lower().strip()

        return action

    def get_schedule_by_day(self) -> str:
        """Gets the date the user wants to see a schedule for."""
        date_input = input("Input date (YYYY-MM-DD): ").strip()
        while not self.validation.validate_date(date_input):
            print("Invalid date entered. ")
            date_input = input("Input date (YYYY-MM-DD): ").strip()
        date_format = "%Y-%m-%d"
        a_date = datetime.strptime(date_input, date_format)

        return a_date.date()

    def who_was_working(self, date_working: date) -> None:
        """Prints who was working on a chosen day"""
        title = f"The people that were working on {date_working}:"
        result = ""
        employees = self.logic_wrapper.employee_working(date_working)

        for employee, destination in employees:
            if destination != "KEF":
                result += f"{employee.name:<20} --> {destination:>5}\n"

        user_input = self.menus.print_the_info(title, result)

        return user_input

    def get_who_was_not_working(self, date_not_working: date) -> None:
        """Gets the people that where not working on a specific date"""
        title = f"The people that were not working on {date_not_working}:"
        result = ""
        employees = self.logic_wrapper.employee_not_working(date_not_working)
        for employee in employees:
            result += employee.name + "\n"

        user_input = self.menus.print_the_info(title, result)
        return user_input

    def get_employee(self) -> str:
        """Gets information about a specific employee"""
        social_id = input("Enter social ID: ").strip()
        valid_id = False

        while valid_id != True:
            try:
                employee = self.logic_wrapper.employee_info(social_id).social_id
                valid_id = True
            except KeyError or AttributeError:
                print("ERROR: Employee is not in the system! ")
                social_id = input("Social ID: ").strip()
        return employee

    def get_schedule_for_employee(self, employee: str) -> None:
        """Let's the user choose a time period to see the employees work time."""
        year = input("Enter year: ").strip()

        while not self.validation.validate_year(year):
            print("ERROR: invalid year.\nYear must be a number.")
            year = input("Enter year: ").strip()
        week = input("Enter week: ").strip()

        while not self.validation.validate_weeks(week):
            print("ERROR: invalid week number.\nWeek must be from 1-52.")
            week = input("Enter week: ").strip()

        title = "Week schedule: "
        result = self.logic_wrapper.employee_schedule_by_week(employee, year, week)

        user_input = self.menus.print_the_info(title, result)

        return user_input

    def get_datetime(self) -> date:
        """Gets a date from the user and converts it into datetime."""
        date_input = input("Input date (YYYY-MM-DD): ").strip()
        while not self.validation.validate_date(date_input):
            print("Invalid date entered. ")
            date_input = input("Input date (YYYY-MM-DD): ").strip()
        date_format = "%Y-%m-%d"
        a_date = datetime.strptime(date_input, date_format)

        return a_date

    def get_total_hours_worked(self) -> None:
        """Prints total hours an employee worked over a specidic period of time"""
        print("See total hours an employee has worked! ")

        valid_id = False
        social_id = self.employeeUI.get_social_id()
        while valid_id == False:
            try:
                employee = self.logic_wrapper.employee_info(social_id)
                valid_id = True
            except KeyError:
                print("There is no employee in the system with that ID \nTry again!")
                social_id = self.employeeUI.get_social_id()

        print(f"Choose what dates to see {employee.name}'s work schedule for.")
        print("\nStart of time period. ")

        start_date = self.get_datetime()
        print("\nEnd of time period. ")

        end_date = self.get_datetime()
        voyages, hours = self.logic_wrapper.total_hours_worked(
            employee, start_date, end_date
        )
        hours_int = int(hours)
        title = f"{employee.name} worked {hours_int} hours within {start_date.date()} - {end_date.date()}"
        result = ""
        for voyage, destination in voyages:
            if destination != "KEF":
                result += f"Flight{voyage}: From KEF to {destination} \n"
            else:
                result += f"Flight{voyage}: From {prev_destination} to {destination} \n"

            prev_destination = destination

        user_input = self.menus.print_the_info(title, result)
        return user_input
