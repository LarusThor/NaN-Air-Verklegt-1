from data.data_wrapper import DataWrapper
from datetime import datetime

class ValidationLL():
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        pass


    def validate_name(self, name: str) -> bool:
        """ Validates name input. """
        #TODO:
        if len(name) >= 3:
            return True
        else:
            return False


    def validate_social_ID(self, socialID: str) -> bool:
        """ Validates social ID input. """
        try:
            if len(socialID) == 10:
                return True
        except Exception:# chacha error todo value error eða keky error
            return False


    def validate_number(self, number: str) -> bool:
        """ TODO: add docstring """
        try:
            if len(number) == 7:
                return True
        except Exception:
            return False


    def validate_email(self, email: str) -> bool:
        """ TODO: add docstring """
        if "@" in email and "." in email:
            return True
        else:
            return False
    
    
    def validate_address(self, address: str) -> bool:
        """ TODO: add docstring """
        try: 
            if len(address) >= 3:
                return True
        except Exception:
            return False
        
    def validate_print_crew(self, list_crew: str) -> bool:
        
        if "m" in list_crew and "r" in list_crew:
            return True
        else:
            return False
    
        
       
        
        
        
    
        
        
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
