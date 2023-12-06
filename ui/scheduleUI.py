from ui.main_menuUI import display_options

SCHEDULE_OPTIONS = ["1. Schedule for a specific day", "2. Schedule for specific employee"]
SCHEDULE_FOR_A_DAY_OPTIONS = ["1. See who was working", "2. See who was not working"]


def schedule():
    def schedule_for_a_spedific_day(date): #if nr 1 if chosen from SCHEDULE_OPTIONS
        display_options(SCHEDULE_FOR_A_DAY_OPTIONS)
        action = str(input("Enter your action: ").lower())

        if action == "m":
            None

        elif action == "1":
            pass #print how was working

        elif action == "2":
            pass #print how was not working

    #main
    display_options(SCHEDULE_OPTIONS)
    action = str(input("Enter your action: ").lower())
    
    if action == "m":
        None
    
    elif action == "1":
        print("Choose day")
        print("Input date as: day/month/year")
        date = input("Enter date: ")
        schedule_for_a_spedific_day(date)

    elif action == "2":
        employee = input("Enter the employees social ID: ")
        #print the employees schedule