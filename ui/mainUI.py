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
                """ Calls a function that will print out a menu and return the users input and store it in the user_input. 
                It then matched the input with the right case and gets outputs from those functions and inputs that is restored in the user_input."""
                
                user_input = ""
                user_input2 = BACK

                while user_input != BACK and user_input2 == BACK:
                    user_input = self.airplane_ui.pilots_by_license()

                    match user_input:
                        case "q":
                            exit()

                        case "1":
                            user_input2 = self.airplane_ui.get_pilots_for_a_specific_type()

                        case "2":
                            user_input2 = self.airplane_ui.list_pilots_by_license()

                        case "3":
                            user_input2 = self.airplane_ui.get_number_of_pilots_for_airplanes()

                        case "b":
                            user_input = BACK

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input = BACK

                if user_input == QUIT or user_input2 == QUIT:
                    exit()

                return user_input2
            

            def airplane_types_and_license_options():
                """ This function is called if the user enters first 1 and that 1 again. Calls a function that will print out a menu 
                and return the users input. It then calls the right action according to the input and returns the input from that function."""
                
                user_input = "" # define a verible
                user_input2 = BACK # defult for the while loop does not go into the cases with the user_input2

                while user_input != BACK and user_input2 == BACK:
                    user_input = self.airplane_ui.airplane_types_and_licence()
                    
                    match user_input:
                        case "q":
                            exit()

                        case "1":
                            user_input2 = pilots_by_license_options()
                        
                        case "2":
                            user_input2 = self.airplane_ui.types()
                            
                        case "b":
                            user_input = BACK # if the input is "b" then it will go out of this loop and back to the function before with the menu before.

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input2 = BACK # if it is not a valid input than it will go and loop again

                if user_input == QUIT or user_input2 == QUIT:
                    exit()

                return user_input2


            def airplane_usage_options():
                """ This function is called if the user enters first 1 and that 3. Calls a function that will print out a menu 
                and return the users input. It then calls the right action according to the input and returns the input from that function."""

                user_input = ""
                user_input2 = BACK

                while user_input != BACK and user_input2 == BACK:
                    user_input = self.airplane_ui.airplane_usage_options()

                    match user_input:
                        case "q":
                            exit()

                        case "1":
                            user_input2 = self.airplane_ui.most_used_airplane() 

                        case "2":
                            user_input2 = self.airplane_ui.flown_furthest_airplane()

                        case "b":
                            user_input = BACK

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input2 = BACK
                
                if user_input2 == QUIT:
                    exit()
                    
                return user_input2


            def airplane() -> None:
                """In this code we are in airplanes and starting loops with the feature of backing out and quitting
                we are storing the user inputs in a user_input variables and making sure the user puts the right input in. 
                It then calls the right action according to the input"""
                
                user_input1 = ""
                user_input2 = BACK

                while user_input1 != BACK and user_input2 == BACK:
                    user_input1 = self.airplane_ui.airplane_options()
                    
                    match user_input1:
                        case "q": # quit feature for the system
                            exit()

                        case "1":  # airplane types and license
                            user_input2 = airplane_types_and_license_options()    
                                    
                        case "2":  # add new airplane
                            user_input2 = self.airplane_ui.add_airplane()
                                                
                        case "3":  # airplane usage
                            user_input2 = airplane_usage_options()

                        case "b":
                            user_input1 = BACK

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input1 = BACK

                if user_input1 == QUIT or user_input2 == QUIT:
                    exit()

                return user_input2


# destinations
            def destinations_options_input(user_input):
                """ Takes in the users input and calls the right functions to print everything out and return an input that is stored in the user_input. """

                match user_input:
                    case "q":
                        exit()

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
                """ Function that prints out the optins for destination and gets the user input and stored it in the user_input. Than calls another function
                to that will take care of printing out the right ting according to the input. """
                
                user_input1 = ""
                user_input2 = BACK
                
                while user_input1 != BACK and user_input2 == BACK:
                    user_input1 = self.destinations_ui.destinations_options()

                    user_input2 = destinations_options_input(user_input1)

                    if user_input2 == QUIT:
                        exit()


# employees
            def list_employees_opt():
                """ Prints out a menu and stores the input options in the user_input variable. From that input the right functions are called, 
                they will get an input and store it in the user_input2 """

                user_input = ""
                user_input2 = BACK

                while user_input != BACK and user_input2 == BACK:
                    user_input = self.employee_ui.list_employees_options()

                    match user_input:
                        case "q":
                            exit()
                        
                        case "1":
                            user_input2 = self.employee_ui.get_pilots()

                        case "2":
                            user_input2 = self.employee_ui.get_flight_attendants()

                        case "3":
                            user_input2 = self.employee_ui.get_all_employees()

                        case "4":
                            user_input2 = self.employee_ui.get_most_experienced()

                        case "b":
                            user_input = BACK

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input2 = BACK
                    
                if user_input == QUIT or user_input2 == QUIT:
                    exit()

                return user_input2
                    

            def employee_info_opt():
                """ Prints out a menu and stores the input in the user_input variable. From that input the right functions are called, 
                they will get an input and store it in the user_input2 """

                user_input = ""
                user_input2 = BACK

                while user_input != BACK and user_input2 == BACK:
                    user_input = self.employee_ui.employee_info_options()
                    
                    match user_input:
                        case "q":
                            exit()

                        case "1":
                            user_input2 = self.employee_ui.get_info()
                        
                        case "2": #TODO laga back og quit TINNA
                            user_input2 = self.employee_ui.change_info_options()
                        
                        case "b":
                            user_input = BACK

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input2 = BACK

                if user_input == QUIT or user_input2 == QUIT:
                    exit()

                return user_input2


            def employees() -> None:
                """ In this code we are in employee and starting loops with the feature of backing out and quitting. This function will call a 
                function that prints out tha options for employee and than get an input that is returned and stored in the user_input. Then it calls 
                the right function from the userss input. """
                
                user_input = ""
                user_input2 = BACK

                while user_input != BACK and user_input2 == BACK:
                    user_input = self.employee_ui.employees_options()
                    
                    match user_input:
                        case "q":
                            exit()

                        case "1":
                            user_input2 = list_employees_opt()

                        case "2":
                            user_input2 = employee_info_opt()
                                        
                        case "3":

                            user_input2 = self.employee_ui.add_employee()
                        
                        case "b":
                            user_input = BACK

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input2 = BACK
                            
                if user_input == QUIT or user_input2 == QUIT:
                    exit()
                
                return user_input2
                        
# schedule                       
            def schedule_by_day():
                """ Gets a date form the input. Prints out a menu and stores the input in the user_input variable. From that input the right functions are called, 
                they will get an input and store it in the user_input2 """
                
                date = self.schedule_ui.get_schedule_by_day()
                
                user_input = ""
                user_input2 = BACK

                while user_input != BACK and user_input2 == BACK:
                    user_input = self.schedule_ui.schedule_for_a_day_options(date)

                    match user_input:
                        case "q":
                            exit()

                        case "b":
                            user_input = BACK

                        case "1":
                            user_input2 = self.schedule_ui.who_was_working(date)
                        
                        case "2":
                            user_input2 = self.schedule_ui.get_who_was_not_working(date)

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input2 = BACK
                
                if user_input == QUIT or user_input2 == QUIT:
                    exit()

                return user_input2


            def schedule_by_employee():
                """ Prints out a menu and stores the input in the user_input variable. From that input the right functions are called, 
                they will get an input and store it in the user_input2 """

                user_input = ""
                user_input2 = BACK

                while user_input != BACK and user_input2 == BACK:
                    user_input =self.schedule_ui.schedule_for_employee_options()

                    match user_input:
                        case "q":
                            exit()

                        case "b":
                            user_input = BACK
                    
                        case "1":
                            employee = self.schedule_ui.get_employee()
                            user_input2 = self.schedule_ui.get_schedule_for_employee(employee)

                        case "2":
                            user_input2 = self.schedule_ui.get_total_hours_worked()

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input2 = BACK
                    
                if user_input == QUIT or user_input2 == QUIT:
                    exit()

                return user_input2

            
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
                            user_input1 = BACK

                        case "1":
                            user_input2 = schedule_by_day()
                        
                        case "2":
                            user_input2 = schedule_by_employee()

                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(INVALID_INPUT_SLEEP)
                            user_input2 = BACK
                    
                if user_input2 == QUIT or user_input1 == QUIT:
                    exit()    

                return user_input2                                
                                
                                
# voyages
            def voyages() -> None:
                """In this code we are in voyages and starting loops with the feature of backing out and quiting
                we are storing the inputs in a user_input variables and making sure the user puts the right input in. 
                From that input it will match it with the right case and continue doing that."""
                
                user_input1 = ""
                user_input2 = ""
                user_input3 = ""

                while(user_input1 != BACK):
                    user_input1 = self.voyages_ui.voyages_options()
                    user_input2 = ""
                    user_input4 = ""
                    user_input5 = ""
                    user_input6 = ""
                    user_input7 = ""
                    user_input3 = ""

                    match user_input1:
                        case "q":
                            exit()

                        case "1":
                            while(user_input2 != BACK):
                                user_input1 = ""
                                user_input2 = self.voyages_ui.add_voyage()
                                
                                if user_input2 == QUIT:
                                    exit()

                        case "2":
                            while(user_input3 != BACK):
                                user_input3 = self.voyages_ui.voyage_past_or_present_options()
                                
                                match user_input3:

                                    case "q":
                                        exit()

                                    case "1":
                                        user_input5 = BACK
                                        while(user_input5 == BACK):
                                            user_input4 = self.voyages_ui.list_voyage_options()
                                            
                                            match user_input4:
                                                case "q":
                                                    exit()

                                                case "1":
                                                    date = self.voyages_ui.get_date()
                                                    user_input5 = self.voyages_ui.get_upcoming_voyage_by_date(date)

                                                case "2":
                                                    year, week = self.voyages_ui.get_week()
                                                    user_input5 = self.voyages_ui.get_upcoming_voyage_by_week(year, week)

                                                case "b":
                                                    break

                                                case _:
                                                    print("Input was invalid, try again ")
                                                    time.sleep(INVALID_INPUT_SLEEP)


                                    case "2":
                                        user_input7 = BACK
                                        while(user_input7 == BACK):
                                            user_input6 = self.voyages_ui.list_voyage_options()

                                            match user_input6:

                                                case "q":
                                                    exit()

                                                case "1":
                                                    date = self.voyages_ui.get_date()
                                                    user_input7 = self.voyages_ui.get_past_voyage_by_date(date)

                                                case "2":
                                                    year, week = self.voyages_ui.get_week()
                                                    user_input7 = self.voyages_ui.get_past_voyage_by_week(year, week)

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

            

# Flight information
            def flight_status() -> None:
                """If the user chooses to see the flight information. This function calls a function in the flight information UI
                 and will print out a table that shows the flight status."""
                
                user_input = self.flight_info.get_flight_status() 

                if user_input == QUIT:
                    exit()


# Main menu
            options = {
                "1": airplane,
                "2": destinations,
                "3": employees,
                "4": schedule,
                "5": voyages,
                "6": flight_status,
            }


            action = input("Enter your action: ").lower().strip()

            while not self.validation.validate_choice(action, len(options)):
                print("Invalid action! \nTry again.")
                action = input("Enter your action: ").lower().strip()

            options[action]()