from entities.employee import Employee, EmployeeInfo
from typing import List
import uuid
class Company():
    id:int
    tenant_id:uuid.UUID
    company_name:str
    contact_email:str
    country:str
    employees:List[Employee]
    def __init__(self, id:int, company_name:str, contact_email:str, country:str):
        self.id=id
        self.tenant_id=uuid.uuid4
        self.company_name=company_name
        self.contact_email=contact_email
        self.country=country
        self.employees=[]

    def add_employee(self, employee:Employee,):
        existing_employees=[empl.employee_name for empl in self.employees]
        if employee.employee_name in existing_employees:
            raise ValueError("Ya tiene un empleado con ese nombre")
        self.employees.append(employee)

    

            