from ui.menu_managerUI import Menu
from logic.logic_wrapper import LogicWrapper
from model.employee_model import Employee

EMPLOYEES_OPTIONS = [
    "1. List employees - Alphabetical",
    "2. Employee information",
    "3. Add employee",
]
LIST_EMPLOYEES_OPTIONS = [
    "1. Print pilots",
    "2. Print flight attendants",
    "3. Print all employees",
    "4. Print most experienced",
]
EMPLOYEE_INFORMATION_OPTIONS = [
    "1. Print employee information",
    "2. Change employee information.",
]
CHANGE_EMPLOYEE_INFO_OPTIONS = [
    "1. Edit home address",
    "2. Edit phone number",
    "3. Edit email",
    "4. Edit home address",
]


class EmployeeUI:
    def __init__(self) -> None:
        """Instantiate a EmployeeUI object."""
        self.logic_wrapper = LogicWrapper()
        self.menus = Menu()
        self.validation = self.logic_wrapper.validation

    def employees_options(self) -> str:
        """Displays options for information and actions about employees."""
        self.menus.display_options("Employee:", EMPLOYEES_OPTIONS)
        action = input("Enter your action: ").lower()
        return action

    def list_employees_options(self) -> str:
        """Prints out the options for witch tipe of employee list the user wants to see. Returns for the action input"""
        self.menus.display_options("List employees:", LIST_EMPLOYEES_OPTIONS)
        action = input("Enter your action: ").lower()
        return action

    def employee_info_options(self) -> str:
        """Prints out the options that come up when the user chooses to get the employees information.
        And gets the action input from the user
        """
        self.menus.display_options(
            "Employee information:", EMPLOYEE_INFORMATION_OPTIONS
        )
        action = input("Enter your action: ").lower()
        return action

    def get_pilots(self) -> None:
        """Gets the pilots from the logic wrapper. Calls a function in the menu_manager that takes care of
        printing the pilots and the title out."""
        pilot_list_model = self.logic_wrapper.pilot_list()
        title = "All pilots:"
        return_pilot_list = []
        result = ""

        for pilot in pilot_list_model:
            return_pilot_list.append(pilot.name)
            
        for pilot in sorted(return_pilot_list):
            result += pilot + "\n"
            
        user_input = self.menus.print_the_info(title, result)
        return user_input

    def get_flight_attendants(self) -> None:
        """Gets the flight attendants from the logic wrapper. Calls a function in the menu_manager that takes care of
        printing the flight attendants and the title out."""

        flight_attendant_list = self.logic_wrapper.flight_attendant_list()
        title = "All flight attendants:"
        result = ""

        for person in sorted(flight_attendant_list):
            result += person + "\n"

        user_input = self.menus.print_the_info(title, result)
        return user_input

    def get_all_employees(self) -> None:
        """Gets all the employees from the logic wrapper. Calls a function in the menu_manager that takes care of
        printing all the employees and the title out."""
        employees = self.logic_wrapper.employee_dict()
        title = "All employees:"
        result = ""

        for person in sorted(employees):
            result += person + "\n"

        user_input = self.menus.print_the_info(title, result)

        return user_input

    def get_employee(self) -> Employee:
        """Gets a social id number from a user and gets that employee from the logic wrapper."""

        employee_info = self.logic_wrapper.employee_info
        social_id = str(input("Enter employee social ID: ")).strip()
        while not self.validation.validate_social_ID(social_id):
            print("ERROR: Invalid social ID. \nSocial ID should be 10 digits. ")
            social_id = str(input("Enter employee social ID: ")).strip()

        try:
            employee = employee_info(social_id)
        except KeyError:
            print("Employee does not exist in the system!")

        return employee

    def get_info(self) -> None:
        """Takes the social id of an employee and prints out their information"""

        employee_info = self.logic_wrapper.employee_info

        social_id = str(input("Enter employee social ID: ")).strip()

        valid_id = False
        while valid_id == False:
            try:
                employee = employee_info(social_id)
                title = "Employee information:"
                result = ""
                result += "{:<14} {}".format("Name:", employee.name) + "\n"
                result += "{:<14} {}".format("Social ID:", employee.social_id) + "\n"
                result += "{:<14} {}".format("Role:", employee.role) + "\n"
                result += "{:<14} {}".format("Rank:", employee.rank) + "\n"
                result += "{:<14} {}".format("Licence:", employee.licence) + "\n"
                result += "{:<14} {}".format("Email:", employee.email) + "\n"
                result += (
                    "{:<14} {}".format("Phone number:", employee.phonenumber) + "\n"
                )
                result += (
                    "{:<14} {}".format("Home address:", employee.home_address) + "\n"
                )
                result += "{:<14} {}".format("Landline:", employee.landline) + "\n"
                action = self.menus.print_the_info(title, result)
                return action

            except KeyError:
                print("Employee is not in the system!")
                social_id = str(input("Enter employee social ID: ")).strip()

    def change_info_options(self) -> None:
        """Changes employees information.
        Not name or social ID
        """
        social_id = self.get_social_id()
        employee = self.logic_wrapper.employee_info(social_id)
        print(employee.social_id)

        # setting up variables so we can change or not change them
        social_id = employee.social_id
        name = employee.name
        role = employee.role
        rank = employee.rank
        licence = employee.licence
        email = employee.email
        phonenumber = employee.phonenumber
        home_address = employee.home_address
        landline = employee.landline

        # options to change
        options = f"""
            1: Change role
            2: Change rank and license
            3: Change email
            4: Change mobile number
            5: Change address
            6: Change landline

            Any other to quit

        """
        action = "N/A" 

        while action != "d":
            action = input(f"Select an option: {options} \n").lower().strip()
            match action:
                case "1":
                    role = self.choose_role()

                case "2":
                    rank, licence = self.choose_rank_and_licence(role)

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
        """ TODO: add docstring """
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
        validation = self.logic_wrapper.validation
        print("Fill out the following informaation about the new employee:")
        
        name = input("Name: ").title()
        while not validation.validate_name(name):
            print("ERROR: Invalid name \nName has to be a string of length > 3. ")
            name = input("Name: ").title()
            continue
        
        social_id = input("Social ID: ")
        while not validation.validate_social_ID(social_id):
            print("ERROR: Invalid social ID \n Social ID should be 10 digits. ")
            social_id = input("Social ID: ")
 
        phone_number = input("Phone number: ")
        while not validation.validate_number(phone_number):
            print("ERROR: Invalid phone number \n Phone number should be 7 digits. ")
            phone_number = input("Phone number: ")

        return phone_number

    def get_email(self) -> str:
        """User inputs email for employee"""
        email = input("Email: ")

        while not self.validation.validate_email(email):
            print("ERROR: Invalid email. \nEmail should include @ and a top level domain e.g. (.com/.org/.is)")
            email = input("Email: ")

        home_address = input("Home adress: ")
        while not validation.validate_address(home_address):
            print("ERROR: Invalid address \n Address should be a string")
            home_address = input("Home adress: ")


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
        landline_check = self.validation.validate_yes_no(optional_landline)
        
        while landline_check == False:
            print("Please enter a valid input")
            optional_landline = input("Do you want to add a landline number? (y)es or (n)o? ").lower()
            landline_check = self.validation.validate_yes_no(optional_landline)

        if optional_landline == "y":
            landline = self.get_phone_nr()

        elif optional_landline == "n":
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

        employee = Employee(
            name=name,
            social_id=social_id,
            phonenumber=phone_number,
            role=role,
            rank=rank,
            licence=license,
            email=email,
            home_address=home_address,
            landline=landline,
        )

        save_prompt = input("Would you like to save the new employee, (y)es or (n)o? ").lower()
        save_promt_check = self.validation.validate_yes_no(save_prompt)

        while save_promt_check == False:
            print("Please enter a valid input")
            save_prompt = input("Would you like to save the new employee, (y)es or (n)o? ").lower()
            save_promt_check = self.validation.validate_yes_no(save_prompt)

        while save_prompt != "y" and save_prompt != "n":
            print("Please enter a valid input")
            save_prompt = input("Would you like to save the new employee, (y)es or (n)o? ").lower()

        if save_prompt == "y":
            self.logic_wrapper.add_employee(employee)
            title = "New employee saved!"
            action = self.menus.print_the_info(title)
            return action

        elif save_prompt == "n":
            title = "New employee not saved."
            action = self.menus.print_the_info(title)
            return action

    def get_most_experienced(self) -> None:
        most_exper = self.logic_wrapper.get_most_experienced_employee()
        result = ""
        name, voyages = most_exper[0][0], most_exper[0][1]
        title = "The most experienced employee:"

        for name, voyages in most_exper:
            result += f"{name} has gone on {int(voyages)} voyages."

        action = self.menus.print_the_info(title, result)
        return action