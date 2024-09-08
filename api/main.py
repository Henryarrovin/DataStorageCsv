from flask import Flask, request, jsonify
import csv
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

CSV_FILE_PATH = "data.csv"


@app.route("/store-data", methods=["POST"])
def store_data():
    data = request.json

    if not data:
        return jsonify({"error": "No data provided"}), 400

    file_exists = os.path.isfile(CSV_FILE_PATH)

    with open(CSV_FILE_PATH, mode="a", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)

    return jsonify({"message": "Data stored successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
