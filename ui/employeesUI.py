from ui.main_menuUI import Menu
from logic.LogicWrapper import LogicWrapper

EMPLOYEES_OPTIONS = ["1. List employees - Alphabetical", "2. Employee information", "3. Add employee"]
LIST_EMPLOYEES_OPTIONS = ["1. Print pilots", "2. Print flight attendants", "3. Print all employees", "4. Print most experienced"]
EMPLOYEE_INFORMATION_OPTIONS = ["1. Print employee information", "2. Change employee information."]
CHANGE_EMPLOYEE_INFO_OPTIONS = ["1. Edit home address", "2. Edit phone number", "3. Edit email"]

class EmployeesUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()

        self.all_employees_list = self.logic_wrapper.employee_list()
        self.pilots_list = self.logic_wrapper.pilot_list()
        self.flight_attendants_list = self.logic_wrapper.flight_attendant_list()

    def employees(self):
        self.menus.display_options(EMPLOYEES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action

# List employees :
    def list_employees(self): #if nr 1 from EMPLOYEES_OPTIONS is chosen
        """four options on how to list the employees, 1. Print pilots, 2. Print flight attendants, 3. Print all employees, 4. Print most experienced""" 
        self.menus.display_options(LIST_EMPLOYEES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    
    def print_crew(self, crew_list): 
        """function used to print out a list"""
        self.crew_list = crew_list
        self.crew_list.sort()
        for person in self.crew_list:
            print(person)
        print()
        print("(M)enu  (R)epeat")
        
        # action = str(input("Enter your action: ").lower())
        # if action == "m":
        #     None
        # elif action == "r":
        #     list_employees()        

    def get_pilots(self):
        print()
        print("All pilots:")
        print("-"*15)
        self.print_crew(self.pilots_list)
    
    def get_flight_attendants(self):
        print()
        print("All flight attendants:")
        print("-"*15)
        self.print_crew(self.flight_attendants_list)
    
    def get_all_employees(self):            
        print()
        print("All employees:")
        print("-"*15)
        self.print_crew(self.all_employees_list)
    
    def get_most_experienced(self):
        pass #print the most experienced TODO

# Employee Information :
    def get_employee(self): #TODO
        employees_social_id = input("Enter the employees social ID")
        """TODO use the ID to get the name of the employee, and return the name"""
        return employees_social_id

    def employee_info_options(self):
        self.menus.display_options(EMPLOYEE_INFORMATION_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    
    def get_info(self, employee_name):
        pass

    def change_info_options(self):
        self.menus.display_options(CHANGE_EMPLOYEE_INFO_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action

    def change_employees_info(self):
        pass

    def change_email(self):
        pass

    def change_phone_number(self):
        pass

    def change_home_address(self):
        pass

# Add employee :
    def add_employee(self):
        print("Fill out the following informaation about the new employee:")
        name = input("Name: ")
        social_id = input("Social ID: ")
        phone_number = input("Phone number: ")
        email = input("Email: ")
        home_adress = input("Home adress: ")
        work_titles = ["Captain", "Pilot", "Flight Service Manager", "Flight Attendant"]
        print("Work title:\n1. Captain\n2. Pilot\n3. Flight Service Manager\n4. Flight Attendant")
        work_title = input()
        while work_title != "1" and work_title != "2" and work_title != "3" and work_title != "4":
            print("Invalid input! You can choose 1, 2, 3, or 4")
            work_title = input("Work title: ")

        if work_title == "1" or work_title == "2":
            flight_type = input("Enter the flight type the employee is qualified to fly: ")
        print("New employee:")
        print("Name:", name)
        print("Social ID:", social_id)
        print("Phone number:", phone_number)
        print("Email:", email)
        print("Home adress:", home_adress)
        print("Work title:", work_titles[int(work_title) - 1])
        save_prompt = input("Would you like to save the new employee, (y)es or (n)o? ").lower()
        while save_prompt != "y" and save_prompt != "n":
            print("Invalid input!")
            save_prompt = input("Enter Y for yes or N for no:").lower()

        if save_prompt == "y":
            print()
            print("New employee saved!")
            print()
            print("(M)enu  (R)epeat")
            action = str(input("Enter your action: ").lower())
            if action == "m":
                None
            elif action == "r":
                print()
                EmployeesUI.add_employee()   

        elif save_prompt == "n":
            print()
            print("New employee not saved.")
            print()
            print("(M)enu  (R)epeat")
            action = str(input("Enter your action: ").lower())
            if action == "m":
                None
            elif action == "r":
                print()
                EmployeesUI.add_employee()   

