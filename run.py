import os
from src.main.server.server import app

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
print(os.getenv("COLLECTION_NAME_MONGO_DB_PRODUCTS"))
if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)