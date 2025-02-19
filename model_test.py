import joblib
import numpy as np
import pandas as pd

# Load the trained model and scaler
model = joblib.load("model.pkl")  
scaler = joblib.load("scaler.pkl")

# Define label columns (used for interpretation of predictions)
label_columns = [
    "High RPM", "High Coolant Temperature", "Low Speed", 
    "High Intake Air Mass", "Low Intake Air Mass", "Thermostat Issue", "Airflow Restriction"
]

# Define feature names for scaling
feature_columns = ["RPM", "Coolant Temperature (°C)", "Vehicle Speed (km/h)", "Intake Air Mass (g/s)"]

# Define test cases
test_cases = np.array([
    [2000, 90, 60, 12],   # Should detect no anomaly
    [4000, 110, 30, 8],   # High RPM, High Coolant Temp
    [1000, 95, 10, 5],    # Low Speed, Low Intake Air Mass
    [8000, 85, 80, 2]    # High RPM
])

# Convert to DataFrame with correct column names
test_cases_df = pd.DataFrame(test_cases, columns=feature_columns)

# Scale test cases
test_cases_scaled = scaler.transform(test_cases_df)

# Get model predictions
pred_binary = model.predict(test_cases_scaled)  

# Convert binary predictions (0 or 1) into readable labels
for i, pred in enumerate(pred_binary):
    detected_anomalies = [label_columns[j] for j in range(len(label_columns)) if pred[j] == 1]
    
    print(f"\n🔹 Test Case {i+1}: RPM={test_cases[i,0]}, Coolant Temp={test_cases[i,1]}°C, Speed={test_cases[i,2]} km/h, Intake Air Mass={test_cases[i,3]} g/s")
    
    if detected_anomalies:
        print(f"⚠️ Detected Anomalies: {', '.join(detected_anomalies)}")
    else:
        print("✅ No anomalies detected.")
