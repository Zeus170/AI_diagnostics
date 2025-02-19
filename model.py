import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("vehicle_sensor_data_balanced.csv")

# Define features and labels
features = ["RPM", "Coolant Temperature (°C)", "Vehicle Speed (km/h)", "Intake Air Mass (g/s)"]
label_columns = ["High RPM", "High Coolant Temperature", "Low Speed", "High Intake Air Mass",
                 "Low Intake Air Mass", "Thermostat Issue", "Airflow Restriction"]

X = df[features]
y = df[label_columns]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert multi-labels to binary encoding
mlb = MultiLabelBinarizer()
y_encoded = np.array(y.values)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluation
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save model and scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(mlb, "mlb.pkl")

print("\nModel and scaler saved!")
