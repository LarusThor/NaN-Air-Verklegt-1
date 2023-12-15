import csv
from model.employee_model import Employee
from pathlib import Path


class EmployeeIO:
    def read_employee(self) -> dict:
        """Returns employee information form csv file and returns employee dict."""
        employee_dict = {}
        with open("files/crew.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                line = line.strip()
                (social_id, name, role, rank, license, address, phone_nr, email, landline,) = line.split(",")

                employee = Employee(
                    name,
                    social_id,
                    role,
                    rank,
                    license,
                    email,
                    phone_nr,
                    address,
                    landline,
                )
                employee_dict[social_id] = employee

        return employee_dict

    def write_employees(self, employees: list[Employee]) -> None:
        """Updates crew csv file."""
        file_path = Path("files/crew.csv")

        fieldnames = [
            "social_id",
            "name",
            "role",
            "rank",
            "licence",
            "address",
            "phone_nr",
            "email",
            "landline",
        ]

        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for employee in employees:
                writer.writerow(
                    {
                        "social_id": employee.social_id,
                        "name": employee.name,
                        "role": employee.role,
                        "rank": employee.rank,
                        "licence": employee.licence,
                        "address": employee.home_address,
                        "phone_nr": employee.phonenumber,
                        "email": employee.email,
                        "landline": employee.landline,
                    }
                )
