const ESP32_URL = "http://127.0.0.1:5000/predict"; // Change to your ESP32's IP

function updateValue(id) {
    document.getElementById(id + "Value").innerText = document.getElementById(id).value;
}

function sendData() {
    let rpm = parseInt(document.getElementById("rpm").value);
    let coolant = parseInt(document.getElementById("coolant").value);
    let speed = parseInt(document.getElementById("speed").value);
    let intake = parseInt(document.getElementById("intake").value);

    let data = {
        "rpm": rpm,
        "coolant_temp": coolant,
        "speed": speed,
        "intake_air_mass": intake
    };

    fetch(ESP32_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        let resultElement = document.getElementById("result");
        let diagnosisElement = document.getElementById("diagnosis");

        if (data.anomalies.length > 0) {
            resultElement.innerHTML = `⚠️ Anomalies Detected: ${data.anomalies.join(", ")}`;
            resultElement.style.color = "red";

            let diagnosis = getDiagnosis(data.anomalies);
            diagnosisElement.innerHTML = diagnosis;
            diagnosisElement.style.color = diagnosis.includes("⚠️") ? "red" : "orange";
        } else {
            resultElement.innerHTML = "✅ No anomalies detected.";
            resultElement.style.color = "green";
            diagnosisElement.innerHTML = "Vehicle operating normally.";
            diagnosisElement.style.color = "green";
        }

        resultElement.classList.remove("hidden");
        diagnosisElement.classList.remove("hidden");
    })
    .catch(error => console.error("Error:", error));
}

// Diagnosis logic based on ML-detected anomalies
function getDiagnosis(anomalies) {
    let issues = [];

    if (anomalies.includes("High RPM")) {
        issues.push("⚠️ High RPM detected. Possible causes: Aggressive driving, throttle body issue, transmission problem.");
    }
    
    if (anomalies.includes("High Coolant Temperature")) {
        issues.push("🔥 Engine overheating. Possible causes: Low coolant, radiator blockage, thermostat failure.");
    }
    
    if (anomalies.includes("Low Speed")) {
        issues.push("🚗 Low speed detected. May indicate idling or stop-and-go traffic conditions.");
    }
    
    if (anomalies.includes("High Intake Air Mass")) {
        issues.push("🌬️ High air intake. Possible causes: Boost leak, faulty MAP/MAF sensor, intake manifold issue.");
    }
    
    if (anomalies.includes("Low Intake Air Mass")) {
        issues.push("🛠️ Low intake airflow. Possible causes: Clogged air filter, MAF sensor issue.");
    }
    
    if (anomalies.includes("Thermostat Issue")) {
        issues.push("🌡️ Thermostat malfunction. Possible causes: Stuck-open thermostat (overcooling) or stuck-closed (overheating).");
    }
    
    if (anomalies.includes("Airflow Restriction")) {
        issues.push("🔧 Airflow restriction detected. Possible causes: Dirty air filter, intake blockage, throttle body issue.");
    }
    
    // Combinations of two issues
    if (anomalies.includes("High Coolant Temperature") && anomalies.includes("High RPM")) {
        issues.push("🔥 Overheating under high RPM. Possible causes: Radiator blockage, low coolant, thermostat failure.");
    }
    if (anomalies.includes("High Coolant Temperature") && anomalies.includes("Low Speed")) {
        issues.push("🔥 Overheating at low speed. Possible causes: Radiator fan failure, coolant circulation issue.");
    }
    if (anomalies.includes("High Coolant Temperature") && anomalies.includes("High Speed")) {
        issues.push("🚗 Overheating even at high speed. Possible causes: Radiator blockage, coolant leak.");
    }
    if (anomalies.includes("Low Intake Air Mass") && anomalies.includes("High RPM")) {
        issues.push("🛠️ Low intake airflow at high RPM. Possible causes: Clogged air filter, MAF sensor issue.");
    }
    if (anomalies.includes("High Intake Air Mass") && anomalies.includes("Low Coolant Temperature")) {
        issues.push("🌡️ Unusually high air intake with low coolant temperature. Possible causes: Fuel mixture issue or turbo boost leak.");
    }
    if (anomalies.includes("Thermostat Issue") && anomalies.includes("High Coolant Temperature")) {
        issues.push("🌡️ Overheating due to thermostat issue. Possible causes: Stuck-closed thermostat preventing coolant flow.");
    }
    if (anomalies.includes("Thermostat Issue") && anomalies.includes("Low Coolant Temperature")) {
        issues.push("🌡️ Engine running too cool. Possible causes: Stuck-open thermostat, inefficient heating.");
    }
    if (anomalies.includes("Airflow Restriction") && anomalies.includes("Low Intake Air Mass")) {
        issues.push("🛠️ Low intake airflow due to restriction. Possible causes: Clogged air filter, intake manifold blockage.");
    }
    
    // Combinations of three issues
    if (anomalies.includes("High Coolant Temperature") && anomalies.includes("High RPM") && anomalies.includes("Thermostat Issue")) {
        issues.push("🔥 Severe overheating under high RPM. Possible causes: Thermostat stuck closed, poor coolant flow.");
    }
    if (anomalies.includes("Low Intake Air Mass") && anomalies.includes("High RPM") && anomalies.includes("Airflow Restriction")) {
        issues.push("🛠️ Severe airflow restriction at high RPM. Possible causes: Dirty air filter, throttle body issue, intake leak.");
    }
    if (anomalies.includes("High Coolant Temperature") && anomalies.includes("Low Speed") && anomalies.includes("Thermostat Issue")) {
        issues.push("🔥 Overheating at low speed due to thermostat issue. Possible causes: Thermostat stuck closed, poor circulation.");
    }
    
    // Combinations of four issues
    if (anomalies.includes("High Coolant Temperature") && anomalies.includes("High RPM") && anomalies.includes("Low Speed") && anomalies.includes("Thermostat Issue")) {
        issues.push("🔥 Critical overheating in all conditions. Possible causes: Severe coolant flow restriction, failing radiator.");
    }
    if (anomalies.includes("Low Intake Air Mass") && anomalies.includes("High RPM") && anomalies.includes("Airflow Restriction") && anomalies.includes("Thermostat Issue")) {
        issues.push("🛠️ Severe airflow and cooling issues. Possible causes: Blocked intake and coolant flow restriction.");
    }

    return issues.length > 0 ? issues.join("<br>") : "⚠️ Unknown issue. Further diagnostics needed.";
}
setInterval(sendData, 500);