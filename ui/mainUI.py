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
    """"Instantiate a Main object."""
    def __init__(self) -> None:
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
        """Takes care of calling all options based on user input and calling the correct function."""
        while True:
            self.menus.main_menu()
            

# airplanes
            def pilots_by_license_options():
                user_input = ""

                while user_input != BACK:

                    user_input = self.airplane_ui.pilots_by_license()

                    match user_input:
                        case "1":
                            user_input = self.airplane_ui.get_pilots_for_a_specific_type()

                        case "2":
                            user_input = self.airplane_ui.list_pilots_by_license()

                        case "3":
                            user_input = self.airplane_ui.get_number_of_pilots_for_airplanes()

                        case "b":
                            user_input = BACK

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input = BACK

                if user_input == "q":
                    quit()

                return user_input
            

            def airplane_types_and_license_options():

                user_input = ""
                user_input2 = BACK

                while user_input != BACK and user_input2 == BACK:
                    user_input = self.airplane_ui.airplane_types_and_licence()
                    
                    match user_input:
                        case "q":
                            quit(0)

                        case "1":
                            user_input2 = pilots_by_license_options()
                        
                        case "2":
                            user_input2 = self.airplane_ui.types()
                            
                            
                        case "b":
                            user_input = BACK

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input = BACK

                if user_input == "q" or user_input2 == "q":
                    quit()

                return user_input


            def airplane_usage_options():
                user_input = ""
                user_input2 = BACK

                while user_input != BACK and user_input2 == BACK:
                    user_input = self.airplane_ui.airplane_usage_options()

                    match user_input:
                        case "q":
                            quit(0)

                        case "b":
                            user_input = BACK

                        case "1":
                            user_input2 = self.airplane_ui.most_used_airplane() 

                        case "2":
                            user_input2 = self.airplane_ui.flown_furthest_airplane()

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input = BACK
                
                if user_input2 == "q":
                    quit()
                    
                return user_input


            def airplane() -> None:
                """In this code we are in airplanes and starting loops with the feature of backing out and quiting
                    we are storing the user inputs in a action variables and making sure the user puts the right input in:"""
                
                user_input1 = ""
                user_input2 = BACK

                while user_input1 != BACK and user_input2 == BACK:
                    user_input1 = self.airplane_ui.airplane_options()
                    
                    match user_input1:
                        case "q":# quit feature for the system
                            quit(0)

                        case "1":  # airplane types and license
                            user_input2 = airplane_types_and_license_options()
                                    
                                    
                        case "2":  # add new airplane
                            user_input2 = self.airplane_ui.add_airplane()
                                                
                        case "3":  # airplane usage
                            user_input2 = airplane_usage_options()

                        case "b":
                            continue

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)

                if user_input1 == "q" or user_input2 == "q":
                    quit()

                return user_input1


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
                """TODO: in this code we are in destination and starting loops with the feature of backing out and quitting
                    we are storing the user inputs in a action variables and making sure the user puts the right input in:"""
                
                user_input1 = ""
                user_input2 = BACK
                
                while user_input1 != BACK and user_input2 == BACK:
                    user_input1 = self.destinations_ui.destinations_options()

                    user_input2 = destinations_options_input(user_input1)

                    if user_input2 == "q":
                        quit()

                

# employees

            def list_employees_opt():
                user_input = BACK
                user_input2 = ""

                while user_input == BACK and user_input2 != BACK:
                    user_input = self.employee_ui.list_employees_options()

                    match user_input:
                        case "q":
                            quit(0)
                        
                        case "1":
                            user_input2 = self.employee_ui.get_pilots()

                        case "2":
                            user_input2 = self.employee_ui.get_flight_attendants()

                        case "3":
                            user_input2 = self.employee_ui.get_all_employees()

                        case "4":
                            user_input2 = self.employee_ui.get_most_experienced()

                        case "b":
                            user_input2 = BACK

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input2 = BACK
                    
                    if user_input == "q" or user_input2 == "q":
                        quit()

                return user_input2
                    

            def employee_info_opt():
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


            def employees() -> None:
                """In this code we are in employee and starting loops with the feature of backing out and quiting
                    we are storing the user inputs in a action variables and making sure the user puts the right input in:"""
                
                user_input = ""
                user_input2 = BACK
                while user_input != BACK and user_input2 == BACK:

                    user_input = self.employee_ui.employees_options()
                    
                    match user_input:
                        case "q":
                            quit(0)

                        case "1":
                            user_input2 = list_employees_opt()

                        case "2":
                            user_input2 = employee_info_opt()
                                        
                        case "3":

                            user_input2 = self.employee_ui.add_employee()
                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input = BACK
                            
                    if user_input == "q":
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
                """In this code we are in schedule and starting loops with the feature of backing out and quiting
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
                                
                                # action12 = action2
                                # if action12 == "q":
                                #     quit()
                                # elif action12 == "b":
                                #     break

                                # match action2:
                                #     case "q":
                                #         quit(0)
                                #     case "1":
                                #         action12 = self.schedule_ui.who_was_working(date)
                                #     case "2":
                                #         action12 = self.schedule_ui.get_who_was_not_working(date)
                                #     case "b":
                                #         continue
                                #     case _:
                                #         print("Input was invalid, try again ")
                                #         time.sleep(INVALID_INPUT_SLEEP)

                                # action2 = action12


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
                """In this code we are in voyages and starting loops with the feature of backing out and quiting
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
                    action14 = ""

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
                            while(action14 != BACK):
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
                                        break

                                    case _:
                                        print("Input was invalid, try again ")
                                        time.sleep(INVALID_INPUT_SLEEP)


                        case "3":
                            voyage_number = self.voyages_ui.get_voyage_flight_number()
                            voyage_date = self.voyages_ui.get_voyage_date()
                            self.voyages_ui.manager_staffs_voyage(voyage_number, voyage_date)
     
                            
                        case "b":
                            break

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)

            


            def flight_status() -> None:
                """If the user chooses to see the flight information. This function calls a function in the flight information UI
                 and will print out a table that shows the flight status."""
                
                user_input = self.flight_info.get_flight_status() 

                if user_input == "q":
                    quit()



# Main menu
            options = {
                "1": airplane,
                "2": destinations,
                "3": employees,
                "4": schedule,
                "5": voyages,
                "6": flight_status,
            }


            action = input("Enter your action: ").lower()

            while not self.validation.validate_choice(action, len(options)):
                print("Invalid action! \nTry again.")
                action = input("Enter your action: ").lower()

            options[action]()
