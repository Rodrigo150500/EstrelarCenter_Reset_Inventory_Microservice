from flask import Blueprint, jsonify
from src.main.compose.mongo_db.product_reset_stock_compose import product_reset_stock_compose
from src.errors.error_handler import error_handler

product_route_mongo_db_bp = Blueprint("product_route_mongo_db_bp", __name__)

@product_route_mongo_db_bp.route("/mongo/products", methods=["POST", "GET"])
def reset_product_stock():

    try:

        use_case = product_reset_stock_compose()
        
        response = use_case.handle()

        return jsonify(response.body), response.status_code

    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code