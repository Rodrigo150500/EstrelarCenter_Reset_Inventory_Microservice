from dotenv import load_dotenv
load_dotenv(".env")

from flask import Flask
from flask_cors import CORS
from src.model.database.mongodb.settings.mongo_db_connection import mongo_db_connection
from src.model.database.firebase.settings.firebase_db_connection import firebase_db_connection

from src.main.routes.mongo_db.product_route import product_route_mongo_db_bp
from src.main.routes.firebase.product_route import product_route_firebase_bp
from src.main.routes.html.html_route import html_route_bp


mongo_db_connection.connect()
firebase_db_connection.connect()

app = Flask(__name__)
CORS(app)

app.register_blueprint(product_route_mongo_db_bp)
app.register_blueprint(product_route_firebase_bp)
app.register_blueprint(html_route_bp)