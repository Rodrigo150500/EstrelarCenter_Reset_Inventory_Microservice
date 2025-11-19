from firebase_admin import db
from dotenv import dotenv_values

ENV = dotenv_values("dev.env")
COLLECTION = ENV["COLLECTION_NAME_FIREBASE_PRODUCTS"]

class ProductRepository:

    def __init__(self, db_reference: db):
        
        self.__db_reference = db_reference.reference(f"/{COLLECTION}")
    
    
    def get_all_products(self) -> dict:

        products = self.__db_reference.get()

        return products


    def update_product_by_code_to_zero(self, code: str):

        self.__db_reference.child(code).update({
            "Quantidade": "0"
        })