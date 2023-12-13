from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from datetime import date, datetime

SCHEDULE_OPTIONS = [
    "1. Schedule for a specific day",
    "2. Schedule for specific employee",
]
SCHEDULE_FOR_A_DAY_OPTIONS = ["1. See who was working", "2. See who was not working"]


class ScheduleUI:
    def __init__(self) -> None:
        self.menus = Menu()
        self.logic_wrapper = LogicWrapper()

    def schedule_options(self) -> str:
        """Shows the options the user can choose from when they choose schedule from the main menu"""
        self.menus.display_options(SCHEDULE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action

    def get_schedule_by_day(self) -> str:
        """TODO: add docsting"""
        date_input = input("Input date (year-month-day): ").strip()
        date_format = "%Y-%m-%d"
        a_date = datetime.strptime(date_input, date_format)
        return a_date.date()

    def schedule_for_a_day_options(self) -> str:
        """TODO: add docstring"""
        self.menus.display_options(SCHEDULE_FOR_A_DAY_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action

    def who_was_working(self, date_working) -> None:
        """TODO: add docstring"""
        # TODO: make pretty :))
        # TODO: prentast ekki út
        employees = self.logic_wrapper.employee_working(date_working)
        for employee in employees:
            print(employee.name)

    def get_who_was_not_working(self, date_not_working):
        """TODO: add docstring"""
        # TODO: make pretty

        employees = self.logic_wrapper.employee_not_working(date_not_working)
        for employee in employees:
            print(employee.name)

    def get_employee(self) -> str:
        """TODO: add docstring"""
        employee = input("Enter the employees social ID: ")
        return employee

    def get_schedule_for_employee(self, employee):
        """TODO: add docstring"""
        year = input("Enter year: ")
        week = input("Enter week: ")
        print(self.logic_wrapper.employee_schedule_by_week(employee, year, week))
