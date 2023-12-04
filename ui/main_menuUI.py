LINE = "*"*30

class MainMenu_UI:
    def __init__(self) -> None:
        pass

    def menu(self):
        print("{}\n1. Airplane\n2. Destinations\n3. Employees\n4. Schedule\n5. VoyagesFlight information\n{}".format(LINE, LINE))

    def input_prompt(self):
        while True:
            self.menu()
            command = input("Enter your command: ")
            command = command.lower()



m = MainMenu_UI()
m.input_prompt()