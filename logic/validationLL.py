from data.data_wrapper import DataWrapper
from datetime import datetime

class ValidationLL():
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        pass

    def validate_name(self, name: str) -> bool:
        #TODO: laga svo að hann leyfi bil
        if name.isalpha() and len(name) >= 5:
            return True
        else:
            return False

    def validate_social_ID(self, socialID: str) -> bool:
        try:
            social_id = int(socialID)
            if len(social_id) == 10:
                return True
        except Exception:
            return False

        

    def validate_flight(self, flight: str) -> bool:
        pass

    def validate_address(self, address: str) -> bool:
        pass

    def validate_number(self, number: str) -> bool:
        try:
            phone_number = int(number)
            if len(phone_number) == 8:
                return True
        except Exception:
            return False

    def validate_email(self, email: str) -> bool:
        if "@" in email and "." in email:
            return True
        else:
            return False

    def validate_flight_nr(self, flight_nr: str) -> bool:
        pass

    def validate_voyage(self, voyage: str) -> bool:
        pass

    def date_validation(self, departure: datetime) -> bool:
        pass