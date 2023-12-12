from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from datetime import date, datetime

SCHEDULE_OPTIONS = ["1. Schedule for a specific day", "2. Schedule for specific employee"]
SCHEDULE_FOR_A_DAY_OPTIONS = ["1. See who was working", "2. See who was not working"]


class ScheduleUI:
    def __init__(self) -> None:
        self.menus = Menu()
        self.logic_wrapper = LogicWrapper()


    def schedule_options(self) -> str:
        """ TODO: add docstring """
        self.menus.display_options(SCHEDULE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action


    def get_schedule_by_day(self) -> str:
        """ TODO: add docstring """
        date_input = input("Input date (year/month/day): ")
        date_format = "%Y/%m/%d"
        a_date = datetime.strptime(date_input, date_format)
        return a_date.strftime(date_format)
    

    def schedule_for_a_day_options(self) -> str:
        """ TODO: add docstring """
        self.menus.display_options(SCHEDULE_FOR_A_DAY_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action


    def who_was_working(self, date_working) -> None:
        """ TODO: add docstring """
        #TODO: make pretty :))
        #TODO: prentast ekki út
        employees = self.logic_wrapper.employee_working(date_working)
        print(employees)
        for employee in employees:
            print("BRUH")
            print(employee)


    def get_how_was_not_working(self, date_not_working):
        """ TODO: add docstring """

        employees = self.logic_wrapper.employee_not_working(date_not_working)
        for employee in employees:
            print(employee.name)


    def get_employee(self) -> str:
        """ TODO: add docstring """
        employee = input("Enter the employees social ID: ")
        return employee
    

    def get_schedule_for_employee(self, employee):
        """ TODO: add docstring """
        year = int(input("Enter year: ")).strip()
        week = int(input("Enter week: ")).strip()
        print(self.logic_wrapper.employee_schedule_by_week(employee, year, week))

        