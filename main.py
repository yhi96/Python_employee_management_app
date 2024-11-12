#Checking if methods implemented in employee.py are working properly
from models.employee import Employee

employee = Employee("Yoana", "Ivanova", 1000, 3)
salary = employee.calculate_salary()

print(f"{employee.first_name} {employee.last_name} will receive {salary} money.")

#Checking if method performs as expected designer.py
from models.designer import Designer

def designer():
    designer = Designer("Ivan", "Dimitrov", 1000, 6, 0.5)

    print(f"Designer: {designer.first_name} {designer.last_name}")

    salary = designer.calculate_salary()
    print(f"Salary: {salary}")

if __name__ == "__main__":
    designer()

#Checking if method performs as expected manager.py
from models.employee import Employee
from models.developer import Developer
from models.manager import Manager

def manager():

    developer1 = Developer("Nikoleta", "Georgieva", 1500, 4)
    developer2 = Developer("Stanislava", "Nikolova", 1500, 3)
    developer3 = Developer("Ivan", "Dimitrov", 1500, 2)
    
    team = [developer1, developer2, developer3]
    manager = Manager("Sofia", "Hristova", 2000, 6, team)
    
    salary_manager = manager.calculate_salary()
    print(f"Manager: {manager.first_name} {manager.last_name} will receive {salary_manager} money.")

if __name__ == "__main__":
    manager()

#Checking if department.py performs as expected
from models.department import Department
from models.manager import Manager
from models.developer import Developer
from models.designer import Designer

def team():
    
    developer1 = Developer("Nikoleta", "Georgieva", 1500, 4)
    designer1 = Designer("Ivan", "Dimitrov", 1000, 6, 0.5)
    developer2 = Developer("Stanislava", "Nikolova", 1500, 3)
    
    manager1 = Manager("Sofia", "Hristova", 2000, 6, [developer1, designer1])
    manager2 = Manager("Hristo", "Atanasov", 1200, 7, [developer2])
    
    department = Department([manager1, manager2])

    department.save_employees("employees.json")
    
    new_department = Department([])
    new_department.load_employees("employees.json")

    new_department.give_salary()

if __name__ == "__main__":
    team()


