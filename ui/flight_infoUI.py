from ui.main_menuUI import display_options

FLIGHT_INFORMATION_OPTIONS = ["1. Booking status for specific voyage", "2. Booking status for a specific date"]

def flight_information():
            display_options(FLIGHT_INFORMATION_OPTIONS)
            action = str(input("Enter your action: ").lower())
            
            if action == "m":
                None

            elif action == "1":
                flight_number = input("Enter flight number: ")
                #print if the voyage if fully booked or not

            elif action == "2":
                date = input("Enter date; day/month/year: ")  
                #print the booking status for the flights on that date