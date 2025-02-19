from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Load trained model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Define label columns (for interpreting predictions)
label_columns = [
    "High RPM", "High Coolant Temperature", "Low Speed", 
    "High Intake Air Mass", "Low Intake Air Mass", "Thermostat Issue", "Airflow Restriction"
]

# Feature columns (ensure order matches training data)
feature_columns = ["RPM", "Coolant Temperature (°C)", "Vehicle Speed (km/h)", "Intake Air Mass (g/s)"]

@app.route("/predict", methods=["POST", "GET"])
def predict():
    try:
        if request.method == "GET":
            return jsonify({"message": "Use a POST request with JSON data."}), 400
        data = request.json

        # Convert input to DataFrame
        test_case = pd.DataFrame([[data["rpm"], data["coolant_temp"], data["speed"], data["intake_air_mass"]]], columns=feature_columns)
        
        # Scale the input data
        test_case_scaled = scaler.transform(test_case)

        # Make predictions
        pred_binary = model.predict(test_case_scaled)

        # Convert binary predictions to human-readable labels
        detected_anomalies = [label_columns[j] for j in range(len(label_columns)) if pred_binary[0][j] == 1]

        # Return results
        return jsonify({"anomalies": detected_anomalies})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
