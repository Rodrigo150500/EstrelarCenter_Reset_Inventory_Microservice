from src.model.database.mongodb.repositories.types.update_one_interface import IUpdateOne
from dotenv import dotenv_values
from bson.objectid import ObjectId

ENV = dotenv_values("dev.env")

COLLECTION_NAME = ENV["COLLECTION_NAME_MONGO_DB_PRODUCTS"]

class ProductRepository:

    def __init__(self, connection):
        self.__collection = connection.get_collection(COLLECTION_NAME)
    

    def get_all_products(self) -> list:

        response = self.__collection.find()        

        return response
    
    
    def get_product_by_object_id(self, object_id: ObjectId) -> dict:

        response = self.__collection.find_one({"_id":object_id})

        return response   


    def update_product_by_code_to_zero(self, code: str, item: str) -> IUpdateOne:

        response = self.__collection.update_one(
            {code: {"$exists": True}},
            {"$set": {f"{code}.{item}.stock": 0}})
        
        return response
