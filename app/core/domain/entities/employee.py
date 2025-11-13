from app.infraestructure.database.models import Status
from datetime import datetime
class EmployeeInfo():
    country:str
    city:str
    personal_number:str
    current_address:str
    date_of_birthday:datetime
    document_number:str

    def __init__(self,country:str=None, city:str=None,personal_number:str=None, date_of_birthday:str=None,document_number:str=None, current_address=None):
        self.city=city
        self.country=country
        self.current_address=current_address
        self.document_number=document_number
        self.date_of_birthday=date_of_birthday
        self.personal_number=personal_number
        


class Employee():
    id:int
    def __init__(self , employee_name:str, description:str,  email:str,charge:str, department:str, company_id:int, status:Status,profile_pic:str=None,personal_info:EmployeeInfo=None):
        if not isinstance(status,Status):
            raise ValueError("El estado introducido no es válido")
        
        self.employee_name=employee_name
        self.description=description
        self.profile_pic=profile_pic
        self.email=email
        self.charge=charge
        self.department=department
        self.company_id=company_id
        self.status=status
        self.personal_info=personal_info



        