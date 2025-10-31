from app.infraestructure.database.models import Users
from abc import ABC, abstractmethod
from typing import List
from app.core.domain.repositories.generic_crud_interface import GenericCRUDInterface

class UserInterface(ABC, GenericCRUDInterface):
    @abstractmethod
    def get_by_email(email:str):
        pass
    
    @abstractmethod
    def get_by_user_name(username:str):
        pass

