from airplaneUI import AirplaneUI
from destinationsUI import DestinationsUI
from employeesUI import EmployeesUI
from scheduleUI import ScheduleUI
from voyagesUI import VoyagesUI
from flight_infoUI import FlightInfoUI

import os

#the menu
OUTLINE = "*"*50
MAIN_MENU_OPTIONS = ["1. Airplane", "2. Destinations", "3. Employees", "4. Schedule", "5. Voyages", "6. Flight information"]
AIRPLANE_OPTIONS = ["1. Airplane types and license", "2. Add new airplane", "3. Airplane usage"]
DESTINATIONS_OPTIONS = ["1. List of destinations", "2. Most popular destination", "3. Add new destination", "4. Destination information"]
EMPLOYEES_OPTIONS = ["1. List employees - Alphabetical", "2. Employee information", "3. Add employee"]
SCHEDULE_OPTIONS = ["1. Schedule for a specific day", "2. Schedule for specific employee"]
VOYAGES_OPTIONS =["1. Create a voyage", "2. List of voyages", "3. Staff a voyage", "4. cancel a voyage"]
FLIGHT_INFORMATION_OPTIONS = ["1. Booking status for specific voyage", "2. Booking status for a specific date"]

class MainMenu_UI():
    def __init__(self) -> None:
        self.airplane = AirplaneUI()
        self.destinations = DestinationsUI()
        self.employees = EmployeesUI()
        self.schedule = ScheduleUI()
        self.voyages = VoyagesUI()
        self.flight_info = FlightInfoUI()

    def display_options(self, list_of_options):
    # Get terminal size
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns
        terminal_height = terminal_size.lines

        # Calculate the number of empty lines above and below the menu
        empty_lines_above = (terminal_height - 6) // 2
        empty_lines_below = terminal_height - 6 - empty_lines_above - 2

        # Print empty lines above the menu
        print("\n" * empty_lines_above)

        padding = (terminal_width) // 3
        print(" " * padding + OUTLINE)
        # Print menu items centered in the terminal
        for item in list_of_options:
            print(" " * padding + item)
        print(" " * padding + OUTLINE)
        print("(M)enu")

        # Print empty lines below the menu
        print("\n" * empty_lines_below)
       
    def input_prompt(self):
        while True:
            self.display_options(MAIN_MENU_OPTIONS)            
            action = str(input("Enter your action: ").lower())
            
            if action == "1":
                if action == "m":
                    self.display_options(MAIN_MENU_OPTIONS)
                elif action == "1":
                    self.types()
                elif action == "2":
                    self.airplane.add_airplane()
                elif action == "3":
                    self.airplane.add_airplane()
                    
            elif action == "2":
                self.display_options(DESTINATIONS_OPTIONS)
                action = str(input("Enter your action: ").lower())
                
                if action == "m":
                    self.display_options(MAIN_MENU_OPTIONS)
                elif action == "1":
                    self.destinations.get_all_destinations()
                elif action == "2":
                    self.destinations_get_most_popular_destination()
                elif action == "3":
                    self.destinations.add_destination()
                elif action == "4":
                    self.destinations()#

            elif action == "3":
                self.display_options(EMPLOYEES_OPTIONS)
                action = str(input("Enter your action: ").lower())
                
                if action == "m":
                    self.display_options(MAIN_MENU_OPTIONS)
                elif action == "1":
                    self.employees()#
                elif action == "2":
                    self.employees()#
                elif action == "3":
                    self.employees()#

            elif action == "4":
                self.display_options(SCHEDULE_OPTIONS)
                action = str(input("Enter your action: ").lower())
                
                if action == "m":
                    self.display_options(MAIN_MENU_OPTIONS)
                elif action == "1":
                    self.schedule()#
                elif action == "2":
                    self.schedule()#

            elif action == "5":
                self.display_options(VOYAGES_OPTIONS)
                action = str(input("Enter your action: ").lower())
                
                if action == "m":
                    self.display_options(MAIN_MENU_OPTIONS)
                elif action == "1":
                    self.voyages()#
                elif action == "2":
                    self.voyages()#
                elif action == "3":
                    self.voyages()#
                elif action == "4":
                    self.voyages()
                
            elif action == "6":
                self.display_options(FLIGHT_INFORMATION_OPTIONS)
                action = str(input("Enter your action: ").lower())
                
                if action == "m":
                    self.display_options(MAIN_MENU_OPTIONS)
                elif action == "1":
                    self.flight_info()#
                elif action == "2":
                    self.flight_info()#
                elif action == "3":
                    self.flight_info()#
                elif action == "4":
                    self.flight_info()#


test = MainMenu_UI()
test.input_prompt()

