from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
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
        self.validation = self.logic_wrapper.validation
        


    def employees_options(self) -> str:
        """Prints the first options the user can choose from when they choose employee. Returns the action input"""
        self.menus.display_options(EMPLOYEES_OPTIONS)
        action = str(input("Enter your action: ").lower())#validate
        return action
    

    def list_employees_options(self) -> str:
        """Prints out the options for witch tipe of employee list the user wants to see. Returns the action input"""
        self.menus.display_options(LIST_EMPLOYEES_OPTIONS)
        action = str(input("Enter your action: ").lower())#validate
        return action


    def print_crew(self, crew_list) -> None:
        """Used to print out a list"""
        crew_list.sort()
        for person in crew_list:
            print(person)
        print()
        print("(M)enu  (R)epeat")
        action = str(input("Enter your action: ").lower())#validate
        while not self.validation.validate_print_crew(action):
            print("ERROR: Invalid")
            action = input("Enter you action:") 
        if action == "m":
            None
        elif action == "r":
            None


    def get_pilots(self) -> None:
        """Prints out a list of all the pilots"""
        print()
        print("All pilots:")
        print("-"*15)
        for pilot in self.pilot_list:
            print(pilot.name)
    

    def get_flight_attendants(self) -> None:
        """Prints out a list of all the flight attendants"""
        print()
        print("All flight attendants:")
        print("-"*15)
        self.print_crew(self.flight_attendant_list)
    

    def get_all_employees(self) -> None:
        """Prints out a list of all the employees"""
        print()
        print("All employees:")
        print("-"*15)
        self.print_crew(self.all_employees_list)


    def get_most_experienced(self):
        """ TODO: add docstring """
        pass


    def get_employee(self):
        """Gets a social id number and returns that employee"""
        social_id = str(input("Enter employee social ID: ")).strip()#validate
        employee = self.employee_info(social_id)
        return employee

    def employee_info_options(self) -> str:
        """Prints out the options that come up when the user chooses to get the employees information.
        And gets the action input from the user"""
        self.menus.display_options(EMPLOYEE_INFORMATION_OPTIONS)
        action = str(input("Enter your action: ").lower())#validate   
        return action 


    def get_info(self):
        """Takes the social id of an employee and prints out their information"""
        social_id = str(input("Enter employee social ID: ")).strip()#validate
        
        employee = self.employee_info(social_id)
        print()
        print("Employee's information:")
        print("-"*30)
        print("{:<14}".format("Name:"), employee.name)
        print("{:<14}".format("Social ID:"), employee.social_id)
        print("{:<14}".format("Role:"), employee.role)
        print("{:<14}".format("Rank:"), employee.rank)
        print("{:<14}".format("Licence:"), employee.licence)
        print("{:<14}".format("Email:"), employee.email)
        print("{:<14}".format("Phone number:"), employee.phonenumber)
        print("{:<14}".format("Home address:"), employee.home_address)
        print("{:<14}".format("Landline:"), employee.landline)
        print()
        print("(H)ome  (B)ack")
        action = input("Enter your action: ")#validate


    def change_info_options(self):
        """ TODO: add docstring """
        #TODO: robert hjálp
        employee = Employee(
            social_id="broseph",
            name="44",
            role="test_role",
            rank="test_rank",
            licence="f",
            email="f@f.f",
            phonenumber="0.5",
            home_address="bruh street 69",
            landline="??"
             )
        self.logic_wrapper.change_employee_info(employee)




    def change_home_address(self):
        pass

    def change_phone_number(self):
        """ TODO: add docstring """
        pass
    

    def change_email(self):
        """ TODO: add docstring """
        pass


    def add_employee(self): #define
        """ TODO: add docstring """
        #TODO: rosa ljótt getum við stytt eða fegrað?
        #TODO: skipta í fleir föll??
        
        print("Fill out the following informaation about the new employee:")
        
        name = input("Name: ").title()
        while not self.validation.validate_name(name):
            print("ERROR: Invalid name \nName has to be a string of length > 3. ")
            name = input("Name: ").title()
        
        social_id = input("Social ID: ")
        while not self.validation.validate_social_ID(social_id):
            print("ERROR: Invalid social ID \n Social ID should be 10 digits. ")
            social_id = input("Social ID: ")
 
        phone_number = input("Phone number: ")
        while not self.validation.validate_number(phone_number):
            print("ERROR: Invalid phone number \n Phone number should be 7 digits. ")
            phone_number = input("Phone number: ")

        email = input("Email: ")
        while not self.validation.validate_email(email):
            print("ERROR: Invalid email \n Email should include @ and a top level domain e.g. (.com/.org/.is)")
            email = input("Email: ")

        home_address = input("Home adress: ")
        while not self.validation.validate_address(home_address):
            print("ERROR: Invalid address \n Address should be a string")
            home_address = input("Home address: ")


        roles = ["Pilot","Cabincrew"]
        print("Role:\n1. Pilot\n2. Cabincrew")
        role = input()
        while role != "1" and role != "2":
            print("Invalid input! You can choose 1, 2")
            role = input("Role: ")
        ranks = ["Captain", "Copilot", "Flight Service Manager", "Flight Attendant"]
        print("Rank:\n1. Captain\n2. Copilot\n3. Flight Service Manager\n4. Flight Attendant")
        rank = input()
        while rank != "1" and rank != "2" and rank != "3" and rank != "4":
            print("Invalid input! You can choose 1, 2, 3, or 4")
            rank = input("Rank: ")
        if rank == "1" or rank == "2":
            licences = ["NAFokker100","NAFokkerF28","NABAE146"]
            print("Licenses:\n1. NAFokker100\n2. NAFokkerF28\n3. NABAE146",)
            licence = input()
        else:
            licence = "N/A"
        optional_landline = input("Do you want to add a landline number? (y)es or (n)o? ").lower()
        if optional_landline == "y":
            landline = input("Landline number: ")#validate
        else:
            landline = None

        print("New employee:")
        print("Name:", name)
        print("Social ID:", social_id)
        print("Phone number:", phone_number)
        print("Email:", email)
        print("Home adress:", home_address)
        print("Role:", roles[int(role) - 1])
        print("Rank:", ranks[int(rank) - 1])
        print("License:", licences[int(licence) - 1])
        print("Landline number:", landline)

        # TODO
        employee = Employee(
            name=name, 
            social_id=social_id, 
            phonenumber=phone_number,
            role=role, 
            rank=rank,
            licence=licence,
            email=email,
            home_address=home_address,
            landline=landline
        )

        save_prompt = input("Would you like to save the new employee, (y)es or (n)o? ").lower()
        while save_prompt != "y" and save_prompt != "n":
            print("Invalid input!")
            save_prompt = input("Enter Y for yes or N for no:").lower()

        if save_prompt == "y":
            self.logic_wrapper.add_employee(employee)
            print()
            print("New employee saved!")
            print()
            print("(M)enu  (R)epeat")
            action = str(input("Enter your action: ").lower())
            if action == "m":
                None
            elif action == "r":
                print()
                self.logic_wrapper.add_employee(employee)   

        elif save_prompt == "n":
            print()
            print("New employee not saved.")
            print()
            print("(M)enu  (R)epeat")
            action = str(input("Enter your action: ").lower())#validate
            if action == "m":
                None
            elif action == "r":
                print()
                self.logic_wrapper.add_employee(employee)