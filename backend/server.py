from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Allow all origins for now

@app.route("/listings", methods=["GET"])
def get_listings():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend/kijiji-listings/public/listings.json"))
    with open(file_path, "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # ✅ Use Railway-provided port
    app.run(host="0.0.0.0", port=port)