class Employee:
    def __init__(self, name = "", socialID = "", email = "", phonenumber = 5871234, landline = None):
        self.name = name
        self.socialID = socialID
        self.email = email
        self.phonenumber = phonenumber
        self.landline = landline

    def __str__(self) -> str:
        return f'name: {self.name}\nsocialID: {self.socialID}\nemail: {self.email}\nphonenumber: {self.phonenumber}\nlandline: {self.landline}'