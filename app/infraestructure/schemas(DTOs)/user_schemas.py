from pydantic import BaseModel, Field,  ConfigDict,EmailStr,field_validator, model_validator
from app.core.domain.constants.constants import  UserRole
from datetime import datetime
from app.utils.validator import password_field_validator, validate_password

from typing import Optional
class User(BaseModel):
    user_name:str
    email:EmailStr
    

class UserBase(User):
    id:int
    created_at:datetime
    company_id:int
    password:str
    role:UserRole

class SignUp(BaseModel):
    user_name:str=Field(
        ...,
        max_length=100,
        min_length=5 )

    email:EmailStr=Field(...)
    password:str=password_field_validator()
    @field_validator("password")
    def validate_password_field(cls, valor):
        return validate_password(valor)
    model_config=ConfigDict(from_attributes=True)
    
    

class SignIn(BaseModel):
    email:EmailStr=Field(
        ...
    )

    password:str=password_field_validator()
    @field_validator("password",mode="after")
    @classmethod
    def validate_password_field(cls, valor):
        return validate_password(valor)


class UpdateUser(BaseModel):
    user_name:Optional[str]=None
    email=Optional[str]=None


class ForgotPassword(BaseModel):
    new_password:str=password_field_validator()


class UpdatePassword(ForgotPassword):
    
    current_passwordstr=password_field_validator()
    @field_validator("new_password","current_password",mode="after")
    @classmethod
    def validate_password_field(cls, valor):
        return validate_password(valor)