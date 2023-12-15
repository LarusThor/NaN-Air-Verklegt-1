from logic.logic_wrapper import LogicWrapper
import os

OUTLINE = "="*70
MAIN_MENU_OPTIONS = ["1. Airplane", "2. Destinations", "3. Employees", "4. Schedule", "5. Voyages", "6. Flight status"]

TITLE2="_____   __              _____   __              _______       _____           "
TITLE3="___  | / /  ______ _    ___  | / /              ___    |      ___(_)  ________"
TITLE4="__   |/ /   _  __ `/    __   |/ /  ________     __  /| |      __  /   __  ___/"                      
TITLE5="_  /|  /    / /_/ /     _  /|  /   _/_____/     _  ___ |      _  /    _  /    "
TITLE6="/_/ |_/     \__,_/      /_/ |_/                 /_/  |_|      /_/     /_/     "

TITLE7 ="          _____                                         "                                                  
TITLE8="        __\ _~-\____                                    "
TITLE9="=  = ==(___NaN-Air__)                                   "
TITLE10="           \_____\___________________,-~~~~~~~`-.._     "
TITLE11="          /     o O o o o o O O o o o o o o O o  |\_    "
TITLE12="          `~-.__        ___..----..                   ) "
TITLE13="                `---~~\___________/------------`````    "   
TITLE14="                 =  ===(_________)                      "


class Menu():
    """"Class that takes care of printing everyting out; menus and outputs."""
    
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.validation = self.logic_wrapper.validation


    def main_menu(self) -> None:
        """Takes care of printing out the home page. It calculates the terminal size so the ascii art and main menu will always be in the middle"""
        # Get the terminal size
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns
        terminal_height = terminal_size.lines
      
        # Calculate the number of empty lines above and below the menu, subtracted with the space for the ascii art
        empty_lines_above = (terminal_height - 30) // 2
        empty_lines_below = terminal_height - 20 - empty_lines_above - 2

        # Calculating the middle width to then place the ascii art in the middle.
        half_ascii_art_len = int(len(TITLE2) / 2) # Getting half of the ascii art width
        middle_width = int(terminal_width / 2 - half_ascii_art_len) # Calculating where to place the ascii art so it will be in the middle

        # printing the ascii art title at the top-middle
        print("\n" + "=" * terminal_width + "\n")
        print(" " * middle_width + TITLE2)
        print(" " * middle_width + TITLE3)
        print(" " * middle_width + TITLE4)
        print(" " * middle_width + TITLE5)
        print(" " * middle_width + TITLE6 + "\n\n")
        print("="*terminal_width)

        # Print empty lines above the menu
        print("\n" * empty_lines_above)

        padding = (terminal_width) // 3 # Calculating the empty lines that will be printed before the menu so it will be in the middle

        print(" " * padding + OUTLINE)

        # Print menu items centered in the terminal
        for item in MAIN_MENU_OPTIONS:
            print(" " * padding + item)

        print(" " * padding + OUTLINE)

        # Print empty lines below the menu
        print("\n" * empty_lines_below)



    def display_options(self, title: str, list_of_options: list[str]) -> None:
        """Takes in a title and a list of options. Calculates the terminal size so the ascci art, option menu and the back og quit options
        can be placed in the right place. Prints out the ascci art, the given title, an outline, the given options and the back or quit options."""

        # Getting the terminal size
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns
        terminal_height = terminal_size.lines


        # Calculating the the middle width to place the bottem options at.
        half_text_len = int(len(TITLE9) / 2) # Getting half of the option manu width
        middle_width = int(terminal_width / 2 - half_text_len) # Calculating where to place the optins so they will be in the middle

        # Printing the ascci art at the top of the terminal
        print("\n" + " " * middle_width + TITLE7)
        print(" " * middle_width + TITLE8)
        print(" " * middle_width + TITLE9)
        print(" " * middle_width + TITLE10)
        print(" " * middle_width + TITLE11)
        print(" " * middle_width + TITLE12)
        print(" " * middle_width + TITLE13)
        print(" " * middle_width + TITLE14)

        # Calculate the number of empty lines above and below the menu
        empty_lines_above = (terminal_height - 24) // 2
        empty_lines_below = terminal_height - len(list_of_options) - 15 - empty_lines_above - 2

        # Print empty lines above the menu
        print("\n" * empty_lines_above)

        padding = (terminal_width) // 3 # Calculating the empty lines that will be printed before the menu so it will be in the middle

        print(" " * padding + title) # printing the title in the right place
        print(" " * padding + OUTLINE) # printing a line below the title

        # Print menu items centered in the terminal
        for item in list_of_options:
            print(" " * padding + item)

        # Calculating the middle width to place the bottem options at.
        back_or_quit = "Enter (b) for back or (q) for quit"
        half_text_len = int(len(back_or_quit) / 2)
        middle_width = int(terminal_width / 2 - half_text_len)


        print(" " * padding + OUTLINE)

        # Print empty lines below the menu
        print("\n" * empty_lines_below)
        
        # printing the back and quit options at the bottom-middle of the terminal
        print("-" * terminal_width)
        print(" " * middle_width + back_or_quit)
        print("-" * terminal_width)


    def get_next_action(self) -> str:
        """Takes care of telling the user what they can do and asks for an input. Validates the input to check if it is anything other than "q" or "b". 
        Returns the users input"""

        print("Enter (b) for back or (q) for quit")
        
        action = input("Enter in your action: ").lower()

        while self.validation.validate_back_or_quit(action) == False:
            print("\nERROR: Invalid input. You can choose b or q")
            action = input("Enter in your action: ")

        return action
        
    
    def print_the_info(self, title: str, info:str ="") -> str:
        """Takes in a title and the information that needs to be printed out. Calculates the size of the terminal and prints the title 
        and the information in the middle-lines of the terminal. Calls a function in the Menu class that takes in an input from the user and returns that input."""
        
        # Getting the terminal size
        terminal_size = os.get_terminal_size()
        terminal_height = terminal_size.lines

        # Calculate the number of empty lines above and below the information
        info_list = info.split("\n")
        empty_lines_above = (terminal_height - len(info_list)) // 2
        empty_lines_below = terminal_height - len(info_list) - empty_lines_above - 4

        # Print empty lines above the menu
        print("\n" * empty_lines_above)

        # Printing everything out in the middle-lines of the terminal
        print(title)
        print(OUTLINE)

        for item in info_list:
            print(item)
        print("\n" * empty_lines_below)

        # Getting the bottom menu, that is the back og quit options
        action = self.get_next_action()

        return action
