class Employee:
    def __init__(self, first_name, last_name, base_salary, experience):

        self.first_name = first_name
        self.last_name = last_name
        self.base_salary = base_salary
        self.experience = experience

    def calculate_salary(self):
        if self.base_salary < 0:
            return 0
        
        if self.experience > 5:
            return self.base_salary * 1.2 + 500 
        elif self.experience > 2:
            return self.base_salary + 200
        else:
            return self.base_salary