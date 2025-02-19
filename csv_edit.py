import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("vehicle_sensor_data_multilabel.csv")  # Ensure this is your one-hot encoded dataset

# Extract features and labels
feature_columns = ["RPM", "Coolant Temperature (°C)", "Vehicle Speed (km/h)", "Intake Air Mass (g/s)"]
label_columns = ["High RPM", "High Coolant Temperature", "Low Speed", "High Intake Air Mass",
                 "Low Intake Air Mass", "Thermostat Issue", "Airflow Restriction"]

normal_samples = df[df[label_columns].sum(axis=1) == 0]  # Normal entries
faulty_samples = df[df[label_columns].sum(axis=1) == 1]  # Single fault entries

merged_samples = []

# Merge samples by selecting random faulty entries
for _ in range(len(faulty_samples) // 2):  # Merge roughly half the dataset
    sampled_rows = faulty_samples.sample(n=2, replace=False)  # Pick 2 random faulty entries
    
    merged_features = sampled_rows[feature_columns].mean().values  # Average the sensor values
    merged_labels = sampled_rows[label_columns].max().values  # Logical OR for labels

    merged_samples.append(np.concatenate([merged_features, merged_labels]))

# Convert merged samples into DataFrame
merged_df = pd.DataFrame(merged_samples, columns=feature_columns + label_columns)

# Combine normal, original faulty, and merged faulty samples
final_dataset = pd.concat([normal_samples, faulty_samples, merged_df], ignore_index=True)

# Save the new dataset
final_dataset.to_csv("vehicle_sensor_data_multilabel_edit.csv", index=False)

print("✅ Multilabel dataset created and saved!")
