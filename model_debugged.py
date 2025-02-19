import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.multioutput import MultiOutputClassifier

# Load dataset
df = pd.read_csv("vehicle_sensor_data_multilabel_edit.csv")

# Define features and multilabel outputs
features = ["RPM", "Coolant Temperature (°C)", "Vehicle Speed (km/h)", "Intake Air Mass (g/s)"]
label_columns = ["High RPM", "High Coolant Temperature", "Low Speed", "High Intake Air Mass",
                 "Low Intake Air Mass", "Thermostat Issue", "Airflow Restriction"]

# Ensure all required columns exist
missing_cols = [col for col in label_columns if col not in df.columns]
if missing_cols:
    raise KeyError(f"Missing columns in dataset: {missing_cols}")

# Extract feature matrix and labels
X = df[features]
y = df[label_columns].astype(int)  # Convert labels to integers

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert labels to numpy array
y_encoded = np.array(y.values, dtype=int)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Train a multilabel RandomForest model using MultiOutputClassifier
base_model = RandomForestClassifier(n_estimators=200, random_state=42)
model = MultiOutputClassifier(base_model)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluation
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=label_columns, zero_division=1))

# Save model and scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("\n✅ Model and scaler saved successfully!")
