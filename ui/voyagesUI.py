from main_menuUI import display_options

VOYAGES_OPTIONS = ["1. Create a voyage", "2. List of voyages", "3. Staff a voyage", "4. cancel a voyage"]
LIST_VOYAGES_OPTIONS = ["1. List of voyages by day", "2. List of voyages by week"]


def voyages():
    display_options(VOYAGES_OPTIONS)
    action = str(input("Enter your action: ").lower())
    
    if action == "m":
        None

    elif action == "1":
        print("New voyage: ")
        destination = input("Destination: ")
        airplane_type = input("Airplane type: ")
        departure_date = input("Enter departure date; day/month/year: ")
        departure_time = input("Enter departure time: ")
        return_flight_date = input("Enter return flight date; day/month/year: ")
        return_flight_time = input("Enter return flight time: ")
        print("New voyage:")
        print("Destination:", destination)
        print("Airplane type:", airplane_type)
        print("Departure date:", departure_date)
        print("Departure time:", departure_time)
        print("Return flight date:", return_flight_date)
        print("Return flight time:", return_flight_time)
        save_prompt = "Would you like to save this new voyage, (y)es or (n)o? "
        if save_prompt == "y":
            print("New voyage has been saved!")
        elif save_prompt == "n":
            print("New voyage was not saved.")

    elif action == "2":
        display_options(LIST_VOYAGES_OPTIONS)
        action = str(input("Enter your action: ").lower())
        if action == "m":
            None
        elif action == "1":
            date = input("Enter date; day/month/year: ")
            #print voyages by date
        elif action == "2":
            week = input("Enter week number (1-52): ")
            #print voyage by week
        
    elif action == "3":
        flight_number = input("Enter a flight number: ")
        captain = input("Enter captain's social ID: ")
        pilot = input("Enter pilot's social ID: ")
        head_flight_crew = input("Enter head flight attendant's social ID: ")
        #TODO add an option for more flight attendants

    elif action == "4":
        flight_number = input("Enter flight number: ")
        save_prompt = input(f"Would you like to cancel voyage {flight_number}? (y)es or (n)o")
        #TODO show th ifo for the voyage
        if save_prompt == "y":
            print("Voyage has been canceled!")
        elif save_prompt == "n":
            print("Voyage was not canceled.")