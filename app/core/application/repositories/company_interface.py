from abc import  abstractmethod
from app.core.application.repositories.generic_crud_interface import GenericCRUDInterface


class CompanyRepositoryInterface(GenericCRUDInterface):
    @abstractmethod
    async def get_by_company_name(self, company_name:str):
        pass

    @abstractmethod 
    async def get_by_email(self,email:str):
        pass

    @abstractmethod
    async def get_by_country(self, email:str):
        pass