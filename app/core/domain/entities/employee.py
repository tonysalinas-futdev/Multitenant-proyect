class Employee():
    def __init__(self, id:int , employee_name:str, description:str, profile_pic:str, email:str,charge:str, department:str, company_id:int):
        self.id=id
        self.employee_name=employee_name
        self.description=description
        self.profile_pic=profile_pic
        self.email=email
        self.charge=charge
        self.department=department
        self.company_id=company_id

class EmployeeInfo():
    country:str
    city:str
    personal_number:str
    current_address:str
    date_of_birthday:str
    document_number:str

        