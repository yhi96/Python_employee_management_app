from models.employee import Employee
from models.developer import Developer
from models.manager import Manager
from models.designer import Designer
from models.developer import Developer
import json

class Department:
    def __init__(self, managers):
        self.managers = managers

    def give_salary(self):
        for manager in self.managers:
            Department.print_salary(manager)
            for employee in manager.team:
                Department.print_salary(employee)
    
    def print_salary(employee):
        print(f"{employee.first_name} {employee.last_name} received: {employee.calculate_salary()} money.")

    def save_employees(self, filename):
        try:
            with open(filename, 'w') as f:
                json.dump([Department.serialize_manager(manager) for manager in self.managers], f, indent=4)
        except IOError:
            print("Error saving the file.")
    
    def load_employees(self, filename):
        try:
            with open(filename, 'r') as f:
                manager_data = json.load(f)
                self.managers = [Department.deserialize_manager(data) for data in manager_data]
        except FileNotFoundError:
            print("File not found.")

    def serialize_manager(manager):
        return {
            "first_name": manager.first_name,
            "last_name": manager.last_name,
            "base_salary": manager.base_salary,
            "experience": manager.experience,
            "team": [
                {
                    "type": "Developer" if isinstance(member, Developer) else "Designer",
                    "first_name": member.first_name,
                    "last_name": member.last_name,
                    "base_salary": member.base_salary,
                    "experience": member.experience,
                    "eff_coeff": getattr(member, "eff_coeff", None)
                } for member in manager.team
            ]
        }
    
    def deserialize_manager(data):
        team = []
        for member_data in data["team"]:
            member_data_copy = member_data.copy()
            member_data_copy.pop("type", None)

            if "eff_coeff" in member_data_copy:
                eff_coeff = member_data_copy.pop("eff_coeff")
            else:
                eff_coeff = None

            if member_data["type"] == "Developer":
                team.append(Developer(**member_data_copy))
            elif member_data["type"] == "Designer":
                team.append(Designer(**member_data_copy, eff_coeff=eff_coeff))
        
        return Manager(data["first_name"], data["last_name"], data["base_salary"], data["experience"], team)