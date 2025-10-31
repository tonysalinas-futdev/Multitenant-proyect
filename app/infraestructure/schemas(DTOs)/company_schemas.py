from pydantic import BaseModel,EmailStr
from typing import Optional
from employee_schemas import EmployeeBase
from typing import List

class CompanyBase(BaseModel):
    id:int
    tenant_id:int
    company_name:str
    contact_email:EmailStr
    country:str
    emplooyess:List[EmployeeBase]

class CreateCompany(BaseModel):
    company_name:str
    contact_email:EmailStr
    country:str

class UpdateCompany(BaseModel):
    company_name:Optional[str]=None
    contact_email:Optional[EmailStr]=None
    country:Optional[str]=None