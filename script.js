const ESP32_URL = "http://127.0.0.1:5000/predict"; // Change to your ESP32's IP

function updateValue(id) {
    document.getElementById(id + "Value").innerText = document.getElementById(id).value;
}

function sendData() {
    let rpm = document.getElementById("rpm").value;
    let coolant = document.getElementById("coolant").value;
    let speed = document.getElementById("speed").value;
    let intake = document.getElementById("intake").value;

    let data = {
        "rpm": parseInt(rpm),
        "coolant_temp": parseInt(coolant),
        "speed": parseInt(speed),
        "intake_air_mass": parseInt(intake)
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
        if (data.anomalies.length > 0) {
            resultElement.innerHTML = `⚠️ Anomalies Detected: ${data.anomalies.join(", ")}`;
            resultElement.style.color = "red";
        } else {
            resultElement.innerHTML = "✅ No anomalies detected.";
            resultElement.style.color = "green";
        }
        resultElement.classList.remove("hidden");
    })
    .catch(error => console.error("Error:", error));
}
