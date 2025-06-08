from flask import Flask, jsonify, request
import os
from connection import collections

app = Flask(__name__)

PORT = os.environ.get("PORT", 8000)

@app.route("/")
def index():
    return jsonify({
        "message": "Backend is running!",
    })

@app.route("/api/get")
def get():
    names = collections.find({}, {"_id": 0, "id": 0})

    names_list = [name["name"] for name in names]

    return jsonify({
        "data": names_list,
    })

@app.route("/api/add", methods=["POST"])
def add():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    name = data["name"]
    if not name:
        return jsonify({"error": "Name cannot be empty"}), 400
    
    new_entry = {"name": name}
    collections.insert_one(new_entry)
    new_entry["_id"] = str(new_entry["_id"])

    return jsonify({
        "message": "Name added successfully",
        "data": new_entry
        }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)