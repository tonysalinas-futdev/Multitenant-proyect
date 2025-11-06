from pydantic import BaseModel,EmailStr,Field
from typing import Optional
from datetime import datetime
from app.core.domain.constants.constants import Status


class EmployeeInfo(BaseModel):
    country:str
    personal_number:str
    city:str
    current_address:str
    date_of_birthday:datetime
    document_number:str


class EmployeeInfoBase(EmployeeInfo):
    id:int
    employee_id:int


class EmployeeBase(BaseModel):
    id:int
    employee_name:str
    email:EmailStr
    description:str
    charge:str
    department:str
    date_of_hire:datetime
    status:Status
    personal_info:EmployeeInfo
    company_id:int


class CreateAndUpdatePersonalInfo(BaseModel):
    country:Optional[str]=None
    personal_number:Optional[str]=None
    city:Optional[str]=None
    current_address:Optional[str]=None
    date_of_birthday:Optional[datetime]=None
    document_number:Optional[str]=None


class CreateEmployee(BaseModel):
    employee_name:str
    email:EmailStr
    description:Optional[str]=Field(default=None, max_length=2000)
    charge:Optional[str]=None
    department:Optional[str]=None
    status:Status
    personal_info:CreateAndUpdatePersonalInfo

class UpdateEmployee(BaseModel):
    employee_name:Optional[str]=None
    email:Optional[EmailStr]=None
    description:Optional[str]=Field(default=None, max_length=2000)
    charge:Optional[str]=None
    department:Optional[str]=None
    status:Optional[Status]=None
    personal_info:CreateAndUpdatePersonalInfo
    

