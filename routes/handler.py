from flask import Blueprint, jsonify, send_from_directory, request
from .functions import (
    auth,
    youtube
)

app = Blueprint("web", __name__)

# Root route returns JSON
@app.route("/")
def index():
    return jsonify(status="ok")


# Auth API route
@app.route("/api/auth", methods=["POST"])
async def authorization():
    return await auth.handle() 

@app.route("/api/search", methods=["POST"])
async def browse():
    return await youtube.handle()     
    



