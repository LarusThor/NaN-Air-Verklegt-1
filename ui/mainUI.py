from main_menuUI import display_options
from airplaneUI import airplane

# from airplaneUI import AirplaneUI
# from destinationsUI import DestinationsUI
# from employeesUI import EmployeesUI
# from scheduleUI import ScheduleUI
# from voyagesUI import VoyagesUI
# from flight_infoUI import FlightInfoUI

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

# def __init__(self) -> None:
#     self.airplane = AirplaneUI()
#     self.destinations = DestinationsUI()
#     self.employees = EmployeesUI()
#     self.schedule = ScheduleUI()
#     self.voyages = VoyagesUI()
#     self.flight_info = FlightInfoUI()

# def display_options(list_of_options):
# # Get terminal size
#     terminal_size = os.get_terminal_size()
#     terminal_width = terminal_size.columns
#     terminal_height = terminal_size.lines

#     # Calculate the number of empty lines above and below the menu
#     empty_lines_above = (terminal_height - 6) // 2
#     empty_lines_below = terminal_height - 6 - empty_lines_above - 2

#     # Print empty lines above the menu
#     print("\n" * empty_lines_above)

#     padding = (terminal_width) // 3
#     print(" " * padding + OUTLINE)
#     # Print menu items centered in the terminal
#     for item in list_of_options:
#         print(" " * padding + item)
#     print(" " * padding + OUTLINE)
#     print("(M)enu")

#     # Print empty lines below the menu
#     print("\n" * empty_lines_below)


# def airplane():
#     display_options(AIRPLANE_OPTIONS)
#     action = str(input("Enter your action: ").lower())

#     if action == "m":
#         input_prompt()
    
#     elif action == "1":
#         #Airplane types and license
#         display_options(["1. Pilots by license", "2. List all airplane types"])
#         action = str(input("Enter your action: ").lower())
#         if action == "m":
#             input_prompt()
#         elif action == "1":
#             display_options(["1. Licensed pilots for a specific airplane type", "2. All pilots listed by license", "3. Number of licensed pilots for each airplane type"])
#             action = str(input("Enter your action: ").lower())
#             if action == "m":
#                 input_prompt()
#             elif action == "1":
#                 airplane_type = input("Enter the airplane type: ")
#                 pass # get_pilots_by_type
#             elif action == "2":
#                 pass #get_all_pilots_by_license
#             elif action == "3":
#                 pass #get_number_of_pilots_for_a_type
#         elif action == "2":
#             pass #get_list_of_all_aiplane_types
        

#     elif action == "2":
#         # add_airplane()
#         name = input("Enter airplane name: ")
#         type = input("Enter airplane type: ")
#         manufacturer = input("Enter airplane manufacturer: ")
#         number_of_seats = input("Enter the number of seats in the airplane: ")
#         print("New airplane: ")
#         print("Name:", name)
#         print("Type:", type)
#         print("Manufacturer:", manufacturer)
#         print("Number of seats:", number_of_seats)
#         save_prompt = input("Would you like to save this new airplane, (y)es or (n)o? ").lower()
#         if save_prompt == "y":
#             print("Airplane saved!")
#         elif save_prompt == "n":
#             print("New airplane was not saved.")

        
#     elif action == "3":
#         # airplane_usage()
#         display_options(["1. Get most used airplane", "2. Get airplane which flown furthest"])
#         action = str(input("Enter your action: ").lower())
#         if action == "m":
#             input_prompt()
#         elif action == "1":
#             pass #get_mosed_used_airplane
#         elif action == "2":
#             pass #get_most_flown_airplane

# def destinations():
#     display_options(DESTINATIONS_OPTIONS)
#     action = str(input("Enter your action: ").lower())

#     if action == "m":
#         input_prompt()
    
#     elif action == "1":
#         pass #get_list_of_destinations

#     elif action == "2":
#         pass #get_most_popular_destination

#     elif action == "3":
#         #add_destination
#         print("New destination")
#         country = input("Enter the country: ")
#         airport = input("Enter the airport: ")
#         id = input("Enter the ID: ")
#         numeric_id = input("Enter the numeric ID: ")
#         distance_from_iceland = input("Enter the distance form Iceland: ")
#         contact_name = input("Enter the name of the contact person:")
#         contact_number = input("Enter the number of the contact number: ")
#         print("New destination:")
#         print("Country:", country)
#         print("Airport:", airport)
#         print("ID:", id)
#         print("Numeric ID:", numeric_id)
#         print("Distance from Iceland:", distance_from_iceland)
#         print("Contact name: ", contact_name)
#         print("Contact number: ", contact_number)
#         save_prompt = input("Would you like to save this new destionation, (y)es or (n)o? ").lower()
#         if save_prompt == "y":
#             print("Destination saved!")
#         elif save_prompt == "n":
#             print("Destionation not saved.")

#     elif action == "4":
#         #info about a destionation
#         print("What destination would you like to get the information about?")
#         #print a list of destinations
        
# def employees():
#     display_options(EMPLOYEES_OPTIONS)
#     action = str(input("Enter your action: ").lower())

#     if action == "m":
#         input_prompt()

#     elif action == "1":
#         display_options(["1. Print pilots", "2. Print flight attendants", "3. Print all employees", "4. Print most experienced"])
#         action = str(input("Enter your action: ").lower())

#         if action == "m":
#             input_prompt()

#         elif action == "1":
#             pass #print out a list of all pilots

#         elif action == "2":
#             pass #print out all the flight attendants

#         elif action == "3":
#             pass #print out all the employees

#         elif action == "4":
#             pass #print the most experienced

#     elif action == "2": #employee information
#         employees_social_id = input("Enter the employees social ID")
#         #print the name of the employee
#         display_options(["1. Print employee information\n2. Change employee information."])
#         action = str(input("Enter your action: ").lower())
#         if action == "m":
#             input_prompt()
#         elif action == "1":
#             pass #print the employees info
#         elif action == "2":
#             display_options("1. Edit home address", "2. Edit phone number", "3. Edit email", "4. Edit home address")
#             action = str(input("Enter your action: ").lower())

#     elif action == "3":
#         print("New employee:")
#         name = input("Name: ")
#         social_id = input("Social ID: ")
#         phone_number = input("Phone number: ")
#         email = input("Email: ")
#         home_adress = input("Home adress: ")
#         work_titles = ["Captain", "Pilot", "Flight Service Manager", "Flight Attendant"]
#         print("Work title:\n1. Captain\n2. Pilot\n3. Flight Service Manager\n4. Flight Attendant")
#         work_title = input()
#         if work_title == "1" or work_title == "2":
#             flight_type = input("Flight type: ")
#         print("New employee:")
#         print("Name:", name)
#         print("Social ID:", social_id)
#         print("Phone number:", phone_number)
#         print("Email:", email)
#         print("Home adress:", home_adress)
#         print("Work title:", work_titles[int(work_title) + 1])
#         save_prompt = "Would you like to save the new employee, (y)es or (n)o? ".lower()
#         if save_prompt == "y":
#             print("New employee saved!")
#         elif save_prompt == "n":
#             print("New employee not saved.")
        
# def schedule():
#     display_options(SCHEDULE_OPTIONS)
#     action = str(input("Enter your action: ").lower())
    
#     if action == "m":
#         input_prompt()
    
#     elif action == "1":
#         print("Choose day")
#         print("Input date as: day/month/year")
#         date = input("Enter date: ")

#         display_options(["1. See who was working", "2. See who was not working"])
#         action = str(input("Enter your action: ").lower())
#         if action == "m":
#             input_prompt()
#         elif action == "1":
#             pass #print how was working
#         elif action == "2":
#             pass #print how was not working

#     elif action == "2":
#         employee = input("Enter the employees social ID: ")
#         #print the employees schedule

# def voyages():
#     display_options(VOYAGES_OPTIONS)
#     action = str(input("Enter your action: ").lower())
    
#     if action == "m":
#         display_options(MAIN_MENU_OPTIONS)
#     elif action == "1":
#         print("New voyage: ")
#         destination = input("Destination: ")
#         airplane_type = input("Airplane type: ")
#         departure_date = input("Enter departure date; day/month/year: ")
#         departure_time = input("Enter departure time: ")
#         return_flight_date = input("Enter return flight date; day/month/year: ")
#         return_flight_time = input("Enter return flight time: ")
#         print("New voyage:")
#         print("Destination:", destination)
#         print("Airplane type:", airplane_type)
#         print("Departure date:", departure_date)
#         print("Departure time:", departure_time)
#         print("Return flight date:", return_flight_date)
#         print("Return flight time:", return_flight_time)
#         save_prompt = "Would you like to save this new voyage, (y)es or (n)o? "
#         if save_prompt == "y":
#             print("New voyage has been saved!")
#         elif save_prompt == "n":
#             print("New voyage was not saved.")


#     elif action == "2":
#         display_options(["1. List of voyages by day", "2. List of voyages by week"])
#         action = str(input("Enter your action: ").lower())
#         if action == "m":
#             input_prompt()
#         elif action == "1":
#             date = input("Enter date; day/month/year: ")
#             #print voyages by date
#         elif action == "2":
#             week = input("Enter week number (1-52): ")
#             #print voyage by week
        
#     elif action == "3":
#         flight_number = input("Enter a flight number: ")
#         captain = input("Enter captain's social ID: ")
#         pilot = input("Enter pilot's social ID: ")
#         head_flight_crew = input("Enter head flight attendant's social ID: ")
#         #TODO add an option for more flight attendants

#     elif action == "4":
#         flight_number = input("Enter flight number: ")
#         save_prompt = input(f"Would you like to cancel voyage {flight_number}? (y)es or (n)o")
#         #TODO show th ifo for the voyage
#         if save_prompt == "y":
#             print("Voyage has been canceled!")
#         elif save_prompt == "n":
#             print("Voyage was not canceled.")

# def flight_information():
#             display_options(FLIGHT_INFORMATION_OPTIONS)
#             action = str(input("Enter your action: ").lower())
            
#             if action == "m":
#                 input_prompt()

#             elif action == "1":
#                 flight_number = input("Enter flight number: ")
#                 #print if the voyage if fully booked or not

#             elif action == "2":
#                 date = input("Enter date; day/month/year: ")  
#                 #print the booking status for the flights on that date              
    
def input_prompt():
    while True:
        display_options(MAIN_MENU_OPTIONS)            
        action = str(input("Enter your action: ").lower())
        
        if action == "1":
            airplane()
                
        # elif action == "2":
        #     destinations()

        # elif action == "3":
        #     employees()
            
        # elif action == "4":
        #     schedule()

        # elif action == "5":
        #     voyages()
            
        # elif action == "6":
        #     flight_information()


test = display_options(MAIN_MENU_OPTIONS)
input_prompt()