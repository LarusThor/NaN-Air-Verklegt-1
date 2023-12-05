from ui.main_menuUI import display_options
from logic.LogicWrapper import LogicWrapper

DESTINATIONS_OPTIONS = ["1. List of destinations", "2. Most popular destination", "3. Add new destination", "4. Destination information"]

logic_wrapper = LogicWrapper()
destinations_list = logic_wrapper.destination_list()

def destinations():
    display_options(DESTINATIONS_OPTIONS)
    action = str(input("Enter your action: ").lower())

    if action == "m":
        None
    
    elif action == "1":
        print(destinations_list)

    elif action == "2":
        pass #get_most_popular_destination

    elif action == "3":
        #add_destination
        print("New destination")
        country = input("Enter the country: ")
        airport = input("Enter the airport: ")
        id = input("Enter the ID: ")
        numeric_id = input("Enter the numeric ID: ")
        distance_from_iceland = input("Enter the distance form Iceland: ")
        contact_name = input("Enter the name of the contact person:")
        contact_number = input("Enter the number of the contact number: ")
        print("New destination:")
        print("Country:", country)
        print("Airport:", airport)
        print("ID:", id)
        print("Numeric ID:", numeric_id)
        print("Distance from Iceland:", distance_from_iceland)
        print("Contact name: ", contact_name)
        print("Contact number: ", contact_number)
        save_prompt = input("Would you like to save this new destionation, (y)es or (n)o? ").lower()
        if save_prompt == "y":
            print("Destination saved!")
        elif save_prompt == "n":
            print("Destionation not saved.")

    elif action == "4":
        #info about a destionation
        print("What destination would you like to get the information about?")
        #print a list of destinations