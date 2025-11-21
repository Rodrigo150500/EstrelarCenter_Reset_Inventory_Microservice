import os
from firebase_admin import db
from .interface.product_repository_interface import IProductRepository

COLLECTION = os.getenv("COLLECTION_NAME_FIREBASE_PRODUCTS")

class ProductRepository(IProductRepository):

    def __init__(self, db_reference: db):
        
        self.__db_reference = db_reference.reference(f"/{COLLECTION}")
    
    
    def get_all_products(self) -> dict:

        products = self.__db_reference.get()

        return products


    def update_product_by_code_to_zero(self, code: str):

        self.__db_reference.child(code).update({
            "Quantidade": "0"
        })