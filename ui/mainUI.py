from logic.logic_wrapper import LogicWrapper
from ui.menu_managerUI import Menu
from ui.airplaneUI import AirplaneUI
from ui.destinationsUI import DestinationsUI
from ui.employeesUI import EmployeeUI
from ui.scheduleUI import ScheduleUI
from ui.voyagesUI import VoyagesUI
from ui.flight_infoUI import FlightInfoUI

import time

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
        while True:
            self.menus.main_menu()
            

            def airplane() -> None:
                """TODO: add docstring og kommenta þennan kóða hann er svoldið flókinn :"""
                action1 = ""
                action2 = ""
                action3 = ""
                action4 = ""
                while (action1 != 'b'):
                    action2= ""
                    action4= ""
                    action1 = self.airplane_ui.airplane_options()
                    match action1:
                        case "q":
                            quit(0)
                        case "1":  # airplane types and license
                            while( action2 != 'b' ):
                                action3 = ""
                                action2 = self.airplane_ui.airplane_types_and_licence()
                                match action2:
                                    case "q":
                                        quit(0)
                                    case "1":
                                        while( action3 != 'b'):
                                            action3 = self.airplane_ui.pilots_by_licanse()
                                            match action3:
                                                case "q":
                                                    quit(0)
                                                case "1":
                                                    self.airplane_ui.get_pilots_for_a_specific_type()
                                                case "2":
                                                    self.airplane_ui.list_pilots_by_licanse()
                                                case "3":
                                                    self.airplane_ui.get_number_of_pilots_for_airplanes()
                                                case "b":
                                                    continue
                                                case _:
                                                    print("Input was invalid, try again ")
                                                    time.sleep(3)
                                            #end match action 3
                                        #end w-action3
                                    #end case action2=1
                                    case "2":
                                        self.airplane_ui.types()
                                        
                                    case "b":
                                        continue
                                    case _:
                                        print("Input was invalid, try again ")
                                        time.sleep(3)
                                    #end case action2=2
                                    
                                #end match a2
                            #end w-a2
                        #case action1=1
                        case "2":  # add new airplane
                            self.airplane_ui.add_airplane()
                        
                        #case action1=2
                        
                        case "3":  # airplane usage
                            while(action4 != "b"):
                                action1= ""
                                action4 = self.airplane_ui.airplane_usage_options()
                                match action4:
                                    case "q":
                                        quit(0)
                                    case "1":
                                        self.airplane_ui.most_used_airplane()
                                    case "2":
                                        self.airplane_ui.flown_furthest_airplane()
                                    case "b":
                                        continue
                                    case _:
                                        print("Input was invalid, try again ")
                                        time.sleep(3)
                        case "b":
                            continue
                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(3)


            def destinations() -> None:
                action4 = ""
                action5 = ""
                while ( action4 != "b"):
                    action4 = self.destinations_ui.destinations()
                    match action4:
                        case "q":
                            quit(0)
                        case "1":
                            action4 = self.destinations_ui.get_all_destinations()

                        case "2":
                            self.destinations_ui.get_most_popular_destination()

                        case "3":
                            self.destinations_ui.add_destination()

                        case "4":
                            while (action5 != "b"):
                                action5 = self.destinations_ui.select_info()
                                action4 = ""
                                
                                match action5:
                                    case "q":
                                        quit(0)
                                    case "1":
                                        self.destinations_ui.change_destination_info()

                                    case "2":
                                        self.destinations_ui.change_contact_info()

                                    case "3":
                                        self.destinations_ui.change_airport_info()
                                    
                                    case "b":
                                        continue
                                    case _:
                                        print("Input was invalid, try again ")
                                        time.sleep(3)
                        case "b":
                            continue
                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(3)
                                
                                
                                

            def employees() -> None:
                action6 = ""
                action7 = ""
                action8 = ""
                action9 = ""
                while (action6 != "b"):
                    action7 = ""
                    action8 = ""
                    action9 = ""
                    action6 = self.employee_ui.employees_options()
                    match action6:
                        case "q":
                            quit(0)
                    # list employees :
                        case "1":
                            while(action7 != "b"):
                                action6 =""
                                action7 = self.employee_ui.list_employees_options()
                                match action7:
                                    case "q":
                                        quit(0)
                                    # elif action == "b":
                                    #employees()
                                    case "1":
                                        action7 = self.employee_ui.get_pilots()
                                        print(action7)
                                        if action7 == "q":
                                            quit(0)
                                    # EmployeesUI.print_crew(self.pilots_list)
                                    case "2":
                                        self.employee_ui.get_flight_attendants()
                                    case "3":
                                        self.employee_ui.get_all_employees()
                                    case "4":
                                        self.employee_ui.get_most_experienced()
                                    case "b":
                                        continue
                                    case _:
                                        print("Input was invalid, try again ")
                                        time.sleep(3)

                    # Employee info :
                        case "2":
                            while(action8 != "b"):
                                action6 = ""
                            # employee_name = self.employee_ui.get_employee()
                                action8 = self.employee_ui.employee_info_options()

                                match action8:
                                    case "q":
                                        quit(0)

                                    case "1":
                                        self.employee_ui.get_info()
                                    

                                    case "2":
                                        while(action9 != "b"):
                                            action8 = ""
                                            action9 = self.employee_ui.change_info_options()

                                            match action9:
                                                case "q":
                                                    quit(0)
                                                case "1":
                                                    self.employee_ui.change_home_address()
                                                case "2":
                                                    self.employee_ui.change_phone_number()
                                                case "3":
                                                    self.employee_ui.change_email()
                                                case "b":
                                                    continue
                                                case _:
                                                    print("Input was invalid, try again ")
                                                    time.sleep(3)
                                    case "b":
                                        continue
                                    case _:
                                        print("Input was invalid, try again ")
                                        time.sleep(3)
                                        
                        # Add employee :
                        case "3":
                            self.employee_ui.add_employee()
                        
                        
                        

            def schedule() -> None:
                action10= ""
                action11 = ""
                action12 = ""
                while(action10 != "b"):
                    action12 =""
                    action10 = self.schedule_ui.schedule_options()

                    match action10:
                        case "q":
                            quit(0)
                        case "1":
                            while(action11 != "b"):
                                action10=""
                                action11=""
                                date = self.schedule_ui.get_schedule_by_day()
                                action11 = self.schedule_ui.schedule_for_a_day_options()

                                match action11:
                                    case "q":
                                        quit(0)
                                    case "1":
                                        self.schedule_ui.who_was_working(date)
                                    case "2":
                                        self.schedule_ui.get_who_was_not_working(date)
                                    case "b":
                                        continue
                                    case _:
                                        print("Input was invalid, try again ")
                                        time.sleep(3)
                                

                        case "2":
                            while(action12 != "b"):
                                action11=""
                                action10=""
                                action12 = self.schedule_ui.schedule_for_employee_options()
                                match action12:
                                    case "q":
                                        quit(0)
                                    case "1":
                                        employee = self.schedule_ui.get_employee()
                                        self.schedule_ui.get_schedule_for_employee(employee)
                                    case "2":
                                        self.schedule_ui.get_total_hours_worked()
                                    case "b":
                                        continue
                                    case _:
                                        print("Input was invalid, try again ")
                                        time.sleep(3)
                        case "b":
                            continue
                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(3)
                                    
                                
                                

            def voyages() -> None:
                action13=""
                action14=""
                action15=""
                action16=""
                while(action13 != "b"):
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
                            while(action14 != "b"):
                                action13=""
                                action14 = self.voyages_ui.voyage_past_or_present_options()
                                match action14:
                                    case "q":
                                        quit(0)
                                    case "1":
                                        while(action15 != "b"):
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
                                                    time.sleep(3)    

                                    case "2":
                                        while(action16 != "b"):
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
                                                    time.sleep(3)
                                                    
                                                    
                                    case "b":
                                        continue
                                    case _:
                                        print("Input was invalid, try again ")
                                        time.sleep(3)
                        case "3":
                            voyage_number = self.voyages_ui.get_voyage_flight_number()
                            voyage_date = self.voyages_ui.get_voyage_date()
                            self.voyages_ui.manager_staffs_voyage(
                                voyage_number, voyage_date
                            )
                            # return_voyage_number, return_voyage_date = self.logic_wrapper.voyage_info_for_return_flight(voyage_number, voyage_date)
                            # return_voyage_date = return_voyage_date.strftime("%Y-%m-%d")
                            # self.voyages_ui.manager_staffs_voyage(return_voyage_number, return_voyage_date)

                        case "4":
                            self.voyages_ui.staff_voyage()
                            
                        case "b":
                            continue
                        case _:
                            print("Input was invalid, try again ")
                            time.sleep(3)

            def flight_status() -> None:
                """If the user chooses to see the flight information. This function calls a function in the flight information UI
                 and will print out a table that shows the flight status."""
                
                self.flight_info.get_flight_status()


            options = {
                "1": airplane,
                "2": destinations,
                "3": employees,
                "4": schedule,
                "5": voyages,
                "6": flight_status,
            }

            action = str(input("Enter your action: ").lower())
            while not self.validation.validate_action(action, len(options)):
                print("Invalid action! \nTry again.")
                action = str(input("Enter your action: ").lower())

            options[action]()
