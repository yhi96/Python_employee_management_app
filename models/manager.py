from models.employee import Employee
from models.developer import Developer
from models.designer import Designer

class Manager(Employee):
    def __init__(self, first_name, last_name, base_salary, experience, team=None):
        super().__init__(first_name, last_name, base_salary, experience)
        self.team = team if team else []

    def calculate_salary(self):
        base_salary = super().calculate_salary()

        developers_count = sum(1 for member in self.team if isinstance(member, Developer))
        designers_count = sum(1 for member in self.team if isinstance(member, Designer))

        if developers_count > designers_count:
            base_salary *= 1.1 

        if len(self.team) > 10:
            base_salary += 300
        elif len(self.team) > 5:
            base_salary += 200
        
        if developers_count > len(self.team) / 2:
            base_salary *= 1.1

        return round(base_salary)