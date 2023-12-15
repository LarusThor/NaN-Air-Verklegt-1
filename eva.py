
from logic.validationLL import ValidationLL
from logic.logic_wrapper import LogicWrapper

vali = ValidationLL()
logic = LogicWrapper()

dd = "00:00:90"


print(vali.validate_time(dd))