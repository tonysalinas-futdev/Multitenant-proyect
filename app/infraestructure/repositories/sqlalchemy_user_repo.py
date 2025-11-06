from app.infraestructure.repositories.sqlalchemy_generic_crud import SqlAlchemyGenericCrud
from app.core.application.repositories.user_interface import UserRepositoryInterface

from app.infraestructure.database.models import Users
from sqlalchemy import select
from sqlalchemy.orm import selectinload


class SqlalchemyUserRepo(UserRepositoryInterface,SqlAlchemyGenericCrud[Users]):
    def __init__(self, session):
        super().__init__(session, Users)

    async def get_by_id(self, object_id:int):
        stmt=select(Users).options(
        selectinload(Users.company)
        ).where(Users.id==object_id)

        result=await self.session.execute(stmt)
        user=result.scalar_one_or_none()
        return user



    async def get_by_email(self,email:str)->Users:
        query=select(Users).where(Users.email==email)
        result=await self.session.execute(query)
        user_object=result.scalar_one_or_none()
        return user_object
    
    async def get_by_user_name(self,username:str)->Users:
        query=select(Users).where(Users.user_name==username)
        result=await self.session.execute(query)
        user_object=result.scalar_one_or_none()
        return user_object
        