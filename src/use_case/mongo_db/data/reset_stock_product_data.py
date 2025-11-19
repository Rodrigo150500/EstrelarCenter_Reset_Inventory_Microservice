from bson.objectid import ObjectId

def reset_stock_product_data():

    get_all_products = [
    {
        "_id": ObjectId("68b70ef826423e500863c1c6"),
        "1":[{
            "description":"Product A",
            "stock": 20
        },{
            "description": "Product A.1",
            "stock": 80
        }]
    },{
        "_id": ObjectId("68b70ef826423e500863c1c6"),
        "2":[{
            "description": "Product B",
            "stock": 50
        },{
            "description": "Product B.1",
            "stock": 150
        },{
            "description": "Product B.2",
            "stock": 120
        }]
    },{
        "_id": ObjectId("68b70ef826423e500863c1c6"),
        "3":[{
            "description": "Product C",
            "stock": 15
        },{
            "description": "Product C.1",
            "stock": 50
        },{
            "description": "Product C.2",
            "stock": 55
        }]
    }]

    expected_body = {
        "data":{
            "operation":"update",
            "count":3
        }
    }  

    data = {
        "get_all_products": get_all_products,
        "expected_body": expected_body
    }

    return data