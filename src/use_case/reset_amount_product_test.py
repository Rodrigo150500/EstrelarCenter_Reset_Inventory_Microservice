import pytest
from unittest.mock import Mock, call
from .reset_amount_product import ResetAmountProduct
from .data.reset_amount_product_data import reset_amount_product_data
from src.main.http_types.http_response.http_response import HttpResponse

@pytest.fixture
def setup_use_case():

    repository = Mock()

    use_case = ResetAmountProduct(repository)

    data = {
        "repository": repository,
        "use_case": use_case
    }

    return data


def test_reset_amount_sucessfully(setup_use_case):

    data = reset_amount_product_data()

    repository = setup_use_case["repository"]

    repository.get_all_products.return_value = data["get_all_products"]

    use_case = setup_use_case["use_case"]

    response = use_case.handle()

    call_list = [call("1", "0"), call("1", "1"), call("2", "0"), call("2", "1"), call("2", "2"), call("3", "0"), call("3", "1"), call("3", "2") ]

    assert isinstance(response, HttpResponse)
    assert response.body == data["expected_body"]
    assert response.status_code == 200

    repository.get_all_products.assert_called_once()

    repository.update_product_by_code_to_zero.assert_has_calls(call_list)
    



