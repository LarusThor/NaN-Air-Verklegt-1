from logic.LogicWrapper import LogicWrapper
from ui.menu_managerUI import Menu
from ui.airplaneUI import AirplaneUI
from ui.destinationsUI import DestinationsUI
from ui.employeesUI import EmployeeUI
from ui.scheduleUI import ScheduleUI
from ui.voyagesUI import VoyagesUI
from ui.flight_infoUI import FlightInfoUI

#the menu
MAIN_MENU_OPTIONS = ["1. Airplane", "2. Destinations", "3. Employees", "4. Schedule", "5. Voyages", "6. Flight information"]

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



    def input_prompt(self) -> None:
        while True:
            self.menus.main_menu()          
            action = str(input("Enter your action: ").lower())
            
            def airplane() -> None:
                action = self.airplane_ui.airplane()
                
                if action == "m" or action == "b":
                    None
                
                elif action == "1": # airplane types and license
                    action = self.airplane_ui.airplane_types_and_licanse()
                    if action == "1":
                        action = self.airplane_ui.pilots_by_licanse()
                        #vantar meira
                    elif action == "2":
                        self.airplane_ui.types()
                
                elif action == "2": # add new airplane
                    self.airplane_ui.add_airplane()
                
                elif action == "3": # airplane usage
                    action = self.airplane_ui.airplane_usage_options()
                    if action == "1":
                        self.airplane_ui.most_used_airplane()
                    elif action ==  "2":
                        self.airplane_ui.flown_furthest_airplane()

            
            def destinations() -> None:
                action = self.destinations_ui.destinations()
                if action == "1":
                    action = self.destinations_ui.get_all_destinations()

                elif action == "2":
                    self.destinations_ui.get_most_popular_destination()

                elif action == "3":
                    self.destinations_ui.add_destination()

                elif action == "4":
                    self.destinations_ui.get_destination_info()

            def employees() -> None:
                action = self.employee_ui.employees_options()
                
                if action == "m" or action == "b":
                    None

                # list employees :
                elif action == "1":
                    action = self.employee_ui.list_employees_options()
                    if action == "m":
                        None
                    # elif action == "b":
                    #     employees()
                    elif action == "1": 
                        self.employee_ui.get_pilots()
                        # EmployeesUI.print_crew(self.pilots_list)

                    elif action == "2": 
                        self.employee_ui.get_flight_attendants()
                    elif action == "3": 
                        self.employee_ui.get_all_employees()
                    elif action == "4": 
                        self.employee_ui.get_most_experienced()

                # Employee info :
                elif action == "2":
                    employee_name = self.employee_ui.get_employee()
                    action = self.employee_ui.employee_info_options()
                    
                    if action == "m":
                        None

                    elif action == "1":
                        self.employee_ui.get_info(employee_name)

                    elif action == "2":
                        action = self.employee_ui.change_info_options()
                        if action == "1":
                            self.employee_ui.change_home_address()
                        elif action == "2":
                            self.employee_ui.change_phone_number()
                        elif action == "3":
                            self.employee_ui.change_email()
                        
                    # Add employee :
                    elif action == "3":
                        self.employee_ui.add_employee()

            def schedule() -> None:
                action = self.schedule_ui.schedule_options()
                
                if action == "1":
                    date = self.schedule_ui.get_schedule_by_day()
                    action = self.schedule_ui.schedule_for_a_day_options()
                    if action == "1":
                        self.schedule_ui.get_how_was_working(date)
                    elif action == "2":
                        self.schedule_ui.get_how_was_not_working(date)

                elif action == "2":
                    employee = self.schedule_ui.get_employee()
                    self.schedule_ui.get_schedule_for_employee(employee)


            def voyages() -> None:
                action = self.voyages_ui.voyages_options()
                
                if action == "1":
                    self.voyages_ui.add_voyage()

                elif action == "2":
                    action = self.voyages_ui.list_voyage_options()
                    if action == "1":
                        date = self.voyages_ui.get_date()
                        self.voyages_ui.get_voyage_by_date(date)
                    elif action == "2":
                        week = self.voyages_ui.get_week()
                        self.voyages_ui.get_voyage_by_week(week)

                elif action == "3":
                    self.voyages_ui.staff_voyage()
                
                elif action == "4":
                    self.voyages_ui.staff_voyage()
            
            def flight_information() -> None:
                action = self.flight_info.flight_info_options()
                
                if action == "1":
                    voyage = self.flight_info.get_voyage()
                    self.flight_info.get_flight_status_by_voyage(voyage)

                elif action == "2":
                    date = self.flight_info.get_date()
                    self.flight_info.get_flight_status_by_date(date)

           
            options = {
                "1": airplane,
                "2": destinations,
                "3": employees,
                "4": schedule,
                "5": voyages,
                "6": flight_information
            }
            
            options[action]()