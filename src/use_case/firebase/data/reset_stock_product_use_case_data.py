def reset_stock_product_use_case_data():

    get_all_products = {
        "1":{
            "Descrição": "Produto A",
            "Quantidade": 20
        },"2":{
            "Descrição": "Produto B",
            "Quantidade": 50
        }, "3":{
            "Descrição": "Produto C",
            "Quantidade": 80
        }
    }

    expected_body = {
        "data":{
            "operation": "update",
            "count": 3
        }
    }

    data = {
        "get_all_products": get_all_products,
        "expected_body": expected_body
    }

    return data