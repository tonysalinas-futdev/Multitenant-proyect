from app.infraestructure.database.models import Users
from abc import ABC, abstractmethod
from typing import List
from app.core.domain.repositories.generic_crud_interface import GenericCRUDInterface

class CompanyInterface(ABC,GenericCRUDInterface):
    @abstractmethod
    async def get_by_company_name(self, company_name:str):
        pass

    @abstractmethod 
    async def get_by_email(self,email:str):
        pass