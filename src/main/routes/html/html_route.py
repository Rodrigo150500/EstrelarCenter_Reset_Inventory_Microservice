from flask import Blueprint, jsonify, render_template

html_route_bp = Blueprint("html_route_bp", __name__)

@html_route_bp.route("/reset", methods=["GET", "POST"])
def show_reset_page():
    return render_template("/index.html")