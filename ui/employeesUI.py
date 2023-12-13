from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from model.employee_model import Employee

EMPLOYEES_OPTIONS = ["1. List employees - Alphabetical", "2. Employee information", "3. Add employee"]
LIST_EMPLOYEES_OPTIONS = ["1. Print pilots", "2. Print flight attendants", "3. Print all employees", "4. Print most experienced"]
EMPLOYEE_INFORMATION_OPTIONS = ["1. Print employee information", "2. Change employee information."]
CHANGE_EMPLOYEE_INFO_OPTIONS = ["1. Edit home address", "2. Edit phone number", "3. Edit email", "4. Edit home address"]

class EmployeeUI:
    def __init__(self) -> None:
        """Instantiate a EmployeeUI object."""
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()
        self.validation = self.logic_wrapper.validation


    def employees_options(self) -> str:
        """ Displays options for information and actions about employees. """
        self.menus.display_options(EMPLOYEES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action
    

    def list_employees_options(self) -> str:
        """Prints out the options for witch tipe of employee list the user wants to see. Returns for the action input"""
        self.menus.display_options(LIST_EMPLOYEES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        return action


    def print_crew(self, crew_list) -> None:
        """Used to print out a list"""
        crew_list.sort()
        for person in crew_list:
            print(person)
        print()
        print("(M)enu")
        action = str(input("Enter your action: ").lower())
        if action == "m":
            None


    def get_pilots(self) -> None:
        """Prints out a list of all the pilots"""
        pilot_list = self.logic_wrapper.pilot_list()
        title = "All pilots:"
        result = ""
        for pilot in pilot_list:
            result += pilot.name + "\n"
        self.menus.print_the_info(title, result)

    

    def get_flight_attendants(self) -> None:
        """Prints out a list of all the flight attendants"""
        flight_attendant_list = self.logic_wrapper.flight_attendant_list()
        title = "All flight attendants:"
        result = ""
        for person in flight_attendant_list:
            result += person + "\n"
        self.menus.print_the_info(title, result)
    

    def get_all_employees(self) -> None:
        """Prints out a list of all the employees"""
        employees = self.logic_wrapper.employee_list()
        title = "All employees:"
        result = ""
        for person in employees:
            result += person + "\n"
        self.menus.print_the_info(title, result)


    def get_employee(self):
        """Gets a social id number and returns that employee"""
        employee_info = self.logic_wrapper.employee_info
        social_id = str(input("Enter employee social ID: ")).strip()
        employee = employee_info(social_id)
        return employee


    def employee_info_options(self) -> str:
        """Prints out the options that come up when the user chooses to get the employees information.
        And gets the action input from the user
        """
        self.menus.display_options(EMPLOYEE_INFORMATION_OPTIONS)
        action = str(input("Enter your action: ").lower())   
        return action 


    def get_info(self):
        """Takes the social id of an employee and prints out their information"""
        employee_info = self.logic_wrapper.employee_info
        social_id = str(input("Enter employee social ID: ")).strip()
        while not self.validation.validate_social_ID(social_id):
            print("ERROR: Invalid social ID \n Social ID should be 10 digits. ")
            social_id = str(input("Enter employee social ID: ")).strip()
        employee = employee_info(social_id)
        #TODO: spyrja um ef það er skrifað 10 digits en ekki retti employee
        print()
        print("Employee information:")
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
        action = input("Enter your action: ") #TODO: er ekki tengt í neitt



    def change_info_options(self):
        """ Changes employees information. 
        Not name or social ID 
        """
        social_id = self.get_social_id()
        employee = self.logic_wrapper.employee_info(social_id)
        print(employee.social_id)
        
        #setting up variables so we can change or not change them
        social_id=employee.social_id
        name=employee.name
        role=employee.role
        rank=employee.rank
        licence=employee.licence
        email=employee.email
        phonenumber=employee.phonenumber
        home_address=employee.home_address
        landline=employee.landline

        #options to change
        options = f"""
            1: Change role
            2: Change rank and license
            3: Change email
            4: Change mobile number
            5. Change address
            6. Change landline

            Any other to quit

        """

        action = input(f"Select an option: {options} \n" ).lower().strip()
        while action != "d":
            match action:
                case "1":
                    role = self.choose_role()

                case "2":
                    rank, licence = self.choose_rank_and_licence()

                case "3":
                    email = self.get_email()

                case "4":
                    phonenumber = self.get_phone_nr()

                case "5":
                    home_address = self.get_address()

                case "6":
                    landline = self.get_phone_nr()

                case _:
                    break

            action = input(f"Select an option: {options} \n" ).lower().strip()
        
        employee = Employee(
            social_id = social_id,
            name=name, 
            role=role,
            rank=rank,
            licence=licence,
            email=email,
            phonenumber=phonenumber,
            home_address=home_address,
            landline=landline,
            )
        
        print(employee)

        self.logic_wrapper.change_employee_info(employee)


    def choose_role(self):
        """User chooses a role for employee."""
        roles = {
            "1": "Pilot",
            "2": "Cabincrew"
            }
        
        print("Role:\n1. Pilot\n2. Cabincrew")
        role_choice = input()
        
        while role_choice != "1" and role_choice != "2":
            print("Invalid input! You can choose 1, 2")
            role_choice = input("Role: ")
        role = roles[role_choice]
        
        return role
    

    def get_phone_nr(self):
        """User inputs a phone number for employee."""
        phone_number = input("Phone number: ")
        while not self.validation.validate_number(phone_number):
            print("ERROR: Invalid phone number \n Phone number should be 7 digits. ")
            phone_number = input("Phone number: ")
        return phone_number
    

    def get_email(self):
        """User inputs email for employee"""
        email = input("Email: ")
        while not self.validation.validate_email(email):
            print("ERROR: Invalid email \n Email should include @ and a top level domain e.g. (.com/.org/.is)")
            email = input("Email: ")
        return email
    

    def get_address(self):
        """User inputs an address for employee."""
        home_address = input("Home adress: ")
        while not self.validation.validate_address(home_address):
            print("ERROR: Invalid address \n Address should be a string")
            home_address = input("Home adress: ")
        return home_address
    

    def choose_rank_and_licence(self):
        """User chooses rank and licence for employee."""
        ranks = { #TODO: laga þetta er harðkóðað
            "1": "Captain", 
            "2": "Copilot", 
            "3": "Flight Service Manager", 
            "4": "Flight Attendant"
            }
        
        print("Rank:\n1. Captain\n2. Copilot\n3. Flight Service Manager\n4. Flight Attendant")
        rank_choice = input().strip()

        while rank_choice != "1" and rank_choice != "2" and rank_choice != "3" and rank_choice != "4":
            print("Invalid input! You can choose 1, 2, 3, or 4")#TODO: ætti frekar að vera í validation
            rank = input("Rank: ")
        
        rank = ranks[rank_choice]

        if rank_choice == "1" or rank_choice == "2":
            licences = { #TODO: laga þetta er harðkóðað
                "1" : "NAFokker100",
                "2" : "NAFokkerF28",
                "3" : "NABAE146"
                }
            
            print("Licenses:\n1. NAFokker100\n2. NAFokkerF28\n3. NABAE146",)
            licence_choice = input()
            licence = licences[licence_choice]
        else:
            licence = "N/A"

        return rank, licence
    

    def get_social_id(self):
        """Gets a social id number from the user"""
        social_id = input("Social ID: ")
        while not self.validation.validate_social_ID(social_id):
            print("ERROR: Invalid social ID \n Social ID should be 10 digits. ")
            social_id = input("Social ID: ")

        return social_id


    def add_employee(self): #define
        """Allows user to add an employee to the system."""
        validation = self.logic_wrapper.validation
        print("Fill out the following informaation about the new employee:")
        
        name = input("Name: ").title()
        while not self.validation.validate_name(name):
            print("ERROR: Invalid name \nName has to be a string of length > 3. ")
            name = input("Name: ").title()
        
        social_id = self.get_social_id()
 
        phone_number = self.get_phone_nr()

        email = self.get_email()

        home_address = self.get_address()

        role = self.choose_role()
     
        rank, license = self.choose_rank_and_licence()

        optional_landline = input("Do you want to add a landline number? (y)es or (n)o? ").lower()
        if optional_landline == "y":
            landline = self.get_phone_nr()
        else:
            landline = "N/A"

        print("New employee:")
        print("Name:", name)
        print("Social ID:", social_id)
        print("Phone number:", phone_number)
        print("Email:", email)
        print("Home adress:", home_address)
        print("Role:", role)
        print("Rank:", rank)
        print("License:", license)
        print("Landline number:", landline)

        # TODO
        employee = Employee(
            name=name, 
            social_id=social_id, 
            phonenumber=phone_number,
            role=role, 
            rank=rank,
            licence=license,
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
            action = str(input("Enter your action: ").lower())#TODO: validate
            if action == "m":
                None
            elif action == "r":
                print()
                self.logic_wrapper.add_employee(employee)