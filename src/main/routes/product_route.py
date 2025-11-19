from flask import Blueprint, jsonify
from src.main.compose.mongo_db.product_reset_stock_compose import product_reset_stock_mongo_db_compose
from src.main.compose.firebase.product_reset_stock_compose import product_reset_stock_firebase_compose
from src.errors.error_handler import error_handler

product_route_bp = Blueprint("product_route_bp", __name__)

@product_route_bp.route("/products", methods=["POST", "GET"])
def reset_product_stock():

    try:

        use_case_mongo_db = product_reset_stock_mongo_db_compose()
        use_case_firebase = product_reset_stock_firebase_compose()

        response_mongo_db = use_case_mongo_db.handle()
        response_firebase = use_case_firebase.handle()

        body = {
            "mongo_db": response_mongo_db.body,
            "firebase": response_firebase.body
        }

        return jsonify(body), response_mongo_db.status_code

    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code