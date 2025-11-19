from src.main.server.server import app
from dotenv import dotenv_values

ENV = dotenv_values("dev.env")
HOST = ENV["HOST"]
PORT = ENV["PORT"]

if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)