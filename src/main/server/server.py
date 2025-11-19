from flask import Flask
from flask_cors import CORS
from src.model.database.mongodb.settings.mongo_db_connection import mongo_db_connection

from src.main.routes.mongo_db.product_route import product_route_bp

mongo_db_connection.connect()

app = Flask(__name__)
CORS(app)

app.register_blueprint(product_route_bp)
