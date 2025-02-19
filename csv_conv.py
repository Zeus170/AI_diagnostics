import pandas as pd

# Load dataset
df = pd.read_csv("vehicle_sensor_data_balanced.csv")

# Define failure types
failure_types = ["High RPM", "High Coolant Temperature", "Low Speed", "High Intake Air Mass",
                 "Low Intake Air Mass", "Thermostat Issue", "Airflow Restriction"]

# Convert "Failure Type" to multilabel format
for failure in failure_types:
    df[failure] = df["Failure Type"].apply(lambda x: 1 if failure in x else 0)

# Drop old column
df.drop(columns=["Failure Type"], inplace=True)

# Save new dataset
df.to_csv("vehicle_sensor_data_multilabel.csv", index=False)

print("✅ Dataset converted to multilabel format!")
