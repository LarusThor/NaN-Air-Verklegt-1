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
    "6. Flight information",
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

    def input_prompt(self) -> None:
        """TODO: add docstring"""
        while True:
            self.menus.main_menu()
            action = str(input("Enter your action: ").lower())

            def airplane() -> None:
                """ TODO: add docstring """
                action1 = ""
                action2 = ""
                action3 = ""
                while (action1 != 'b'):
                    action1 = self.airplane_ui.airplane()
                    match action1:
                        case "q":
                            quit(0)
                        case "1":  # airplane types and license
                            while( action2 != 'b' ):
                                action2 = self.airplane_ui.airplane_types_and_licanse()
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
                            action = self.airplane_ui.airplane_usage_options()
                            match action:
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
                """TODO: add docstring"""
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
                """TODO: add docstring"""
                action = self.employee_ui.employees_options()

                match action:
                    case "m", "b":
                        pass

                    # list employees :
                    case "1":
                        action = self.employee_ui.list_employees_options()

                        match action:
                            case "m":
                                pass
                            # elif action == "b":
                            #     employees()
                            case "1":
                                self.employee_ui.get_pilots()
                                # EmployeesUI.print_crew(self.pilots_list)
                            case "2":
                                self.employee_ui.get_flight_attendants()
                            case "3":
                                self.employee_ui.get_all_employees()
                            case "4":
                                self.employee_ui.get_most_experienced()

                    # Employee info :
                    case "2":
                        # employee_name = self.employee_ui.get_employee()
                        action = self.employee_ui.employee_info_options()

                        match action:
                            case "m":
                                # TODO: ???
                                pass

                            case "1":
                                self.employee_ui.get_info()

                            case "2":
                                action = self.employee_ui.change_info_options()

                                match action:
                                    case "1":
                                        self.employee_ui.change_home_address()
                                    case "2":
                                        self.employee_ui.change_phone_number()
                                    case "3":
                                        self.employee_ui.change_email()

                    # Add employee :
                    case "3":
                        self.employee_ui.add_employee()

            def schedule() -> None:
                """TODO: add docstring"""
                action = self.schedule_ui.schedule_options()

                match action:
                    case "1":
                        date = self.schedule_ui.get_schedule_by_day()
                        action = self.schedule_ui.schedule_for_a_day_options()

                        match action:
                            case "1":
                                self.schedule_ui.who_was_working(date)
                            case "2":
                                self.schedule_ui.get_who_was_not_working(date)

                    case "2":
                        action = self.schedule_ui.schedule_for_employee_options()
                        
                        match action:
                            case "1":
                                employee = self.schedule_ui.get_employee()
                                self.schedule_ui.get_schedule_for_employee(employee)
                            case "2":
                                self.schedule_ui.get_total_hours_worked()

            def voyages() -> None:
                """TODO: add docstring"""
                action = self.voyages_ui.voyages_options()

                match action:
                    case "1":
                        self.voyages_ui.add_voyage()

                    case "2":
                        action = self.voyages_ui.voyage_past_or_present_options()

                        match action:
                            case "1":
                                action = self.voyages_ui.list_voyage_options()
                                match action:
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

                            case "2":
                                action = self.voyages_ui.list_voyage_options()
                                match action:
                                    case "1":
                                        date = self.voyages_ui.get_date()
                                        self.voyages_ui.get_past_voyage_by_date(date)
                                    case "2":
                                        year, week = self.voyages_ui.get_week()
                                        self.voyages_ui.get_past_voyage_by_week(
                                            year, week
                                        )

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

            def flight_information() -> None:
                """TODO: add docstring"""
                action = self.flight_info.flight_info_options()
                match action:
                    case "1":
                        voyage = self.flight_info.get_voyage()
                        self.flight_info.get_flight_status_by_voyage(voyage)

                    case "2":
                        date = self.flight_info.get_date()
                        self.flight_info.get_flight_status_by_date(date)

            options = {
                "1": airplane,
                "2": destinations,
                "3": employees,
                "4": schedule,
                "5": voyages,
                "6": flight_information,
            }
            options[action]()
