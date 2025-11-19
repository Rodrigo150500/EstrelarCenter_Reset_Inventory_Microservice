from src.model.database.firebase.settings.firebase_db_connection import firebase_db_connection
from src.model.database.firebase.repositories.product_repository import ProductRepository
from src.use_case.firebase.reset_stock_product_use_case import ResetStockProductUseCase


def product_reset_stock_compose():

    connection = firebase_db_connection.get_connection()
    repository = ProductRepository(connection)
    use_case = ResetStockProductUseCase(repository)

    return use_case