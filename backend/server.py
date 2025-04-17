from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Allow all origins (you can restrict later)

@app.route("/listings", methods=["GET"])
def get_listings():
    file_path = "/app/frontend/kijiji-listings/public/listings.json"

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    with open(file_path, "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)