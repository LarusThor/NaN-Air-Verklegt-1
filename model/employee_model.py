class Employee:
    def __init__(self, name = "", socialID = "", email = "", phonenumber = 5812345, homephone = None):
        self.name = name
        self.socialID = socialID
        self.email = email
        self.phonenumber = phonenumber
        self.homephone = homephone

    def __str__(self) -> str:
        