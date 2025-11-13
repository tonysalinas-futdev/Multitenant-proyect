from app.core.domain.entities.employee import Employee, EmployeeInfo
from typing import List
import uuid
from app.core.domain.constants.constants import Status
from datetime import datetime
from app.utils.validator import validate_email
class Company():
    id:int
    tenant_id:uuid.UUID
    company_name:str
    contact_email:str
    country:str
    employees:List[Employee]
    def __init__(self, company_name:str, contact_email:str, country:str):
        if company_name is None or contact_email is None:
            raise ValueError("Debe introducir un nombre y un email para registrar su empresa")
        validate_email(contact_email)
        self.tenant_id=uuid.uuid4
        self.company_name=company_name
        self.contact_email=contact_email
        self.country=country
        self.employees=[]

    def add_employee_to_company(self, employee:Employee):
        existings_employees_names=[empl.employee_name for empl in self.employees]
        existings_emails=[empl.email for empl in self.employees]
        if employee.employee_name in existings_employees_names or employee.email in existings_emails:
            raise ValueError("Ya existe un empleado registrado con ese correo o nombre")
        self.employees.append(employee)

    def edit_employee_data(self, employee:Employee, new_name:str, new_description:str,profile_pic:str, new_email:str, new_charge:str, new_department:str, new_status:Status,new_personal_info:EmployeeInfo):
            existing_ids=[empl.id for empl in self.employees]
            if employee.id not in existing_ids:
                raise ValueError("No se ha podido encontrar a ese empleado")
            employee.employee_name=new_name
            employee.email=new_email
            employee.charge=new_charge
            employee.description=new_description
            employee.profile_pic=profile_pic
            employee.department=new_department
            employee.personal_info=new_personal_info
                
            
    def change_employee_status(self,employee:Employee, new_status:Status):
        if not isinstance(new_status,Status):
            raise ValueError("El estado introducido no es válido")
        employee.status=new_status
