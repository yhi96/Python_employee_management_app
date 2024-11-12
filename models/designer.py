from models.employee import Employee

class Designer(Employee):
    def __init__(self, first_name, last_name, base_salary, experience, eff_coeff):
        super().__init__(first_name, last_name, base_salary, experience)

        self.eff_coeff = eff_coeff
    
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        return round(base_salary * self.eff_coeff)