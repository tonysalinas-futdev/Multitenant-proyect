from app.core.domain.entities.company import Company
from app.core.domain.entities.employee import Employee, EmployeeInfo
from app.core.domain.entities.user import User
from app.core.domain.constants.constants import Status, UserRole
import pytest
from faker import Faker
import random

@pytest.fixture
def return_company():
    return Company(id=1, country="Cuba",contact_email="example@gmail.com", company_name="Helados SA")

@pytest.fixture
def return_employee():
    info=EmployeeInfo(country="Cuba", city="La habana", personal_number="+53 52000748",current_address="Panchito Gómez", date_of_birthday="25/05/2004",document_number="12345678")

    return Employee(1,"Tony Salinas","Muchacho de 21 años y mestizo","kroosismo0202@gmail.com","presidente","45",1,Status.ACTIVE,personal_info=info)

@pytest.fixture
def return_test_user():
    return User(1,"Pedro Salinas","Abcd1234#","example@gmail.com",UserRole.ADMIN,1)


@pytest.fixture
def create_list_of_employees():
    faker=Faker()
    available_statuses={1:Status.ACTIVE, 2: Status.INACTIVE, 3:Status.ON_VACATION}
    employees_info_list=[EmployeeInfo(
        country=faker.country(),
        city=faker.city(),
        personal_number=faker.phone_number(),
        date_of_birthday=faker.date(),
        document_number=faker.ssn()
        ) for i in range(11)]
    
    employees_list=[
        Employee(
            id=faker.random_number(),
            employee_name=faker.name(),
            description=faker.text(),
            department=faker.word(),
            company_id=faker.random_number(),
            email=faker.email(),
            charge=faker.job(),
            status=available_statuses[random.randint(1,3)],
            personal_info=employees_info_list[random.randint(0,10)]) for i in range(10)]

    return employees_list