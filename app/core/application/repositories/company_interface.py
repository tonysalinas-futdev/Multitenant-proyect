from app.infraestructure.database.models import Users
from abc import ABC, abstractmethod
from typing import List
from app.core.application.repositories import GenericCRUDInterface

class CompanyRepositoryInterface(ABC,GenericCRUDInterface):
    @abstractmethod
    async def get_by_company_name(self, company_name:str):
        pass

    @abstractmethod 
    async def get_by_email(self,email:str):
        pass