from logic.validationLL import ValidationLL
import os
OUTLINE = "="*70
MAIN_MENU_OPTIONS = ["1. Airplane", "2. Destinations", "3. Employees", "4. Schedule", "5. Voyages", "6. Flight status"]


TITLE2="_____   __              _____   __              _______       _____           "
TITLE3="___  | / /  ______ _    ___  | / /              ___    |      ___(_)  ________"
TITLE4="__   |/ /   _  __ `/    __   |/ /  ________     __  /| |      __  /   __  ___/"                      
TITLE5="_  /|  /    / /_/ /     _  /|  /   _/_____/     _  ___ |      _  /    _  /    "
TITLE6="/_/ |_/     \__,_/      /_/ |_/                 /_/  |_|      /_/     /_/     "


TITLE9 ="          _____                                                 __________       "                                                  
TITLE10="        __\ _~-\____                                           |          |      "
TITLE11="=  = ==(___NaN-Air__)                                          |          |      "
TITLE12="           \_____\___________________,-~~~~~~~`-.._            |          |      "
TITLE13="          /     o O o o o o O O o o o o o o O o  |\_           |          |      "
TITLE14="          `~-.__        ___..----..                   )        |          |      "
TITLE15="                `---~~\___________/------------`````           |          |      "   
TITLE16="                 =  ===(_________)                             |__________|      "


class Menu():
    def init(self) -> None:
        """ TODO: add docstring """


    def main_menu(self) -> None:
        """ TODO: add docstring """
    # Get terminal size
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns
        terminal_height = terminal_size.lines
      

        # Calculate the number of empty lines above and below the menu
        empty_lines_above = (terminal_height - 30) // 2
        empty_lines_below = terminal_height - 20 - empty_lines_above - 2

        # Print empty lines above the menu


        #calculating the the middle width to place the bottem options at.
        half_text_len = int(len(TITLE2) / 2)
        middle_width = int(terminal_width / 2 - half_text_len)
        print()
        print("="*terminal_width + "\n")
        print(" " * middle_width + TITLE2)
        print(" " * middle_width + TITLE3)
        print(" " * middle_width + TITLE4)
        print(" " * middle_width + TITLE5)
        print(" " * middle_width + TITLE6 + "\n\n")
        print("="*terminal_width)

        print("\n" * empty_lines_above)

        padding = (terminal_width) // 3
        # print(" Main Menu:")
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


        #calculating the the middle width to place the bottem options at.
        half_text_len = int(len(TITLE9) / 2)
        middle_width = int(terminal_width / 2 - half_text_len)

        print()
        print(" " * middle_width + TITLE9)
        print(" " * middle_width + TITLE10)
        print(" " * middle_width + TITLE11)
        print(" " * middle_width + TITLE12)
        print(" " * middle_width + TITLE13)
        print(" " * middle_width + TITLE14)
        print(" " * middle_width + TITLE15)
        print(" " * middle_width + TITLE16)

        # Calculate the number of empty lines above and below the menu
        empty_lines_above = (terminal_height - 24) // 2
        empty_lines_below = terminal_height - len(list_of_options) - 15 - empty_lines_above - 2

        # Print empty lines above the menu
        print("\n" * empty_lines_above)

        padding = (terminal_width) // 3
        print(" " * padding + title)
        print(" " * padding + OUTLINE)
        # Print menu items centered in the terminal
        for item in list_of_options:
            print(" " * padding + item)

        #calculating the the middle width to place the bottem options at.
        back_or_quit = "Enter (b) for back or (q) for quit"
        half_text_len = int(len(back_or_quit) / 2)
        middle_width = int(terminal_width / 2 - half_text_len)


        print(" " * padding + OUTLINE)

        # Print empty lines below the menu
        print("\n" * empty_lines_below)
        print("-"*terminal_width)
        print(" "*middle_width + back_or_quit)
        print("-"*terminal_width)


    def get_next_action(self) -> None: #TODO þetta fall skilar engu, erum við að nota það?
        """ TODO: add docstring """
        print("Enter (b) for back or (q) for quit") # TODO has to validated
        action = input("Enter in your action: ").lower()

        
    
    def print_the_info(self, title, info="") -> None:
        """ TODO: add docstring """
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns
        terminal_height = terminal_size.lines

        # Calculate the number of empty lines above and below the menu
        info_list = info.split("\n")
        empty_lines_above = (terminal_height - len(info_list)) // 2
        empty_lines_below = terminal_height - len(info_list) - empty_lines_above - 4

        # Print empty lines above the menu
        print("\n" * empty_lines_above)

        #padding = (terminal_width) // 150
        print(title)
        print(OUTLINE)
        for item in info_list:
            print(item)
        print("\n" * empty_lines_below)
        self.get_next_action()
