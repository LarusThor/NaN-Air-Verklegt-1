import os
OUTLINE = "*"*50
MAIN_MENU_OPTIONS = ["1. Airplane", "2. Destinations", "3. Employees", "4. Schedule", "5. Voyages", "6. Flight information"]

def display_options(list_of_options):
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
    print(" " * padding + OUTLINE)
    # Print menu items centered in the terminal
    for item in list_of_options:
        print(" " * padding + item)
    print(" " * padding + OUTLINE)
    print("(M)enu")

    # Print empty lines below the menu
    print("\n" * empty_lines_below)

def ascii_art():
      return""" 
                _____
              __\ _~-\____
      =  = ==(___NaN-Air__)
                  \_____\___________________,-~~~~~~~`-.._
                  /     o O o o o o O O o o o o o o O o  |\_
                  `~-.__        ___..----..                  )
                        `---~~\___________/------------`````
                        =  ===(_________)
      """

def main():
     display_options(MAIN_MENU_OPTIONS)

main()