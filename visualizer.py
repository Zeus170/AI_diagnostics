import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("vehicle_sensor_data_balanced.csv")

# Set Seaborn style
sns.set(style="whitegrid")

# 🔹 1. Histograms of each sensor parameter
df.hist(figsize=(10, 6), bins=30, edgecolor="black")
plt.suptitle("Sensor Value Distributions", fontsize=14)
plt.show()

# 🔹 2. Scatter plots to analyze correlation

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x="RPM", y="Intake Air Mass (g/s)", hue="Failure Type", alpha=0.7)
plt.title("RPM vs Intake Air Mass")
plt.xlabel("RPM")
plt.ylabel("Intake Air Mass (g/s)")

plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x="Vehicle Speed (km/h)", y="Coolant Temperature (°C)", hue="Failure Type", alpha=0.7)
plt.title("Speed vs Coolant Temperature")
plt.xlabel("Vehicle Speed (km/h)")
plt.ylabel("Coolant Temperature (°C)")

plt.tight_layout()
plt.show()

# 🔹 3. Pairplot to see feature interactions
sns.pairplot(df, hue="Failure Type", diag_kind="kde", corner=True)
plt.suptitle("Pairplot of Vehicle Sensor Data", fontsize=14)
plt.show()
