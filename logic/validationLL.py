from data.data_wrapper import DataWrapper
from datetime import datetime

class ValidationLL():
    def __init__(self) -> None:
        """Instantiate a ValidationLL object."""
        

    def validate_action(self, action: int, option: int) -> bool:
        """ Validates numerical action input. """
        if action.isnumeric():
            action = int(action)
            if action > 0 and action <= option:
                return True
        else: 
            return False


    #employee
    def validate_name(self, name: str) -> bool:
        """ Validates name input. """
        return len(name) >=3 and all((char.isalpha()for char in name))
        

    def validate_social_ID(self, socialID: str) -> bool:
        """ Validates social ID input. """
        return len(socialID) ==10 and all((digit.isdigit()for digit in socialID))
        
        
    def validate_number(self, number: str) -> bool:
        """ TODO: add docstring """
        return len(number) ==7 and all((digit.isdigit()for digit in number))
        

    def validate_email(self, email: str) -> bool:
        """ TODO: add docstring """
        return"@" in email and "." in email
    
    
    def validate_address(self, address: str) -> bool:
        address_values = address.split()
        address_number = int(address_values[1])
        if len(address) == 2:
            return len(address_values) >=3 and all(char.isalpha() for char in address[0]) and all(char.isdigit() for char in address_number) #and digit.isdigit() for digit in address [1])
        elif len(address) == 1:
            return len(address_values) >=3 and all(char.isalpha() for char in address[0]) #and digit.isdigit() for digit in address [1])
        
        
    #airplanes   
    def validate_aircraft_by_specific_type(self, aircraft_specific_type) -> bool:
        return "N/A" in aircraft_specific_type
        
        
    def validate_airplane_name(self,aircraft_name) -> bool:
        return "TF" in aircraft_name and "-" in aircraft_name
        

#nota þessa i koðanum til að laga
        
    def validate_manafacturer_name(self,manufacturer_name: str) -> bool:
        return "Fokker" in manufacturer_name or "BAE" in manufacturer_name

        
    def validate_model_name(self,model_name) -> bool:
        return "F100" in model_name or "F28" in model_name or "146" in model_name
    
        
    def validate_number_of_seats(self, number_of_seats) -> bool:
        return len(number_of_seats) <= 110 and len(number_of_seats) >= 84
        
              
    def validate_save_new(self,str) -> bool:
        pass
    
    
    def validate_flight(self, flight: str) -> bool:
        """ TODO: add docstring """
        pass


    def validate_flight_nr(self, flight_nr: str) -> bool:
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