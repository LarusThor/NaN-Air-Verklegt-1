from data.data_wrapper import DataWrapper
from datetime import datetime

class ValidationLL():
    def __init__(self) -> None:
        """Instantiate a ValidationLL object."""

    # menu manager
    def get_next_action(self, action):
        """Takes the input from the user from the get_next_action function in the Menu class. Checks if it b or q.
        Return true if it is b or q and false if it is something else."""
        if action == "b" or action == "q":
            return True
        else:
            return False

    #employee
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
        except :# chacha error todo value error eða keky error
            return False


    def validate_number(self, number: str) -> bool:
        """ TODO: add docstring """
        try:
            if len(number) == 7:
                return True
        except :
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
        except :
            return False
        
    def validate_print_crew(self, list_crew: str) -> bool:
        
        if "m" in list_crew and "r" in list_crew:
            return True
        else:
            return False
        
    #airplanes   
    def validate_aircraft_by_specific_type(self,aircraft_specific_type) -> bool:
        if "NA" in aircraft_specific_type:
            return True
        else:
            return False
        
    def validate_airplane_name(self,aircraft_name) -> bool:
        if "TF" in aircraft_name and "-" in aircraft_name:
            return True
        else:
            return False
        
    def validate_manafacturer_name(self,manufacturer_name: str) -> bool:
        if "Fokker" in manufacturer_name and "BAE" in manufacturer_name:
            #virkar ekki fyrir Fokker og BAe
            return True
        else:
            return False
        
    def validate_model_name(self,model_name) -> bool:
        if "F100" in model_name and "F28" in model_name and "146" in model_name:
            return True
        else:
            return False
        
    def validate_number_of_seats(self, number_of_seats: str) -> bool:
        """ TODO: add docstring """
        try: 
            if len(number_of_seats) <= 110 and len(number_of_seats) >= 84:
                return True
        except:
            return False
        
        
        
    def validate_save_new(self,str) -> bool:
        pass
    
    def validate_home_and_quit(self,str) -> bool:
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
