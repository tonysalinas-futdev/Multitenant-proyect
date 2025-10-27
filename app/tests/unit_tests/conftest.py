from app.core.domain.entities.company import Company
from app.core.domain.entities.employee import Employee, EmployeeInfo
from app.infraestructure.database.models import Status
import pytest
from faker import Faker
import random

@pytest.fixture
def return_company():
    return Company(id=1, country="Cuba",contact_email="example@gmail.com", company_name="Helados SA")


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