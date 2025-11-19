from src.model.database.mongodb.settings.mongo_db_connection import mongo_db_connection
from src.model.database.mongodb.repositories.product_repository import ProductRepository
from src.use_case.reset_amount_product import ResetAmountProduct

def product_reset_amount_compose():
    
    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepository(connection)
    use_case = ResetAmountProduct(repository)

    return use_case