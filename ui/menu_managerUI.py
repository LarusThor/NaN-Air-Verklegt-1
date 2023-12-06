from logic.LogicWrapper import LogicWrapper
import os
OUTLINE = "-"*50
MAIN_MENU_OPTIONS = ["1. Airplane", "2. Destinations", "3. Employees", "4. Schedule", "5. Voyages", "6. Flight information"]

class Menu():
    def init(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def main_menu(self) -> None:
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

    def display_options(self, list_of_options) -> None:
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
        print(" " * padding + OUTLINE)
        print("(M)enu  (B)ack")

        # Print empty lines below the menu
        print("\n" * empty_lines_below)

