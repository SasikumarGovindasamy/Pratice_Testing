# app.py
from flask import Flask, jsonify, request
import database

app = Flask(__name__)

@app.route("/activities", methods=["GET"])
def get_activities():
    return jsonify(database.get_all()), 200

@app.route("/activities/<int:activity_id>", methods=["GET"])
def get_activity(activity_id):
    activity = database.get_by_id(activity_id)
    if activity:
        return jsonify(activity), 200
    return jsonify({"error": "Not found"}), 404

@app.route("/activities", methods=["POST"])
def create_activity():
    data = request.json
    new_activity = {
        "id": data["id"],
        "title": data["title"],
        "completed": data.get("completed", False)
    }
    database.add(new_activity)
    return jsonify(new_activity), 201

@app.route("/activities/<int:activity_id>", methods=["PUT"])
def update_activity(activity_id):
    data = request.json
    updated = database.update(activity_id, data)
    if updated:
        return jsonify(updated), 200
    return jsonify({"error": "Not found"}), 404

@app.route("/activities/<int:activity_id>", methods=["DELETE"])
def delete_activity(activity_id):
    database.delete(activity_id)
    return jsonify({"deleted": True}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
