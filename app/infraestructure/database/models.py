from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime,Enum
from .database_configuration import Base
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid
from sqlalchemy.orm import relationship
from enum import Enum as EnumClass

class Status(str,EnumClass):
    ACTIVE="active"
    ON_VACATION="on vacation"
    INACTIVE="inactive"

class UserRole(str,EnumClass):
    ADMIN="admin"
    MANAGER="manager"
    VIEWER="viewer"


class Company(Base):
    __tablename__="company"
    id=Column(Integer, primary_key=True, autoincrement=True, index=True)
    tenant_id=Column(UUID(as_uuid=True), default=uuid.uuid4, index=True, nullable=True)
    company_name=Column(String, index=True, nullable=False, unique=True)
    contact_email=Column(String, unique=True)
    country=Column(String)
    employees=relationship("Employee", back_populates="company")
    users=relationship("Users", back_populates="company")

class Employee(Base):
    __tablename__="employee"
    id=Column(Integer, primary_key=True, autoincrement=True, index=True)
    employee_name=Column(String, unique=True, index=True,nullable=False)
    description=Column(String(2000))
    profile_pic=Column(String)
    email=Column(String, unique=True, index=True,nullable=False)
    charge=Column(String)
    department=Column(String)
    date_of_hire=Column(DateTime, default=datetime.datetime.utcnow)
    company_id=Column(Integer, ForeignKey("company.id"))
    company=relationship("Company", back_populates="employees")
    personal_info=relationship("EmployeePersonalInfo",back_populates="employee")
    status=Column(Enum(Status), index=True, default="active",nullable=False)



class EmployeePersonalInfo(Base):
    __tablename__="employee_info"
    id=Column(Integer, primary_key=True, autoincrement=True, index=True)
    employee_id=Column(Integer,ForeignKey("employee.id"))
    employee=relationship("Employee", back_populates="personal_info")
    country=Column(String)
    personal_number=Column(String)
    city=Column(String)
    current_address=Column(String)
    date_of_birthday=Column(DateTime)
    document_number=Column(Integer)
    

class Users(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_name=Column(String, index=True, unique=True, nullable=False)
    password=Column(String, nullable=False)
    email=Column(String, index=True, unique=True, nullable=False)
    created_at=Column(DateTime, default=datetime.datetime.now)

    role=Column(Enum(UserRole), default="viewer", index=True)
    company_id=Column(Integer, ForeignKey("company.id"))
    company=relationship("Company", back_populates="users")
    


