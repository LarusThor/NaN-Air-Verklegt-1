from main_menuUI import display_options

SCHEDULE_OPTIONS = ["1. Schedule for a specific day", "2. Schedule for specific employee"]


def schedule():
    display_options(SCHEDULE_OPTIONS)
    action = str(input("Enter your action: ").lower())
    
    if action == "m":
        None
    
    elif action == "1":
        print("Choose day")
        print("Input date as: day/month/year")
        date = input("Enter date: ")

        display_options(["1. See who was working", "2. See who was not working"])
        action = str(input("Enter your action: ").lower())
        if action == "m":
            None
        elif action == "1":
            pass #print how was working
        elif action == "2":
            pass #print how was not working

    elif action == "2":
        employee = input("Enter the employees social ID: ")
        #print the employees schedule