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
        action = input("Enter your action: ").lower().strip()
        return action

    def list_employees_options(self) -> str:
        """Prints out the options for witch tipe of employee list the user wants to see. Returns for the action input"""
        self.menus.display_options("List employees:", LIST_EMPLOYEES_OPTIONS)
        action = input("Enter your action: ").lower().strip()
        return action

    def employee_info_options(self) -> str:
        """Prints out the options that come up when the user chooses to get the employees information.
        And gets the action input from the user
        """
        self.menus.display_options("Employee information:", EMPLOYEE_INFORMATION_OPTIONS)
        action = input("Enter your action: ").lower().strip()
        
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
        valid_id = False
        while not valid_id:
            try:
                employee = self.logic_wrapper.employee_info(social_id)
                print(employee.social_id)
                valid_id = True
            except KeyError:
                print("Employee does not exist in the system \nTry again!")
                social_id = self.get_social_id()

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
            social_id=social_id,
            name=name,
            role=role,
            rank=rank,
            licence=licence,
            email=email,
            phonenumber=phonenumber,
            home_address=home_address,
            landline=landline,
        )

        # print(employee)
        print(f"Updated information for {employee.name}")
        print(
            f"Social_id: {employee.social_id}\n"
            f"Role: {employee.role}\n"
            f"Rank: {employee.rank}\n"
            f"License: {employee.licence}\n"
            f"Email: {employee.email}\n"
            f"Mobile number: {employee.phonenumber}\n"
            f"Address: {employee.home_address}\n"
            f"Landline: {employee.landline}\n"
        )

        save_prompt = input(
            "Would you like to save the new employee, (y)es or (n)o? "
        ).lower().strip()
        save_promt_check = self.validation.validate_yes_no(save_prompt)
        while save_promt_check == False:
            print("Invalid input!")
            save_prompt = input(
                "Would you like to save the new employee, (y)es or (n)o? "
            ).lower().strip()
            save_promt_check = self.validation.validate_yes_no(save_prompt)
        if save_prompt == "y":
            self.logic_wrapper.change_employee_info(employee)
            title = "New information saved!"
            user_input = self.menus.print_the_info(title)

        elif save_prompt == "n":
            title = "Updated information not saved."
            user_input = self.menus.print_the_info(title)

        return user_input

    def choose_role(self) -> str:
        """User chooses a role for employee."""
        roles = {"1": "Pilot", "2": "Cabincrew"}

        print("Role:\n1. Pilot\n2. Cabincrew")
        print("-" * 15)
        role_choice = input("Choose role: ").strip()

        while role_choice != "1" and role_choice != "2":
            print("Invalid input! You can choose 1, 2")
            print("-" * 15)
            role_choice = input("Role: ").strip()
        role = roles[role_choice]

        return role

    def get_phone_nr(self) -> str:
        """User inputs a phone number for employee."""
        phone_number = input("Phone number: ").strip()

        while not self.validation.validate_number(phone_number):
            print("ERROR: Invalid phone number. \nPhone number should be 7 digits. ")
            phone_number = input("Phone number: ").strip()

        return phone_number

    def get_email(self) -> str:
        """User inputs email for employee"""
        email = input("Email: ").strip()

        while not self.validation.validate_email(email):
            print("ERROR: Invalid email. \nEmail should include @ and a top level domain e.g. (.com/.org/.is)")
            email = input("Email: ").strip()

        return email

    def get_address(self) -> str:
        """User inputs an address for employee."""
        home_address = input("Home address: ").strip()

        while not self.validation.validate_address(home_address):
            print("ERROR: Invalid address. \nAddress can be a word with 3 letters or more, optionally followed by address number.")
            home_address = input("Home address: ").strip()

        return home_address

    def choose_rank_and_licence(self, role: str) -> str | str:
        """User chooses rank and licence for employee."""
        airplane_types = self.logic_wrapper.airplane_types()

        if role == "Pilot":
            ranks = {"1": "Captain", "2": "Copilot"}
            print("Rank:\n1. Captain\n2. Copilot")
            print("-" * 15)
            rank_choice = input("Choose a rank: ").strip()

            while rank_choice != "1" and rank_choice != "2":
                print("Invalid input! You can choose 1 or 2")
                print("-" * 15)
                rank_choice = input("Rank: ").strip()
            if rank_choice == "1" or rank_choice == "2":
                # A dictionary of all the airplane types, updates if new airplane type is added
                licences = {
                    (i + 1): licence for i, licence in enumerate(airplane_types)
                }

                print("Licenses:")
                license_list = []
                for index, license in enumerate(licences.values()):
                    tuple_list = []
                    license_list.append(license[0])
                    print(f"{index+1}. {license[0]}")

                licence_choice = input("Choose license: ").strip()
                while licence_choice != "1" and licence_choice != "2" and licence_choice != "3":
                    print("Invalid input! You can choose 1, 2 or 3")
                    print("-" * 15)
                    licence_choice = input("Choose license: ").strip()
                licence_choice_int = int(licence_choice)
                license = license_list[licence_choice_int - 1]
            else:
                license = "N/A"

        elif role == "Cabincrew":
            ranks = {"1": "Flight Service Manager", "2": "Flight Attendant"}
            print("Rank:\n1. Flight Service Manager\n2. Flight Attendant")
            print("-" * 15)
            rank_choice = input("Choose a rank: ").strip()

            while rank_choice != "1" and rank_choice != "2":
                print("Invalid input! You can choose 1 or 2")
                print("-" * 15)
                rank_choice = input("Rank: ").strip()
            license = "N/A"

        rank = ranks[rank_choice]

        return rank, license

    def get_social_id(self) -> str:
        """Gets a social id number from the user"""
        employee = self.logic_wrapper.employee_dict()
        social_id = input("Social ID: ").strip()
        while not self.validation.validate_social_ID(social_id):
            print("ERROR: Invalid social ID. \nPlease enter a valid Social ID, should be 10 digits. ")
            social_id = input("Social ID: ").strip()

        return social_id


    def add_employee(self) -> None:
        """Allows user to add an employee to the system."""
        print("Fill out the following information about the new employee:")

        name = input("Name: ").title().strip()
        while not self.validation.validate_name(name):
            print("ERROR: Invalid name. \nName has to be a string of length >= 3. ")
            name = input("Name: ").title().strip()

        social_id = self.get_social_id()
        valid_social_id = False
        while valid_social_id != True:
            try:
                self.logic_wrapper.employee_info(social_id)
                print(
                    "Employee with that social ID already exists in the system \n Try again!"
                )
                social_id = self.get_social_id()
            except:
                valid_social_id = True

        phone_number = self.get_phone_nr()

        email = self.get_email()

        home_address = self.get_address()

        role = self.choose_role()

        rank, license = self.choose_rank_and_licence(role)
        license_list = []
        for item in license:
            license_list.append(item)

        optional_landline = input("Do you want to add a landline number? (y)es or (n)o? ").lower().strip()
        landline_check = self.validation.validate_yes_no(optional_landline)
        
        while landline_check == False:
            print("Please enter a valid input")
            optional_landline = input("Do you want to add a landline number? (y)es or (n)o? ").lower().strip()
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
            save_prompt = input("Would you like to save the new employee, (y)es or (n)o? ").lower().strip()
            save_promt_check = self.validation.validate_yes_no(save_prompt)

        while save_prompt != "y" and save_prompt != "n":
            print("Please enter a valid input")
            save_prompt = input("Would you like to save the new employee, (y)es or (n)o? ").lower().strip()

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
