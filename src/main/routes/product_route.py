from flask import Blueprint, jsonify
from src.main.compose.product_reset_amount_compose import product_reset_amount_compose
from src.errors.error_handler import error_handler

product_route_bp = Blueprint("product_route_bp", __name__)

@product_route_bp.route("/products", methods=["POST", "GET"])
def reset_product_amount():

    try:

        use_case = product_reset_amount_compose()
        
        response = use_case.handle()

        return jsonify(response.body), response.status_code

    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code