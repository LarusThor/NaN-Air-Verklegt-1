from logic.logic_wrapper import LogicWrapper
from ui.menu_managerUI import Menu
from ui.airplaneUI import AirplaneUI
from ui.destinationsUI import DestinationsUI
from ui.employeesUI import EmployeeUI
from ui.scheduleUI import ScheduleUI
from ui.voyagesUI import VoyagesUI
from ui.flight_infoUI import FlightInfoUI

import time

INVALID_INPUT_SLEEP = 2
BACK = "b"
QUIT = "q"
# the menu
MAIN_MENU_OPTIONS = [
    "1. Airplane",
    "2. Destinations",
    "3. Employees",
    "4. Schedule",
    "5. Voyages",
    "6. Flight status",
]


class Main:
    def __init__(self) -> None:
        """TODO: add docstring"""
        self.menus = Menu()
        self.airplane_ui = AirplaneUI()
        self.destinations_ui = DestinationsUI()
        self.employee_ui = EmployeeUI()
        self.schedule_ui = ScheduleUI()
        self.voyages_ui = VoyagesUI()
        self.flight_info = FlightInfoUI()
        self.logic_wrapper = LogicWrapper()
        self.validation = self.logic_wrapper.validation

    def input_prompt(self) -> None:
        """ TODO: add docstring"""
        while True:
            self.menus.main_menu()
            

            def airplane() -> None:
                """TODO: in this code we are in airplanes and starting loops 
                    with the feature of backing out and quiting
                    we are storing the user inputs in a action variables 
                    and making sure the user puts the right input in:"""
                action1 = "" # initialize a varible and stores the users input
                action2 = ""
                action3 = ""
                action4 = ""
                action15 = ""
                while (action1 != BACK):
                    action1 = self.airplane_ui.airplane_options()
                    action2 = ""
                    action3 = ""
                    action4 = ""
                    action15 = ""
                    
                    match action1:
                        case "q":# quit feature for the system
                            quit(0)

                        case "1":  # airplane types and license
                            while( action2 != BACK):
                                action3 = ""
                                while (action3 != BACK):
                                    action2 = self.airplane_ui.airplane_types_and_licence()
                                    action3 = action2
                                    if action3 == "q":
                                        quit()
                                    match action2:
                                        case "q":
                                            quit(0)

                                        case "1":
                                            while(action4 != BACK):
                                                action2 = ""
                                                action4 = self.airplane_ui.pilots_by_licanse()
                                                action12 = action4
                                                while(action12 != BACK):
                                                    if action12 == "q":
                                                        quit()
                                                    match action4:
                                                        case "q":
                                                            quit(0)
                                                        case "1":
                                                            action12 = self.airplane_ui.get_pilots_for_a_specific_type()
                                                        case "2":
                                                            action12 = self.airplane_ui.list_pilots_by_licanse()
                                                        case "3":
                                                            action12 = self.airplane_ui.get_number_of_pilots_for_airplanes()
                                                        case "b":
                                                            continue
                                                        case _:
                                                            print("Input was invalid, try again ")
                                                            time.sleep(INVALID_INPUT_SLEEP)
                                                #end match action 3
                                            #end w-action3
                                        #end case action2=1
                                        case "2":
                                            action3 = self.airplane_ui.types()
                                            if action3 == "q":
                                                quit()
                                            
                                        case "b":
                                            continue
                                        case _:
                                            print("Input was invalid, try again ")
                                            time.sleep(INVALID_INPUT_SLEEP)
                                        #end case action2=2
                                        
                                    #end match a2
                                #end w-a2
                            #case action1=1

                        case "2":  # add new airplane
                            action2 = self.airplane_ui.add_airplane()
                            if action2 == "q":
                                quit()
                        
                        #case action1=2
                        
                        case "3":  # airplane usage
                            while(action15 != "b"):
                                action15 = ""
                                action15 = self.airplane_ui.airplane_usage_options()
                                action14 = action15.lower()

                                while(action14 != BACK):
                                    
                                    match action14:
                                        case "q":
                                            quit(0)
                                        case "1":
                                            action14 = self.airplane_ui.most_used_airplane() 
                                        case "2":
                                            action14 = self.airplane_ui.flown_furthest_airplane()
                                        case "b":
                                            continue
                                        case _:
                                            print("Input was invalid, try again ")
                                            time.sleep(INVALID_INPUT_SLEEP)
                        case "b":
                            continue
                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)


            def destinations() -> None:
                """TODO: in this code we are in destination and starting loops 
                    with the feature of backing out and quiting
                    we are storing the user inputs in a action variables 
                    and making sure the user puts the right input in:"""
                action4 = ""# initialize a varible and stores the users input
                action5 = ""
                while ( action4 != BACK):
                    action4 = self.destinations_ui.destinations()
                    action5 = ""
                    
                    while(action5 != BACK):
                        if action5 == "q":
                            quit()
                        match action4:
                            case "q":
                                quit(0)
                            case "1":
                                action5 = self.destinations_ui.get_all_destinations()

                            case "2":
                                action5 = self.destinations_ui.get_most_popular_destination()

                            case "3":
                                action5 = self.destinations_ui.add_destination()

                            case "4":
                                # while (action5 != "b"):
                                action5 = self.destinations_ui.change_destination_info()

                            case "b":
                                continue
                            case _:
                                print("Input was invalid, try again ")
                                time.sleep(INVALID_INPUT_SLEEP)
                                
                                

            def employees() -> None:
                """TODO: in this code we are in employee and starting loops 
                    with the feature of backing out and quiting
                    we are storing the user inputs in a action variables 
                    and making sure the user puts the right input in:"""
                action6 = ""# initialize a varible and stores the users input
                action7 = ""
                action8 = ""
                action10 = ""
                while (action6 != BACK):
                    action6 = self.employee_ui.employees_options()
                    action7 = ""
                    action10 = ""
                    match action6:
                        case "q":
                            quit(0)
                    # list employees :
                        case "1":
                            while(action7 != BACK):
                                # action6 =""
                                action7 = self.employee_ui.list_employees_options()
                                action10 = action7
                                while(action10 != BACK):
                                    if action10 == "q":
                                        quit()
                                    match action7:
                                        case "q":
                                            quit(0)
                                        
                                        case "1":
                                            action10 = self.employee_ui.get_pilots()
                                        case "2":
                                            action10 = self.employee_ui.get_flight_attendants()
                                        case "3":
                                            action10 = self.employee_ui.get_all_employees()
                                        case "4":
                                            action10 = self.employee_ui.get_most_experienced()
                                        case "b":
                                            continue
                                        case _:
                                            print("Input was invalid, try again ")
                                            time.sleep(INVALID_INPUT_SLEEP)

                    # Employee info :
                        case "2":
                            action8 = ""
                            while(action8 != BACK):
                                action8 = self.employee_ui.employee_info_options()
                                action11 = action8
                                while(action11 != "b"):
                                    match action11:
                                        case "q":
                                            quit(0)

                                        case "1":
                                            action11 = self.employee_ui.get_info()
                                        

                                        case "2": #TODO laga back og quit TINNA
                                            action11 = self.employee_ui.change_info_options()

                                        case _:
                                            print("Input was invalid, try again ")
                                            time.sleep(INVALID_INPUT_SLEEP)
                                        
                        # Add employee :
                        case "3":
                            action11 = self.employee_ui.add_employee()
                            if action11 == "q":
                                quit()
                        
                        
                        

            def schedule() -> None:
                """TODO: in this code we are in schedule and starting loops 
                    with the feature of backing out and quiting
                    we are storing the user inputs in a action variables 
                    and making sure the user puts the right input in:"""
                action1 = ""# initialize a varible and stores the users input
                action2 = ""
                action12 = ""
                
                while(action1 != BACK):
                    action1 = self.schedule_ui.schedule_options()
                    action12 = ""
                    action2 = ""

                    match action1:
                        case "q":
                            quit(0)

                        case "1":
                            while(action2 != BACK):
                                
                                date = self.schedule_ui.get_schedule_by_day()
                                action2 = self.schedule_ui.schedule_for_a_day_options()
                                
                                action12 = action2
                                if action12 == "q":
                                    quit()
                                elif action12 == "b":
                                    break

                                match action2:
                                    case "q":
                                        quit(0)
                                    case "1":
                                        action12 = self.schedule_ui.who_was_working(date)
                                    case "2":
                                        action12 = self.schedule_ui.get_who_was_not_working(date)
                                    case "b":
                                        continue
                                    case _:
                                        print("Input was invalid, try again ")
                                        time.sleep(INVALID_INPUT_SLEEP)

                                action2 = action12
                                

                        case "2":
                            while(action12 != BACK):
                                action12 = self.schedule_ui.schedule_for_employee_options()
                                action2 = ""

                                match action12:
                                    case "q":
                                        quit(0)
                                    case "1":
                                        employee = self.schedule_ui.get_employee()
                                        action2 = self.schedule_ui.get_schedule_for_employee(employee)
                                    case "2":
                                        action2 = self.schedule_ui.get_total_hours_worked()
                                    case "b":
                                        continue
                                    case _:
                                        print("Input was invalid, try again ")
                                        time.sleep(INVALID_INPUT_SLEEP)
                        case "b":
                            continue
                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                                    
                                
                                

            def voyages() -> None:
                """TODO: in this code we are in voyages and starting loops 
                    with the feature of backing out and quiting
                    we are storing the user inputs in a action variables 
                    and making sure the user puts the right input in:"""
                action13=""
                action14=""
                action15=""
                action16=""
                while(action13 != BACK):
                    action14=""
                    action15=""
                    action16=""
                    action = self.voyages_ui.voyages_options()
                    match action:
                        case "q":
                            quit(0)
                        case "1":
                            self.voyages_ui.add_voyage()

                        case "2":
                            while(action14 != BACK):
                                action13=""
                                action14 = self.voyages_ui.voyage_past_or_present_options()
                                match action14:
                                    case "q":
                                        quit(0)
                                    case "1":
                                        while(action15 != BACK):
                                            action15 = self.voyages_ui.list_voyage_options()
                                            match action15:
                                                case "q":
                                                    quit(0)
                                                case "1":
                                                    date = self.voyages_ui.get_date()
                                                    self.voyages_ui.get_upcoming_voyage_by_date(
                                                        date
                                                    )
                                                case "2":
                                                    year, week = self.voyages_ui.get_week()
                                                    self.voyages_ui.get_upcoming_voyage_by_week(
                                                        year, week
                                                    )
                                                case "b":
                                                    continue
                                                case _:
                                                    print("Input was invalid, try again ")
                                                    time.sleep(INVALID_INPUT_SLEEP)    

                                    case "2":
                                        while(action16 != BACK):
                                            action16 = self.voyages_ui.list_voyage_options()
                                            match action16:
                                                case "q":
                                                    quit(0)
                                                case "1":
                                                    date = self.voyages_ui.get_date()
                                                    self.voyages_ui.get_past_voyage_by_date(date)
                                                case "2":
                                                    year, week = self.voyages_ui.get_week()
                                                    self.voyages_ui.get_past_voyage_by_week(
                                                        year, week
                                                    )
                                                case "b":
                                                    continue
                                                case _:
                                                    print("Input was invalid, try again ")
                                                    time.sleep(INVALID_INPUT_SLEEP)
                                                    
                                                    
                                    case "b":
                                        continue
                                    case _:
                                        print("Input was invalid, try again ")
                                        time.sleep(INVALID_INPUT_SLEEP)
                        case "3":
                            voyage_number = self.voyages_ui.get_voyage_flight_number()
                            voyage_date = self.voyages_ui.get_voyage_date()
                            self.voyages_ui.manager_staffs_voyage(
                                voyage_number, voyage_date
                            )
     
                        case "4":
                            self.voyages_ui.staff_voyage()
                            
                        case "b":
                            continue
                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)

            def flight_status() -> None:
                """If the user chooses to see the flight information. This function calls a function in the flight information UI
                 and will print out a table that shows the flight status."""
                
                user_input = self.flight_info.get_flight_status() #TODO validate, can just be b or q
                if user_input == "q":
                    quit()


            options = {
                "1": airplane,
                "2": destinations,
                "3": employees,
                "4": schedule,
                "5": voyages,
                "6": flight_status,
            }

            action = str(input("Enter your action: ").lower())
            while not self.validation.validate_choice(action, len(options)):
                print("Invalid action! \nTry again.")
                action = str(input("Enter your action: ").lower())

            options[action]()
