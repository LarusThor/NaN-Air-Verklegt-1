from data.data_wrapper import DataWrapper
from datetime import datetime

class ValidationLL():
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        pass

    def validate_name(self, name: str) -> bool:
        pass

    def validate_social_ID(self, socialID: str) -> bool:
        pass

    def validate_flight(self, flight: str) -> bool:
        pass

    def validate_address(self, address: str) -> bool:
        pass

    def validate_number(self, number: str) -> bool:
        pass

    def validate_email(self, email: str) -> bool:
        pass

    def validate_flight_nr(self, flight_nr: str) -> bool:
        pass

    def validate_voyage(self, voyage: str) -> bool:
        pass

    def date_validation(self, departure: datetime) -> bool:
        pass