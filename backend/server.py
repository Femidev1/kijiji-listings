from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)

# Enable CORS for your frontend domain
CORS(app, resources={r"/listings": {"origins": "https://femithedesigner.com"}})

@app.route("/listings", methods=["GET"])
def get_listings():
    file_path = os.path.join(os.path.dirname(__file__), "../frontend/kijiji-listings/public/listings.json")
    with open(file_path, "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)