import pytest
from .product_repository import ProductRepository
from src.model.database.firebase.settings.firebase_db_connection import firebase_db_connection


@pytest.fixture
def setup_repository():

    firebase_db_connection.connect()

    connection = firebase_db_connection.get_connection() 

    repository = ProductRepository(connection)

    return repository


@pytest.mark.skip()
def test_get_all_products_sucessfully(setup_repository):

    repo = setup_repository

    repo.get_all_products()
    

@pytest.mark.skip()
def test_update_product_sucessfully(setup_repository):

    repo = setup_repository

    repo.update_product_by_code_to_zero("14")