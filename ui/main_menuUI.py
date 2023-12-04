import os

LINE = "*"*30
OPTIONS = ["1. Airplane", "2. Destinations", "3. Employees", "4. Schedule", "5. Voyages", "6. Flight information"]

class MainMenu_UI:
    def __init__(self) -> None:
        pass

    def menu(self):
    # Get terminal size
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns
        terminal_height = terminal_size.lines

        # Calculate the number of empty lines above and below the menu
        empty_lines_above = (terminal_height - 6) // 2
        empty_lines_below = terminal_height - 6 - empty_lines_above - 2

        # Print empty lines above the menu
        print("\n" * empty_lines_above)

        padding = (terminal_width) // 3
        print(" " * padding + LINE)
        # Print menu items centered in the terminal
        for item in OPTIONS:
            print(" " * padding + item)
        print(" " * padding + LINE)

        # Print empty lines below the menu
        print("\n" * empty_lines_below)

    def input_prompt(self):
        while True:
            self.menu()
            action = input("Enter your action: ").lower()



