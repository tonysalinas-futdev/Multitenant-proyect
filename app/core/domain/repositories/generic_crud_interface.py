from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import List
T=TypeVar("T")

class GenericCRUDInterface(ABC, Generic[T]):
    @abstractmethod
    def commit_(self)->None:
        pass

    @abstractmethod
    def save(self, object:T)->None:
        pass

    @abstractmethod
    def get_by_id(self, object_id:int)->T:
        pass

    @abstractmethod
    def get_all_objects(self)->List[T]:
        pass

    @abstractmethod
    def delete_object(self, object:T)->None:
        pass

    @abstractmethod
    def update(self, object:T, new_object:BaseModel)->T:
        pass
    
    @abstractmethod
    def rollback_(self)->None:
        pass