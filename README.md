# AI_diagnostics
AI predictive maintenance for vehicles through OBD2 data. 
OBD2 data is acquired through ELM327 module that is interfaced to an ESP32 board via bluetooth. OBD2 parameters are retrieved using AT commands sent to the ELM327 from ESP32. An optimized ML model runs on the ESP32 and through the use of the h/w accelerator available on the ESP32, it predicts DTCs or errors in the vehicle before it is encountered by the ECUs. 
Parameters like RPM, coolant temparature, fuel consumption, throttle position, vehicle speed, boost pressure, air intake volume, timing advance, lambda sensors, NOx, O2 etc are read using the ELM327 connected to the OBD2 port of the vehicle. 
ML model is trained to detect anomalies in these parameters and predict failures before their onset. 
Live data and other visualizations are enabled through a web dashboard that is hosted from the ESP32 and can be accessed by connecting to the WiFi access point of the ESP32. 


1. Coolant Temperature + RPM
High Coolant Temperature with High RPM:
Overheating due to High Load: This could indicate that the engine is under heavy load or the cooling system is not functioning properly (e.g., a failing thermostat, low coolant level, or radiator blockage). The higher RPM could exacerbate the overheating issue.
Coolant Circulation Problems: A failing water pump might not circulate coolant efficiently, causing overheating, especially at higher RPM.
High Coolant Temperature with Low RPM:
Engine Idling Overheating: This can indicate a problem with the radiator fan or a clogged cooling system. Even at low RPM, the engine could overheat if the fan isn't running or coolant flow is obstructed.
2. Vehicle Speed + Coolant Temperature
High Coolant Temperature with Low Speed:
Cooling Efficiency Problems at Low Speeds: The cooling system relies heavily on airflow through the radiator. Low speeds (such as in city traffic) may not provide enough airflow, causing the engine to overheat.
Thermostat Issues: If the thermostat gets stuck closed, coolant can't circulate properly, causing overheating even when the vehicle isn't moving fast.
High Coolant Temperature with High Speed:
Radiator or Coolant Flow Issue: If the coolant temperature remains high even at high speeds, this could point to a faulty radiator, coolant blockage, or insufficient coolant levels.
3. Intake Air Mass + RPM
Low Intake Air Mass with High RPM:
Air Intake Restriction: This could indicate a clogged air filter, throttle body issue, or intake system obstruction, as the engine demands more air at higher RPM, but intake air is restricted.
Mass Air Flow (MAF) Sensor Issue: A malfunctioning MAF sensor could lead to improper air-to-fuel ratios, especially under higher RPM.
High Intake Air Mass with High RPM:
Air-Fuel Mixture Imbalance: If too much air is entering the engine (potentially due to a vacuum leak or malfunctioning sensor), it can cause a lean air-fuel mixture, leading to poor engine performance and potential damage.
4. Coolant Temperature + Intake Air Mass
High Coolant Temperature + Low Intake Air Mass:
Poor Engine Cooling Under Load: When the engine is hot and the intake air mass is low, it could indicate that the engine is working harder than it should, potentially due to air filter clogging, fuel delivery issues, or a cooling system that isn't keeping up.
Turbocharged Engines: In turbocharged engines, a drop in intake air mass with high coolant temperature could suggest issues with the turbocharger or intercooler (e.g., turbo failure, intercooler leaks).
Normal Coolant Temperature + High Intake Air Mass:
Possible Air-Fuel Mixture Issue: High intake air mass could cause the engine to run lean if the fuel injectors or fuel delivery system cannot supply enough fuel for the extra air, leading to poor performance or engine knock.
5. All Parameters Combined
High Coolant Temperature, High RPM, Low Intake Air Mass, and Low Vehicle Speed:
Severe Engine Overload/Overheating: This could indicate that the engine is under high stress (perhaps due to driving conditions like stop-and-go traffic), combined with a lack of sufficient airflow for cooling or air intake, leading to overheating and potential engine damage.
Normal Coolant Temperature, High RPM, Low Intake Air Mass:
Air Intake Restriction or Sensor Issue: The engine is running at high RPM but is not getting enough air, possibly due to a clogged air filter, malfunctioning sensors, or a faulty intake system.
Low Coolant Temperature with Low RPM and Low Vehicle Speed:
Thermostat or Engine Warm-Up Issue: The engine is not warming up properly, possibly due to a stuck open thermostat. This can lead to poor fuel economy and inefficient engine performance, especially at low speeds.


High precision across most labels → The model is making accurate predictions when it does classify something.
Lower recall for certain labels (e.g., Low Speed, Low Intake Air Mass, Airflow Restriction) → The model is missing some positive cases.
samples avg is very high (0.93 F1-score) → The model is good at making correct predictions across multiple labels per sample.