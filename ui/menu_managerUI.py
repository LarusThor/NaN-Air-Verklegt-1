from logic.logic_wrapper import LogicWrapper
import os
OUTLINE = "-"*50
MAIN_MENU_OPTIONS = ["1. Airplane", "2. Destinations", "3. Employees", "4. Schedule", "5. Voyages", "6. Flight information"]

class Menu():
    def init(self) -> None:
        """ TODO: add docstring """
        self.logic_wrapper = LogicWrapper()

    def main_menu(self) -> None:
        """ TODO: add docstring """
    # Get terminal size
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns
        terminal_height = terminal_size.lines

        # Calculate the number of empty lines above and below the menu
        empty_lines_above = (terminal_height - 6) // 2
        empty_lines_below = terminal_height - 6 - empty_lines_above - 2

        # Print empty lines above the menu
        print("\n" * empty_lines_above)

        padding = (terminal_width) // 150
        print(" Main Menu:")
        print(" " * padding + OUTLINE)
        # Print menu items centered in the terminal
        for item in MAIN_MENU_OPTIONS:
            print(" " * padding + item)
        print(" " * padding + OUTLINE)

        # Print empty lines below the menu
        print("\n" * empty_lines_below)

    def display_options(self, title: str, list_of_options: list[str]) -> None:
        """ Display menu options

        TODO: Do not require prepended numbers for the options - automatically insert them

        Args:
            list_of_options: Option strings, with numbers prepended
        
        """
         # Get terminal size
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns
        terminal_height = terminal_size.lines

        # Calculate the number of empty lines above and below the menu
        empty_lines_above = (terminal_height - 6) // 2
        empty_lines_below = terminal_height - 6 - empty_lines_above - 2

        # Print empty lines above the menu
        print("\n" * empty_lines_above)

        padding = (terminal_width) // 150
        print(" " * padding + OUTLINE)
        # Print menu items centered in the terminal

        for item in list_of_options:
            print(" " * padding + item)

        # for i, item in enumerate(list_of_options):
        #     print(" " * padding + f"{i + 1}" +  item) 

        print(" " * padding + OUTLINE)
        print("Enter (h) for Home or (q) for quit")

        # Print empty lines below the menu
        print("\n" * empty_lines_below)

    def get_next_action(self):
        """ TODO: add docstring """
        print("Enter (h) for Home or (q) for quit") # TODO has to validated
        action = input("Enter in your action: ").lower()
        match action:
            case "h":
                None
            case "q":
                quit()

    
    def print_the_info(self, title, info):
        """ TODO: add docstring """
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns
        terminal_height = terminal_size.lines

        # Calculate the number of empty lines above and below the menu
        empty_lines_above = (terminal_height - 6) // 2
        empty_lines_below = terminal_height - 6 - empty_lines_above - 2

        # Print empty lines above the menu
        print("\n" * empty_lines_above)

        padding = (terminal_width) // 150
        # print(" Main Menu:")
        print(" " * padding)
        # Print menu items centered in the terminal
        # for item in info:
        print(title)
        print(OUTLINE)
        print(info)
        print()
        self.get_next_action()