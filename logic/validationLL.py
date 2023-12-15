from data.data_wrapper import DataWrapper
from datetime import datetime

class ValidationLL():
    def __init__(self) -> None:
        """Instantiate a ValidationLL object."""
        

    def validate_choice(self, action: str, option: int) -> bool:
        """ Validates numerical action input. """
        try:
            action = int(action)
            if action > 0 and action <= option:
                return True
            else: 
                return False
        except ValueError:
            return  False


    #employee
    def validate_name(self, name: str) -> bool:
        """ Validates name input. """
        name_values = name.split()
        return len(name) >=3 and all((char.isalpha()for char in name_values))
        

    def validate_social_ID(self, socialID: str) -> bool: 
        """ Validates social ID input. """
        return len(socialID) == 10 and all((digit.isdigit()for digit in socialID))
    
        
    def validate_number(self, number: str) -> bool:
        """ TODO: add docstring """
        return len(number) == 7 and all((digit.isdigit()for digit in number))
        

    def validate_email(self, email: str) -> bool:
        """ TODO: add docstring """
        return"@" in email and "." in email
    
    
    def validate_address(self, address: str) -> bool:
        address_values = address.split()
        if len(address_values) == 2:
            if address_values[1].isdigit() == True:
                return len(address) >=3 and all((char.isalpha()for char in address[0])) and (digit.isdigit() for digit in address[1])
        if len(address_values) == 1:
            return len(address) >=3 and all((char.isalpha()for char in address [0]))
        
    def validate_yes_no(self, input: str) -> bool:
        if input == "y" or input == "n":
            return True
        else:
            return False
    

    #airplanes   
    def validate_aircraft_by_specific_type(self, aircraft_specific_type) -> bool:
        return "N/A" in aircraft_specific_type
        
        
    def validate_airplane_name(self,aircraft_name) -> bool:
        if aircraft_name[0:2] == "TF":
            if aircraft_name[2] == "-":
                if type(aircraft_name[3:6]) == str:
                    return True
        else:
            return False
        
        # return "TF" in aircraft_name and "-" in aircraft_name
    
    #Airplane types and license, Pilots by license
        #Licensed pilots for a specific airplane type (ofkokfsd) = ValueError
    
    def validate_airplane_choice(self, airplane_choice: int) -> bool:
        try:
            airplane_choice = int(airplane_choice)
            return True
        except ValueError:
            return False
            

    
    


        

#nota þessa i koðanum til að laga
        
    def validate_manafacturer_name(self,manufacturer_name: str) -> bool:
        return "Fokker" in manufacturer_name or "BAE" in manufacturer_name

        
    def validate_model_name(self,model_name) -> bool:
        return "F100" in model_name or "F28" in model_name or "146" in model_name
    
        
    #def validate_number_of_seats(self, number_of_seats) -> bool:
    #    return len(number_of_seats) <= 110 and len(number_of_seats) >= 84

#validate the choosing dates

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
            int_year = int(year)
        except ValueError:
            return False
        
              
    def validate_save_new(self, str) -> bool:
        pass
    
    
    def validate_flight(self, flight: str) -> bool:
        """ TODO: add docstring """
        pass


    def validate_voyage(self, voyage: str) -> bool:
        """ TODO: add docstring """
        pass


    def date_validation(self, departure: datetime) -> bool:
        """ TODO: add docstring """
        pass

#destination

    def validate_all_destinations(self,all_destinations) -> bool:
        return 


            
    def validate_destination_name(self, destination_name: str) -> bool:
        """ Validates name input. """
        name_values = destination_name.split()
        return len(destination_name) >=3 and all((char.isalpha()for char in name_values))
    
    def validate_destination_id(self, destination_id: str) -> bool:
        """ Validates name input. """
        name_values = destination_id.split()
        return len(destination_id) >=3 and all((char.isalpha()for char in name_values))
    
    def validate_airport(self, airport_name: str) -> bool:
        """ Validates name input. """
        name_values = airport_name.split()
        return len(airport_name) >=3 and "Airport" in airport_name and all((char.isalpha()for char in name_values))
    
    def validate_distance_from_iceland(self, distance_from_iceland: int) -> bool:
        try:
            distance_from_iceland = int(distance_from_iceland)
            return (distance_from_iceland) >=0 and (distance_from_iceland) <= 400000 and all((digit.isdigit()for digit in distance_from_iceland))
        except ValueError:
            return False
    
# menu 
    def validate_back_or_quit(self, user_input: str):
        return user_input.lower() == "b" or user_input == "q"
    
    
# voyages
    def validate_flight_nr(slef, flight_number: str) -> bool:
        """ Validates a flight numeber that the user inputs, checks whether the input is in the format
        NA000. That is, starts with NA and three numbers follow.
        """
        try:
            flight_number_int = int(flight_number[2:])
        except ValueError:
            flight_number_int = None
            return False
        return (flight_number[:2] == "NA") and 999 >= flight_number_int >= 100 and len(flight_number) == 5