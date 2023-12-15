from logic.logic_wrapper import LogicWrapper
from ui.menu_managerUI import Menu
from ui.airplaneUI import AirplaneUI
from ui.destinationsUI import DestinationsUI
from ui.employeesUI import EmployeeUI
from ui.scheduleUI import ScheduleUI
from ui.voyagesUI import VoyagesUI
from ui.flight_infoUI import FlightInfoUI

import time

INVALID_INPUT_SLEEP = 1
BACK = "b"
QUIT = "q"
INVALID_INPUT = "Input was invalid, try again."
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
                """TODO: in this code we are in airplanes and starting loops with the feature of backing out and quiting
                    we are storing the user inputs in a action variables and making sure the user puts the right input in:"""
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
                                                action4 = self.airplane_ui.pilots_by_license()
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
                                                            action12 = self.airplane_ui.list_pilots_by_license()
                                                        case "3":
                                                            action12 = self.airplane_ui.get_number_of_pilots_for_airplanes()
                                                        case "b":
                                                            continue
                                                        case _:
                                                            print("Input was invalid, try again ")
                                                            time.sleep(INVALID_INPUT_SLEEP)
                                                
                                        case "2":
                                            action3 = self.airplane_ui.types()
                                            if action3 == "q":
                                                quit()
                                            
                                        case "b":
                                            continue
                                        case _:
                                            print("Input was invalid, try again ")
                                            time.sleep(INVALID_INPUT_SLEEP)
                                        

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







# destinations
            def destinations_options_input(user_input):
                match user_input:
                    case "q":
                        quit(0)

                    case "1":
                        user_input = self.destinations_ui.get_all_destinations()

                    case "2":
                        user_input = self.destinations_ui.get_most_popular_destination()

                    case "3":
                        user_input = self.destinations_ui.add_destination()

                    case "4":
                        user_input = self.destinations_ui.change_destination_info()

                    case "b":
                        return BACK

                    case _:
                        print(INVALID_INPUT)
                        time.sleep(INVALID_INPUT_SLEEP)
                        return BACK
                    
                return user_input
                

            def destinations() -> None:
                """TODO: in this code we are in destination and starting loops with the feature of backing out and quiting
                    we are storing the user inputs in a action variables and making sure the user puts the right input in:"""
                
                user_input1 = ""
                user_input2 = BACK
                
                while user_input1 != BACK and user_input2 == BACK:
                    user_input1 = self.destinations_ui.destinations_options()

                    user_input2 = destinations_options_input(user_input1)

                    if user_input2 == "q":
                        quit()

                

            
                                
                                

            def employees() -> None:
                """TODO: in this code we are in employee and starting loops with the feature of backing out and quiting
                    we are storing the user inputs in a action variables and making sure the user puts the right input in:"""
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
                                            action11 = "b"
                                        
                        # Add employee :
                        case "3":
                            action11 = self.employee_ui.add_employee()
                            if action11 == "q":
                                quit()
                        
                        

# schedule                       
            def schedule_by_day():
                date = self.schedule_ui.get_schedule_by_day()
                
                user_input = BACK
                while user_input == BACK:
                    user_input = self.schedule_ui.schedule_for_a_day_options()

                    match user_input:
                        case "q":
                            quit()

                        case "b":
                            return BACK

                        case "1":
                            user_input = self.schedule_ui.who_was_working(date)
                        
                        case "2":
                            user_input = self.schedule_ui.get_who_was_not_working(date)

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input = BACK
                
                return user_input


            def schedule_by_employee():
                user_input = BACK
                while user_input == BACK:
                    user_input =self.schedule_ui.schedule_for_employee_options()

                    match user_input:
                        case "q":
                            quit()

                        case "b":
                            return BACK
                    
                        case "1":
                            employee = self.schedule_ui.get_employee()
                            user_input = self.schedule_ui.get_schedule_for_employee(employee)

                        case "2":
                            user_input = self.schedule_ui.get_total_hours_worked()

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input = BACK

                return user_input

            
            def schedule() -> None:
                """TODO: in this code we are in schedule and starting loops with the feature of backing out and quiting
                    we are storing the user inputs in a action variables and making sure the user puts the right input in:"""
                
                user_input1 = ""
                user_input2 = BACK

                while user_input1 != BACK and user_input2 == BACK:
                    user_input1 = self.schedule_ui.schedule_options()

                    match user_input1:
                        case "q":
                            quit()

                        case "b":
                            return BACK

                        case "1":
                            user_input2 = schedule_by_day()
                        
                        case "2":
                            user_input2 = schedule_by_employee()

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input2 = BACK
                    
                if user_input2 == "q":
                    quit()

                # action1 = ""# initialize a varible and stores the users input
                # action2 = ""
                # action12 = ""
                
                # while(action1 != BACK):
                #     action1 = self.schedule_ui.schedule_options()
                #     action12 = ""
                #     action2 = ""

                #     match action1:
                #         case "q":
                #             quit(0)

                #         case "1":
                #             while(action2 != BACK):
                                
                #                 date = self.schedule_ui.get_schedule_by_day()
                #                 action2 = self.schedule_ui.schedule_for_a_day_options()
                                
                #                 action12 = action2
                #                 if action12 == "q":
                #                     quit()
                #                 elif action12 == "b":
                #                     break

                #                 match action2:
                #                     case "q":
                #                         quit(0)
                #                     case "1":
                #                         action12 = self.schedule_ui.who_was_working(date)
                #                     case "2":
                #                         action12 = self.schedule_ui.get_who_was_not_working(date)
                #                     case "b":
                #                         continue
                #                     case _:
                #                         print("Input was invalid, try again ")
                #                         time.sleep(INVALID_INPUT_SLEEP)

                #                 action2 = action12


                        # case "2":
                        #     while(action12 != BACK):
                        #         action12 = self.schedule_ui.schedule_for_employee_options()
                        #         action2 = ""

                        #         match action12:
                        #             case "q":
                        #                 quit(0)
                        #             case "1":
                        #                 employee = self.schedule_ui.get_employee()
                        #                 action2 = self.schedule_ui.get_schedule_for_employee(employee)
                        #             case "2":
                        #                 action2 = self.schedule_ui.get_total_hours_worked()
                        #             case "b":
                        #                 continue
                        #             case _:
                        #                 print("Input was invalid, try again ")
                        #                 time.sleep(INVALID_INPUT_SLEEP)
                        # case "b":
                        #     continue
                        # case _:
                        #     print("Input was invalid, try again ")
                        #     time.sleep(INVALID_INPUT_SLEEP)
                                    
                                
                                
# voyages
            def voyages() -> None:
                """TODO: in this code we are in voyages and starting loops with the feature of backing out and quiting
                    we are storing the user inputs in a action variables and making sure the user puts the right input in:"""
                action1=""
                action2 = ""
                action14=""
                action15=""
                action16=""
                while(action1 != BACK):
                    action1 = self.voyages_ui.voyages_options()
                    action2 = ""
                    action3 = ""
                    action4 = ""
                    action5 = "b"
                    action6 = ""
                    action7 = "b"
                    action14 = "b"

                    match action1:
                        case "q":
                            quit(0)

                        case "1":
                            while(action2 != BACK):
                                action1 = ""
                                action2 = self.voyages_ui.add_voyage()
                                if action2 == "q":
                                    quit()

                        case "2":
                            while(action14 == BACK):
                                action14 = self.voyages_ui.voyage_past_or_present_options()
                                
                                match action14:

                                    case "q":
                                        quit(0)

                                    case "1":
                                        while(action5 == BACK):
                                            action4 = self.voyages_ui.list_voyage_options()
                                            
                                            match action4:
                                                case "q":
                                                    quit(0)

                                                case "1":
                                                    date = self.voyages_ui.get_date()
                                                    action5 = self.voyages_ui.get_upcoming_voyage_by_date(date)

                                                case "2":
                                                    year, week = self.voyages_ui.get_week()
                                                    action5 = self.voyages_ui.get_upcoming_voyage_by_week(year, week)

                                                case "b":
                                                    break

                                                case _:
                                                    print("Input was invalid, try again ")
                                                    time.sleep(INVALID_INPUT_SLEEP)


                                    case "2":
                                        while(action7 == BACK):
                                            action6 = self.voyages_ui.list_voyage_options()

                                            match action6:

                                                case "q":
                                                    quit(0)

                                                case "1":
                                                    date = self.voyages_ui.get_date()
                                                    action7 = self.voyages_ui.get_past_voyage_by_date(date)

                                                case "2":
                                                    year, week = self.voyages_ui.get_week()
                                                    action7 = self.voyages_ui.get_past_voyage_by_week(year, week)

                                                case "b":
                                                    break
                                                
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
                            self.voyages_ui.manager_staffs_voyage(voyage_number, voyage_date)
     
                            
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
