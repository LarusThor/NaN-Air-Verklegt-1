from ui.main_menuUI import display_options
 
AIRPLANE_OPTIONS = ["1. Airplane types and license", "2. Add new airplane", "3. Airplane usage"]
AIRPLANE_TYPES_AND_LICENSE_OPTIONS = ["1. Pilots by license", "2. List all airplane types"]
PILOTS_BY_LICENSE_OPTIONS = ["1. Licensed pilots for a specific airplane type", "2. All pilots listed by license", "3. Number of licensed pilots for each airplane type"]
AIRPLANE_USAGE = ["1. Get most used airplane", "2. Get airplane which flown furthest"]

def airplane():
    def airplane_usage(): #if nr 3 is chosen from AIRPLANE_OPTIONS
        display_options(AIRPLANE_USAGE)
        action = str(input("Enter your action: ").lower())
        if action == "m":
            None
        elif action == "1":
            pass #get_most_used_airplane
        elif action == "2":
            pass #get_most_flown_airplane

    def add_airplane(): #if nr 2 from AIRPLANE_OPTIONS is chosen
        name = input("Enter airplane name: ")
        type = input("Enter airplane type: ")
        manufacturer = input("Enter airplane manufacturer: ")
        number_of_seats = input("Enter the number of seats in the airplane: ")
        print("New airplane: ")
        print("Name:", name)
        print("Type:", type)
        print("Manufacturer:", manufacturer)
        print("Number of seats:", number_of_seats)
        save_prompt = input("Would you like to save this new airplane, (y)es or (n)o? ").lower()
        if save_prompt == "y":
            print("Airplane saved!")
        elif save_prompt == "n":
            print("New airplane was not saved.")


    def pilots_by_licanse(): # if nr 1 from AIRPLANE_TYPES_AND_LICENSE_OPTIONS is chosen
            display_options(PILOTS_BY_LICENSE_OPTIONS)
            action = str(input("Enter your action: ").lower())

            if action == "m":
                None

            elif action == "1":
                airplane_type = input("Enter the airplane type: ")
                pass # get_pilots_by_type

            elif action == "2":
                pass #get_all_pilots_by_license

            elif action == "3":
                pass #get_number_of_pilots_for_a_type


    def airplane_types_and_licanse(): #if nr 1 from AIRPLANE_OPTIONS is chosen
        display_options(AIRPLANE_TYPES_AND_LICENSE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        
        if action == "m":
            None

        elif action == "1":
            pilots_by_licanse()

        elif action == "2":
            pass #get_list_of_all_aiplane_types
        
    
    #main
    display_options(AIRPLANE_OPTIONS)
    action = str(input("Enter your action: ").lower())

    if action == "m":
        None
    
    elif action == "1":
        airplane_types_and_licanse()
        
    elif action == "2":
        add_airplane()
        
    elif action == "3":
        airplane_usage()