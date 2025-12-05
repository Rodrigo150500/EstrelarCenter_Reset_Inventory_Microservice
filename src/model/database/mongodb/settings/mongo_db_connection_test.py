from dotenv import load_dotenv
load_dotenv(".env")

from src.model.database.mongodb.repositories.product_repository import ProductRepository

from .mongo_db_connection import mongo_db_connection

def test_connection():

    mongo_db_connection.connect()

    connection = mongo_db_connection.get_db_connection()

    repository = ProductRepository(connection)
    
    response = repository.get_all_products()    

    assert response is not None