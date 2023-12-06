def add_employee():
    print("Fill out the following informaation about the new employee:")
    name = input("Name: ")
    social_id = input("Social ID: ")
    phone_number = input("Phone number: ")
    email = input("Email: ")
    home_address = input("Home adress: ")

    roles = ["Pilot","Cabincrew"]
    print("Role:\n1. Pilot\n2. Cabincrew")
    role = input()
    while role != "1" and role != "2":
        print("Invalid input! You can choose 1, 2")
        role = input("Role: ")
    ranks = ["Captain", "Copilot", "Flight Service Manager", "Flight Attendant"]
    print("Rank:\n1. Captain\n2. Copilot\n3. Flight Service Manager\n4. Flight Attendant")
    rank = input()
    while rank != "1" and rank != "2" and rank != "3" and rank != "4":
        print("Invalid input! You can choose 1, 2, 3, or 4")
        rank = input("Rank: ")
    if rank == "1" or rank == "2":
        licences = ["NAFokker100","NAFokkerF28","NABAE146"]
        print("Licenses:\n1. NAFokker100\n2. NAFokkerF28\n3. NABAE146",)
        licence = input()
    else:
        licence = "N/A"
    optional_landline = input("Do you want to add a landline number? (y)es or (n)o? ").lower()
    if optional_landline == "y":
        landline = input("Landline number: ")
    else:
        landline = None

    print("New employee:")
    print("Name:", name)
    print("Social ID:", social_id)
    print("Phone number:", phone_number)
    print("Email:", email)
    print("Home adress:", home_address)
    print("Role:", roles[int(role) - 1])
    print("Rank:", ranks[int(rank) - 1])
    print("License:", licences[int(licence) - 1])
    print("Landline number:", landline)

    # TODO
    employee = Employee(
        name=name, 
        socialID=social_id, 
        phonenumber=phone_number,
        role=role, 
        rank=rank,
        licence=licence,
        email=email,
        home_address=home_address,
        landline=landline
    )