from abc import ABC, abstractmethod
from bson.objectid import ObjectId
from src.model.database.mongodb.repositories.types.update_one_interface import IUpdateOne


class IProductRepository(ABC):

    @abstractmethod
    def get_all_object_id(self) -> list:
        pass
    

    @abstractmethod
    def get_product_by_object_id(self, object_id: ObjectId) -> dict:
        pass

    
    @abstractmethod
    def update_product_by_code_to_zero(self, code: str, item: str) -> IUpdateOne:
        pass
        
