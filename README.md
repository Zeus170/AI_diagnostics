# AI_diagnostics
AI predictive maintenance for vehicles through OBD2 data. 
OBD2 data is acquired through ELM327 module that is interfaced to an ESP32 board via bluetooth. OBD2 parameters are retrieved using AT commands sent to the ELM327 from ESP32. An optimized ML model runs on the ESP32 and through the use of the h/w accelerator available on the ESP32, it predicts DTCs or errors in the vehicle before it is encountered by the ECUs. 
Parameters like RPM, coolant temparature, fuel consumption, throttle position, vehicle speed, boost pressure, air intake volume, timing advance, lambda sensors, NOx, O2 etc are read using the ELM327 connected to the OBD2 port of the vehicle. 
ML model is trained to detect anomalies in these parameters and predict failures before their onset. 
Live data and other visualizations are enabled through a web dashboard that is hosted from the ESP32 and can be accessed by connecting to the WiFi access point of the ESP32. 
