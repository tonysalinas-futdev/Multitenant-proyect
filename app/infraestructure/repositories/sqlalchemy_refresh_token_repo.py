from app.infraestructure.repositories.sqlalchemy_generic_crud import SqlAlchemyGenericCrud
from app.core.application.repositories.refresh_token_interface import RefreshTokenInterface

from app.infraestructure.database.models import RefreshToken
from sqlalchemy import select
from sqlalchemy.orm import selectinload

class SqlAlchemyRefreshTokenRepo(RefreshTokenInterface,SqlAlchemyGenericCrud):
    def __init__(self,session):
        super().__init__(session, RefreshToken)
    async def get_token_by_value(self, token_value:str):
        stmt=select(RefreshToken).options(
            selectinload(RefreshToken.user)
        ).where(RefreshToken.token==token_value)
        result=await self.session.execute(stmt)
        token=result.scalar_one_or_none()
        return token
    
    async def revoke_token(self, token:RefreshToken):
        token.is_revoked=True
        await self.session.commit()
        await self.session.refresh(token)

    async def get_all_revoked_tokens(self):
        stmt=select(RefreshToken).where(RefreshToken.is_revoked==True)
        result= await self.session.execute(stmt)
        tokens=result.scalars().all()
        return tokens
    
