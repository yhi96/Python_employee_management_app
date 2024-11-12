import pytest
from models.developer import Developer
from models.designer import Designer
from models.manager import Manager
from models.department import Department
from models.employee import Employee

#Developers
def test_dev_salary():
    dev = Developer("John", "Albert", 1800, 6)
    assert dev.calculate_salary() == 2660

def test_dev_salary_negative_experience():
    dev = Developer("Jonas", "Alberto", 1800, -6)
    assert dev.calculate_salary() == 1800

def test_dev_salary_negative():
    dev = Developer("Jame", "Oliver", -500, 6)
    assert dev.calculate_salary() == 0

#Designers
def test_designer_salary():
    designer = Designer("Peter", "Kurtev", 2500, 12, 1.0)
    assert designer.calculate_salary() == 3500

#Managers
def test_manager_salary():
    dev1 = Developer("Dev", "1", 1500, 3)
    dev2 = Developer("Dev", "2", 1900, 5)
    team = [dev1, dev2]
    manager = Manager("Sofia", "Hristova", 4500, 15, team)
    assert manager.calculate_salary() == 6490

def test_manager_no_team_salary():
    manager = Manager("Sofia", "Hristova", 2500, 2,)
    assert manager.calculate_salary() == 2500

#Department
def test_department_salary(capfd):
    dev = Developer("Dev", "1", 3000, 3)
    manager = Manager("Niki", "Vasilkovski", 5000, 7, [dev])
    department = Department([manager])
    department.give_salary()
    out, err = capfd.readouterr()

    assert "Dev 1 received: 3200 money." in out
    assert "Niki Vasilkovski received: 7150 money." in out
