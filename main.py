from ui.mainUI import Main

test = Main()

<<<<<<< HEAD
test.input_prompt()
=======
#the menu
MAIN_MENU_OPTIONS = ["1. Airplane", "2. Destinations", "3. Employees", "4. Schedule", "5. Voyages", "6. Flight information"]

    
def input_prompt():
    options = {
        "1": airplane,
        "2": destinations,
        "3": employees,
        "4": schedule,
        "5": voyages,
        "6": flight_information
    }

    while True:
        main_menu()           
        action = str(input("Enter your action: ").lower())
        options[action]()

def main():
    input_prompt()

if __name__ == "__main__":
    main()
>>>>>>> 9968da1c59c0ac572f83d0cad99b3a18d800002b
