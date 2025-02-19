import pandas as pd
import numpy as np

# Set number of samples
num_normal = 700  # 70% normal cases
num_failure = 300  # 30% failure cases
num_samples = num_normal + num_failure

# Function to generate normal sensor values
def generate_normal_values():
    rpm = np.random.randint(800, 3500)  # Normal RPM range
    coolant_temp = np.random.uniform(70, 90)  # Normal temperature range
    speed = np.random.randint(20, 120)  # Normal speed range
    intake_air_mass = np.random.uniform(2.5, 9)  # Normal intake air mass
    
    return rpm, coolant_temp, speed, intake_air_mass

# Function to generate failure sensor values
def generate_failure_values():
    failure_type = np.random.choice([
        "High Coolant Temperature", "Low Intake Air Mass", "High RPM", 
        "High Intake Air Mass", "Low Speed", "Thermostat Issue", "Airflow Restriction"
    ])
    
    rpm, coolant_temp, speed, intake_air_mass = generate_normal_values()
    
    if failure_type == "High Coolant Temperature":
        coolant_temp = np.random.uniform(95, 120)  # Overheating
    
    elif failure_type == "Low Intake Air Mass":
        intake_air_mass = np.random.uniform(0.5, 1.8)  # Airflow restriction
    
    elif failure_type == "High RPM":
        rpm = np.random.randint(4000, 7000)  # Over-revving
    
    elif failure_type == "High Intake Air Mass":
        intake_air_mass = np.random.uniform(10, 20)  # Over-fueling
    
    elif failure_type == "Low Speed":
        speed = np.random.randint(0, 10)  # Stalling issue
    
    elif failure_type == "Thermostat Issue":
        coolant_temp = np.random.uniform(60, 70)  # Stuck open thermostat
    
    elif failure_type == "Airflow Restriction":
        intake_air_mass = np.random.uniform(1, 2)  # Partial intake blockage
    
    return rpm, coolant_temp, speed, intake_air_mass, failure_type

# Create dataset
data = []
labels = []

for _ in range(num_normal):
    rpm, coolant_temp, speed, intake_air_mass = generate_normal_values()
    data.append([rpm, coolant_temp, speed, intake_air_mass])
    labels.append("Normal")

for _ in range(num_failure):
    rpm, coolant_temp, speed, intake_air_mass, failure_type = generate_failure_values()
    data.append([rpm, coolant_temp, speed, intake_air_mass])
    labels.append(failure_type)

# Convert to DataFrame
df = pd.DataFrame(data, columns=["RPM", "Coolant Temperature (°C)", "Vehicle Speed (km/h)", "Intake Air Mass (g/s)"])
df["Failure Type"] = labels

# Save dataset
df.to_csv("vehicle_sensor_data_balanced.csv", index=False)

print("Dataset generated and saved as vehicle_sensor_data_balanced.csv")
