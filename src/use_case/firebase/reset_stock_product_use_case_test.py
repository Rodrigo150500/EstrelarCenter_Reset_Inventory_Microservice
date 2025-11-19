import pytest
from unittest.mock import Mock, call
from .reset_stock_product_use_case import ResetStockProductUseCase
from src.main.http_types.http_response.http_response import HttpResponse
from .data.reset_stock_product_use_case_data import reset_stock_product_use_case_data

@pytest.fixture
def setup_use_case():

    repository = Mock()

    use_case = ResetStockProductUseCase(repository)

    data = {
        "repository": repository,
        "use_case": use_case
    }

    return data


def test_update_stock_sucessfully(setup_use_case):

    data = reset_stock_product_use_case_data()

    repository = setup_use_case["repository"]

    repository.get_all_products.return_value = data["get_all_products"]

    call_list = [call("1"), call("2"), call("3")]

    use_case = setup_use_case["use_case"]

    response = use_case.handle()

    assert isinstance(response, HttpResponse)
    assert response.body == data["expected_body"]
    assert response.status_code == 200
    
    repository.update_product_by_code_to_zero.assert_has_calls(call_list)

    

