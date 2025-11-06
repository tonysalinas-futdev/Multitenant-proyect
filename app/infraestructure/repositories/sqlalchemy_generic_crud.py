from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.application.repositories.generic_crud_interface import GenericCRUDInterface
from typing import TypeVar,Type,Generic,List
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase
T=TypeVar("T", bound=DeclarativeBase)

class SqlAlchemyGenericCrud(GenericCRUDInterface,Generic[T]):
    def __init__(self, session:AsyncSession, model:Type[T]):
        self.session=session
        self.model=model

    async def save(self, sqlalchemy_object:T)->None:
        self.session.add(sqlalchemy_object)
        await self.session.commit()
        await self.session.refresh(sqlalchemy_object)

    async def get_by_id(self, object_id:int)->T:
        query=select(self.model).where(self.model.id==object_id)
        result=await self.session.execute(query)
        object_=result.scalar_one_or_none()

        return object_ 
    
    async def get_all_objects(self,limit=10, cursor=0)->List[T]:
        query=select(self.model).where(self.model.id>cursor).order_by(self.model.id).limit(limit)
        result=await self.session.execute(query)
        objects=result.scalars().all()
        return objects

    async def update(self, object:T, new_object:BaseModel)->None:
        """
        Función para actualizar un objeto, primero convierte a un dicc los valores del modelo pydantic que le pasamos y nos aseguramos de dejar fuera los valores None, luego comprueba que cada clave sea un atributo del objeto que queremos modificar y que ademas no sea , de ser así , lo seteamos
        """
        new_object_attrs=new_object.model_dump(exclude_none=True)
        for attr, attr_value in new_object_attrs.items():
            if hasattr(object,attr):
                setattr(object,attr,attr_value)
            
        await self.session.commit()
        await self.session.refresh(object)
    async def delete_object(self, object:T)->None:
        await self.session.delete(object)
        await self.session.commit()