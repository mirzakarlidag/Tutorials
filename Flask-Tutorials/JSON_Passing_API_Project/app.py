from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)


@app.route("/upload_csv", methods=["GET"])
def upload_csv():
    df = pd.read_csv("sample_data.csv")  # Read the CSV file into a pandas DataFrame

    # Perform any necessary processing on the DataFrame

    # Convert the DataFrame to JSON
    json_data = df.to_json(orient="records")

    # Return the DataFrame as JSON
    return jsonify(json_data)


if __name__ == "__main__":
    app.run(debug=True)
