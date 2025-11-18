import pytest
from src.model.database.mongodb.settings.mongo_db_connection import mongo_db_connection
from .product_repository import ProductRepository
from bson.objectid import ObjectId

@pytest.fixture
def setup_repo():

    mongo_db_connection.connect()
    connection = mongo_db_connection.get_db_connection()
    repo = ProductRepository(connection)

    return repo

@pytest.mark.skip()
def test_get_all_products(setup_repo):

    repo = setup_repo

    documents = repo.get_all_object_id()

    objetct_id_list = []

    for document in documents:
        objetct_id_list.append(document['_id'])    

    assert isinstance(objetct_id_list[0], ObjectId)


@pytest.mark.skip()
def test_get_product_by_object_id(setup_repo):

    repo = setup_repo

    product = repo.get_product_by_object_id(ObjectId("68b70ef826423e500863c1c6"))

    del product["_id"]

    product_key = list(product.keys())[0]

    assert product_key == "16"

@pytest.mark.skip()
def test_update_product_by_code(setup_repo):

    repo = setup_repo

    response = repo.update_product_by_code_to_zero("16", 0)
    
    print(response)