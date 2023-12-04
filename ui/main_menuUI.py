from airplaneUI import AirplaneUI
from destinationsUI import DestinationsUI
from employeesUI import EmployeesUI
from scheduleUI import ScheduleUI
from voyagesUI import VoyagesUI
from flight_infoUI import FlightInfoUI

import os

#the menu
LINE = "*"*30
OPTIONS = ["1. Airplane", "2. Destinations", "3. Employees", "4. Schedule", "5. Voyages", "6. Flight information"]

class MainMenu_UI:
    def __init__(self) -> None:
        self.airplane = AirplaneUI()
        self.destinations = DestinationsUI()
        self.employees = EmployeesUI()
        self.schedule = ScheduleUI()
        self.voyages = VoyagesUI()
        self.flight_info = FlightInfoUI()

    def menu(self, list_of_options):
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
        print(" " * padding + LINE)
        # Print menu items centered in the terminal
        for item in list_of_options:
            print(" " * padding + item)
        print(" " * padding + LINE)

        # Print empty lines below the menu
        print("\n" * empty_lines_below)

    def input_prompt(self, list_of_options):
        while True:
            self.menu(list_of_options)
            action = str(input("Enter your action: ").lower())
            
            if action == "1":
                options = ["1. Airplane types and license", "2. Add new airplane", "3. Airplane usage"]
                self.menu(options)
                action = str(input("Enter your action: ").lower())
                
                if action == "1":
                    self.airplane.types()
                elif action == "2":
                    self.airplane.add_airplane()
                elif action == "3":
                    self.airplane.add_airplane()


            elif action == "2":
                pass

            elif action == "3":
                pass

            elif action == "4":
                pass

            elif action == "5":
                pass

            elif action == "6":
                pass


test = MainMenu_UI()
test.input_prompt(OPTIONS)

