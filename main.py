from flask import Flask
from waitress import serve
from flask_cors import CORS
from routes.handler import app
import os

def create_app():
    flaskapp = Flask(
        __name__,
        template_folder="templates"
    )

    #Enable CORS
    CORS(flaskapp)

    flaskapp.register_blueprint(app)
    return flaskapp


flaskapp = create_app()

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = int(os.getenv("PORT", 5000))
    print(f"Server running on http://{HOST}:{PORT}")

    serve(flaskapp, host=HOST, port=PORT)