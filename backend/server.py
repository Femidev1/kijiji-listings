from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/listings", methods=["GET"])
def get_listings():
    with open("frontend/kijiji-listings/public/listings.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)