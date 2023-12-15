from datetime import datetime


class ValidationLL:
    def __init__(self) -> None:
        """Instantiate a ValidationLL object."""

    def validate_choice(self, action: str, option: int) -> bool:
        """Validates numerical action input."""
        try:
            action = int(action)
            if action > 0 and action <= option:
                return True
            else:
                return False
        except ValueError:
            return False

    # employee
    def validate_name(self, name: str) -> bool:
        """Validates name input."""
        name_values = name.split()
        return len(name) >= 3 and all((char.isalpha() for char in name_values))

    def validate_social_ID(self, socialID: str) -> bool:
        """Validates social ID input."""
        return len(socialID) == 10 and all((digit.isdigit() for digit in socialID))

    def validate_number(self, number: str) -> bool:
        """Validates a phone number."""
        return len(number) == 7 and all(digit.isdigit()for digit in number) and int(number) > 1
        

    def validate_email(self, email: str) -> bool:
        """Validates emails"""
        return "@" in email and "." in email

    def validate_address(self, address: str) -> bool:
        """Validates address"""
        address_values = address.split()
        if len(address_values) == 2:
            if address_values[1].isdigit() == True:
                return (
                    len(address) >= 3
                    and all((char.isalpha() for char in address[0]))
                    and (digit.isdigit() for digit in address[1])
                )
        if len(address_values) == 1:
            return len(address) >= 3 and all((char.isalpha() for char in address[0]))

    def validate_yes_no(self, input: str) -> bool:
        """Validates yes and no options"""
        if input == "y" or input == "n":
            return True
        else:
            return False

    # airplanes
    def validate_aircraft_by_specific_type(self, aircraft_specific_type) -> bool:
        return "N/A" in aircraft_specific_type

    def validate_airplane_name(self, aircraft_name) -> bool:
        if aircraft_name[0:2] == "TF" and len(aircraft_name[3:]) == 3:
            if aircraft_name[2] == "-":
                if type(aircraft_name[3:6]) == str:
                    return True
        else:
            return False

    def validate_airplane_choice(self, airplane_choice: int) -> bool:
        """Validates airplane choices."""
        try:
            airplane_choice = int(airplane_choice)
            return True
        except ValueError:
            return False

    def validate_manafacturer_name(self, manufacturer_name: str) -> bool:
        return "Fokker" in manufacturer_name or "BAE" in manufacturer_name

    def validate_model_name(self, model_name) -> bool:
        """Validates model name"""
        return "F100" in model_name or "F28" in model_name or "146" in model_name

    def validate_weeks(self, week: str) -> bool:
        try:
            int_week = int(week)
        except ValueError:
            return False
        if int_week <= 0 or int_week > 52:
            return False
        else:
            return True

    def validate_year(self, year: str) -> bool:
        try:
            year_int = int(year)
            if year_int >= 0:
                return True
        except ValueError:
            return False
    

    # destination
    def validate_destination_name(self, destination_name: str) -> bool:
        """Validates name input."""
        name_values = destination_name
        return len(name_values) >= 3 and all(
            (char.isalpha() for char in name_values)
        )

    def validate_destination_id(self, destination_id: str) -> bool:
        """Validates name input."""
        name_values = destination_id
        return len(name_values) == 3 and all(
            (char.isalpha() for char in name_values)
        )

    def validate_airport(self, airport_name: str) -> bool:
        """Validates name input."""
        name_values = airport_name.split()
        return (
            len(airport_name) >= 3
            and "Airport" in airport_name
            and all((char.isalpha() for char in name_values))
        )

    def validate_distance_from_iceland(self, distance_from_iceland: int) -> bool:
        """Validates distance from iceland."""
        try:
            distance_from_iceland = int(distance_from_iceland)
            return (distance_from_iceland >= 0) >=0 and (distance_from_iceland <= 40000) and all((digit.isdigit()for digit in str(distance_from_iceland)))
        except ValueError:
            return False
        
    

# menu 
    def validate_back_or_quit(self, user_input: str):
        """Validates back or quit fucntion."""
        return user_input.lower() == "b" or user_input == "q"

    # voyages
    def validate_flight_nr(slef, flight_number: str) -> bool:
        """Validates a flight numeber that the user inputs, checks whether the input is in the format
        NA000. That is, starts with NA and three numbers follow.
        """
        try:
            flight_number_int = int(flight_number[2:])
            flight_number_int += 1
            if len(flight_number[2:]) == 3 and flight_number[:2] == "NA":
                return True
            else:
                return False
        except ValueError:
            return False
    

    def validate_date(self, date:str) -> bool:
        """Validates dates"""
        if len(date) == 10:
            if date[0:4].isdigit() == True:
                if date[4] == "-" and date[7] == "-":
                    if date[5:7].isdigit() == True:
                        if date[8:].isdigit() == True:
                            return True
        return False
    

    def validate_time(self, time) -> bool:
        """Validates time."""
        try:
            hour, minute, second = time.split(":")
            hour_int = int(hour)
            minute_int = int(minute)
            second_int = int(second)
            if hour_int >= 0 and 0 <= minute_int <= 60 and 0 <= second_int <= 60:
                return True
        except ValueError:
            return False
        #if len(time) == 8:
        #    if time[0:2].isdigit() == True:
        #        if time[3] == ":" and time[5] == ":":
        #            if time[3:5].isdigit() == True:
        #                if time[6:].isdigit() == True:
        #                    return True
        #return False
    

