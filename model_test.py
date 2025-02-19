import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load("vehicle_anomaly_model.pkl")
scaler = joblib.load("scaler.pkl")
mlb = joblib.load("mlb.pkl")

# Define test cases (RPM, Coolant Temp, Speed, Intake Air Mass)
test_cases = np.array([
    [2000, 90, 60, 12],   # Should detect no anomaly
    [4000, 110, 30, 8],   # High RPM, High Coolant Temp
    [1000, 95, 10, 5],    # Low Speed, Low Intake Air Mass
    [5000, 85, 80, 25]    # High RPM
])

# Scale test cases
test_cases_scaled = scaler.transform(test_cases)

# Get model predictions
pred_binary = model.predict(test_cases_scaled)  # Multi-label output

# Convert binary predictions back to labels
predicted_anomalies = mlb.inverse_transform(pred_binary)

# Print results
for i, anomalies in enumerate(predicted_anomalies):
    print(f"\n🔹 Test Case {i+1}: RPM={test_cases[i,0]}, Coolant Temp={test_cases[i,1]}°C, Speed={test_cases[i,2]} km/h, Intake Air Mass={test_cases[i,3]} g/s")
    if anomalies:
        print(f"⚠️ Detected Anomalies: {', '.join(anomalies)}")
    else:
        print("✅ No anomalies detected.")
