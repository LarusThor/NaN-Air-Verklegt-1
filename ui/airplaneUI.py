from ui.main_menuUI import display_options
from logic.LogicWrapper import LogicWrapper
 
AIRPLANE_OPTIONS = ["1. Airplane types and license", "2. Add new airplane", "3. Airplane usage"]
AIRPLANE_TYPES_AND_LICENSE_OPTIONS = ["1. Pilots by license", "2. List all airplane types"]
PILOTS_BY_LICENSE_OPTIONS = ["1. Licensed pilots for a specific airplane type", "2. All pilots listed by license", "3. Number of licensed pilots for each airplane type"]
AIRPLANE_USAGE = ["1. Get most used airplane", "2. Get airplane which flown furthest"]

logic_wrapper = LogicWrapper()
airplane_types = logic_wrapper.airplane_types()


def airplane():
    def printing_a_list(the_list):
        for item in the_list:
            print(item)
        print()
        print("(M)enu  (R)epeat")
        action = str(input("Enter your action: ").lower())
        if action == "m":
            None
        elif action == "r":
            airplane_types_and_licanse()   

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

            elif action == "1": # get_pilots_by_type
                airplane_type = input("Enter the airplane type: ")
                pass 

            elif action == "2": #get_all_pilots_by_license
                pass 

            elif action == "3": #get_number_of_pilots_for_a_type
                pass 


    def airplane_types_and_licanse(): #if nr 1 from AIRPLANE_OPTIONS is chosen
        display_options(AIRPLANE_TYPES_AND_LICENSE_OPTIONS)
        action = str(input("Enter your action: ").lower())
        
        if action == "m":
            None

        elif action == "1": #pilots by license
            pilots_by_licanse()

        elif action == "2": #list all airplane types
            print()
            print("Airplane types:")
            print("-" * 15)
            printing_a_list(airplane_types)
            print()
        
    
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