from ui.main_menuUI import Menu
from logic.LogicWrapper import LogicWrapper
from model.employee_model import Employee

EMPLOYEES_OPTIONS = ["1. List employees - Alphabetical", "2. Employee information", "3. Add employee"]
LIST_EMPLOYEES_OPTIONS = ["1. Print pilots", "2. Print flight attendants", "3. Print all employees", "4. Print most experienced"]
EMPLOYEE_INFORMATION_OPTIONS = ["1. Print employee information", "2. Change employee information."]
CHANGE_EMPLOYEE_INFO_OPTIONS = ["1. Edit home address", "2. Edit phone number", "3. Edit email", "4. Edit home address"]

class EmployeeUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()
        self.all_employees_list = self.logic_wrapper.employee_list()
        self.pilot_list = self.logic_wrapper.pilot_list()
        self.flight_attendant_list = self.logic_wrapper.flight_attendant_list()
        self.employee_info = self.logic_wrapper.employee_info

    def employees_options(self) -> str:
        self.menus.display_options(EMPLOYEES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    
    def list_employees_options(self) -> str:
        self.menus.display_options(LIST_EMPLOYEES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action

    def print_crew(self, crew_list) -> None:
        """function used to print out a list"""
        crew_list.sort()
        for person in crew_list:
            print(person)
        print()
        print("(M)enu  (R)epeat")
        action = str(input("Enter your action: ").lower())
        if action == "m":
            None
        elif action == "r":
            None

    def get_pilots(self) -> None:
        print()
        print("All pilots:")
        print("-"*15)
        self.print_crew(self.pilot_list)
    
    def get_flight_attendants(self) -> None:
        print()
        print("All flight attendants:")
        print("-"*15)
        self.print_crew(self.flight_attendant_list)
    
    def get_all_employees(self) -> None:
        print()
        print("All employees:")
        print("-"*15)
        self.print_crew(self.all_employees_list)

    def get_most_experienced(self):
        pass

    def get_employee(self):
        social_id = str(input("Enter employee social ID: ")).strip()
        employee = self.employee_info(social_id)
        print(employee)

    def employee_info_options(self) -> str:
        self.menus.display_options(EMPLOYEE_INFORMATION_OPTIONS)
        action = str(input("Enter your action: ").lower())   
        return action 

    def get_info(self):
        social_id = str(input("Enter employee social ID: ")).strip()
        employee = self.employee_info(social_id)
        print(employee)

    def change_info_options(self):
        pass

    def change_home_address(self):
        pass

    def change_phone_number(self):
        pass
    
    def change_email(self):
        pass

    def add_employee(self): #define
        print("Fill out the following informaation about the new employee:")
        name = input("Name: ")
        social_id = input("Social ID: ")
        phone_number = input("Phone number: ")
        email = input("Email: ")
        home_address = input("Home adress: ")

        roles = ["Pilot","Cabincrew"]
        print("Role:\n1. Pilot\n2. Cabincrew")
        role = input()