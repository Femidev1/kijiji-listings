from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)

# ✅ Enable CORS for /listings route (both domain variants)
CORS(app, resources={
    r"/listings": {
        "origins": [
            "https://femithedesigner.com",
            "https://www.femithedesigner.com"
        ]
    }
})

@app.route("/listings", methods=["GET"])
def get_listings():
    # ✅ Use absolute path to JSON file
    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../frontend/kijiji-listings/public/listings.json")
    )

    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": "Failed to load listings", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)