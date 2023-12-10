from logic.employeeLL import EmployeeLL
from model.employee_model import Employee
from logic.destinationLL import DestinationLL
from model.past_voyage_model import PastVoyage
from logic.past_voyageLL import PastVoyageLL
from logic.scheduleLL import ScheduleLL
from logic.airplaneLL import AirplaneLL


test = AirplaneLL()
sched_ll = ScheduleLL()

print(test.get_airplane_usage())





"""
schedule_stuff = ScheduleLL()

print(schedule_stuff.schedule_employee_by_week("2706838569", "2023", "45"))
"""


"""
employee_ll = EmployeeLL()


employee = Employee(
    social_id="2706838569",
    name="Gerard Norris",
    role="Pilot",
    rank="Captain",
    licence="NAFokkerF100",
    email="bruck@comcast.net",
    phonenumber="8998801",
    home_address="Fellsmúli 4",
    landline="7854878"
)


voyage = PastVoyage(
    flight_nr= "NA031",
    dep_from= "KEF",
    arr_at= "LYR",
    departure="2023-11-16 06:21:00",
    arrival= "2023-11-16 10:21:00",
    aircraft_id= "TF-EPG",
    captain= "3009907461",
    copilot= "2410876598",
    fsm ="1405853585",
    fa1 ="409907212",
    fa2 ="505942924",
    fa3 =  "N/A",
    fa4 = "N/A",
    fa5 = "N/A",
    seats_sold = "N/A"

)

print(employee_ll.get_total_hours_worked(employee))

"""


"""
dest_ll = DestinationLL()

print(dest_ll.get_most_popular_destination())
"""

"""
emp_ll = EmployeeLL()

employee = Employee(
    social_id="broseph",
    name="Bruh Johnson",
    role="test_role",
    rank="test_rank",
    licence="f",
    email="f@f.f",
    phonenumber="0.5",
    home_address="bruh street 69",
    landline="??"
)

emp_ll.change_employee_info(employee)
"""