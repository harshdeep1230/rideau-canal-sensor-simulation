
# Rideau Canal IoT Sensor Simulation 

##  Project Overview
This repository contains the Python-based IoT simulation for the Rideau Canal Monitoring System. It generates real-time telemetry data (ice thickness and temperature) and transmits it to Azure IoT Hub using the MQTT protocol.

##  Student Information
* **Name:** Harshdeep Singh
* **Student ID:** [INSERT_YOUR_ID_HERE]
* **Course:** CST8916 - Cloud Computing

---

##  Implementation Details
The simulation mimics three physical sensors placed at:
1. **NAC** (National Arts Centre)
2. **Fifth Avenue**
3. **Dows Lake**

### Features:
* **Real-time Telemetry:** Sends JSON data every 10 seconds.
* **Randomized Logic:** Simulates realistic environmental fluctuations (Ice: 15-40cm | Temp: -15°C to +5°C).
* **Azure Integration:** Uses the `azure-iot-device` SDK for secure connectivity.

---

##  Setup Instructions

### 1. Prerequisites
* Python 3.8 or higher installed.
* An active Azure IoT Hub with three registered devices.

### 2. Installation
Clone this repository and install the required dependencies:
```bash
git clone [https://github.com/harshdeep1230/rideau-canal-sensor-simulation.git](https://github.com/harshdeep1230/rideau-canal-sensor-simulation.git)
cd rideau-canal-sensor-simulation
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory (do not commit this to GitHub) and add your IoT Hub primary connection strings:
```env
CONN_STR_NAC="HostName=...;DeviceId=NAC;SharedAccessKey=..."
CONN_STR_FIFTH="HostName=...;DeviceId=FifthAve;SharedAccessKey=..."
CONN_STR_DOWS="HostName=...;DeviceId=DowsLake;SharedAccessKey=..."
```

### 4. Running the Simulation
Execute the script to start sending data to Azure:
```bash
python sensor_simulator.py
```

---

##  Sample Data Format
The sensors emit messages in the following JSON format:
```json
{
    "location": "DowsLake",
    "iceThickness": 25.4,
    "surfaceTemp": -4.2,
    "externalTemp": -10.5,
    "timestamp": "2026-04-16T12:00:00Z"
}
```

---

##  Related Repositories
* **Main Documentation:** [Link to rideau-canal-monitoring]
* **Web Dashboard:** [Link to rideau-canal-dashboard]

##  References
* [Azure IoT Device SDK for Python](https://pypi.org/project/azure-iot-device/)
