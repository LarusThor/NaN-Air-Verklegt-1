from ui.main_menuUI import display_options
from ui.airplaneUI import airplane
from ui.destinationsUI import destinations
from ui.employeesUI import employees
from ui.scheduleUI import schedule
from ui.voyagesUI import voyages
from ui.flight_infoUI import flight_information

import os

#the menu
MAIN_MENU_OPTIONS = ["1. Airplane", "2. Destinations", "3. Employees", "4. Schedule", "5. Voyages", "6. Flight information"]

    
def input_prompt():
    while True:
        display_options(MAIN_MENU_OPTIONS)            
        action = str(input("Enter your action: ").lower())
        
        if action == "1":
            airplane()
                
        elif action == "2":
            destinations()

        elif action == "3":
            employees()
            
        elif action == "4":
            schedule()

        elif action == "5":
            voyages()
            
        elif action == "6":
            flight_information()

def main():
    input_prompt()

if __name__ == "__main__":
    main()
