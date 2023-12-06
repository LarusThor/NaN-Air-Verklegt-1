from ui.main_menuUI import display_options
from logic.LogicWrapper import LogicWrapper
from model.employee_model import Employee

EMPLOYEES_OPTIONS = ["1. List employees - Alphabetical", "2. Employee information", "3. Add employee"]
LIST_EMPLOYEES_OPTIONS = ["1. Print pilots", "2. Print flight attendants", "3. Print all employees", "4. Print most experienced"]
EMPLOYEE_INFORMATION_OPTIONS = ["1. Print employee information", "2. Change employee information."]
CHANGE_EMPLOYEE_INFO_OPTIONS = ["1. Edit home address", "2. Edit phone number", "3. Edit email", "4. Edit home address"]

logic_wrapper = LogicWrapper()
employee_list = logic_wrapper.employee_list()
pilot_list = logic_wrapper.pilot_list()
flight_attendant_list = logic_wrapper.flight_attendant_list()


def list_employees(): #if nr 1 from EMPLOYEES_OPTIONS is chosen
    """four options on how to list the employees, 1. Print pilots, 2. Print flight attendants, 3. Print all employees, 4. Print most experienced""" 
    
    def printing_crew(crew_list):
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
            list_employees()        


    display_options(LIST_EMPLOYEES_OPTIONS)
    action = str(input("Enter your action: ").lower())

    if action == "m":
        None
    
    elif action == "b":
        employees()

    elif action == "1": # print pilots
        print()
        print("All pilots:")
        print("-"*15)
        printing_crew(pilot_list)

    elif action == "2": # print flight attendants
        print()
        print("All flight attendants:")
        print("-"*15)
        printing_crew(flight_attendant_list)
        
    elif action == "3": # print all employees
        print()
        print("All employees:")
        print("-"*15)
        printing_crew(employee_list)

    elif action == "4": #TODO
        pass #print the most experienced

def employee_info(): #TODO
    employees_social_id = input("Enter the employees social ID")
    #print the name of the employee
    display_options(EMPLOYEE_INFORMATION_OPTIONS)
    action = str(input("Enter your action: ").lower())

    if action == "m":
        None

    elif action == "1":
        pass #print the employees info

    elif action == "2":
        display_options(CHANGE_EMPLOYEE_INFO_OPTIONS)
        action = str(input("Enter your action: ").lower())


def add_employee():
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

    # TODO
    employee = Employee(
        name=name, 
        socialID=social_id, 
        phonenumber=phone_number,
        role=work_title, 
        email=email,
        home_address=home_adress, 
        work_title=work_title,
        rank="TODO"
    )

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
            add_employee(employee)   

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
            add_employee(employee)   

#main
def employees():
    display_options(EMPLOYEES_OPTIONS)
    action = str(input("Enter your action: ").lower())

    if action == "m" or action == "b":
        None

    elif action == "1":
        list_employees()

    elif action == "2":
        employee_info()

    elif action == "3":
        add_employee()