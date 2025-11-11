from app.core.application.repositories.generic_crud_interface import GenericCRUDInterface
from abc import abstractmethod
from app.infraestructure.database.models import RefreshToken

class RefreshTokenInterface(GenericCRUDInterface):
    @abstractmethod
    async def get_token_by_value(self, token_value:str):
        pass

    @abstractmethod 
    async def revoke_token(self, token:RefreshToken):
        pass

    @abstractmethod
    async def get_all_revoked_tokens(self):
        pass