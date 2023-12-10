from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper

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
        print("Choose day")
        print("Input date as: day/month/year")
        date = input("Enter date: ")
        return date
    
    def schedule_for_a_day_options(self) -> str:
        """ TODO: add docstring """
        self.menus.display_options(SCHEDULE_FOR_A_DAY_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action

    def who_was_working(self, date):
        """ TODO: add docstring """
        pass

    def get_how_was_not_working(self, date):
        """ TODO: add docstring """
        pass

    def get_employee(self) -> str:
        """ TODO: add docstring """
        employee = input("Enter the employees social ID: ")
        return employee
    
    def get_schedule_for_employee(self, employee):
        """ TODO: add docstring """
        pass

        