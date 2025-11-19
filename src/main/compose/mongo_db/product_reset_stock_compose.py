from src.model.database.mongodb.settings.mongo_db_connection import mongo_db_connection
from src.model.database.mongodb.repositories.product_repository import ProductRepository
from src.use_case.mongo_db.reset_stock_product_use_case import ResetStockProductUseCase

def product_reset_stock_compose():
    
    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepository(connection)
    use_case = ResetStockProductUseCase(repository)

    return use_case