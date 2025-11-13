from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import List
T=TypeVar("T")

class GenericCRUDInterface(ABC, Generic[T]):
    @abstractmethod
    async def save(self, object:T)->None:
        pass

    @abstractmethod
    async def get_by_id(self, object_id:int)->T:
        pass

    @abstractmethod
    async def get_all_objects(self)->List[T]:
        pass

    @abstractmethod
    async def delete_object(self, object:T)->None:
        pass

    @abstractmethod
    async def update(self, object:T, new_object:BaseModel)->None:
        pass

