from app.infraestructure.database.models import Users
from abc import ABC, abstractmethod
from typing import List
from app.core.application.repositories import GenericCRUDInterface

class UserRepositoryInterface(ABC, GenericCRUDInterface):
    @abstractmethod
    async def get_by_email(self,email:str)->Users:
        pass
    
    @abstractmethod
    async def get_by_user_name(self,username:str)->Users:
        pass

