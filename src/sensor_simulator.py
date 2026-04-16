import os
import time
import json
import random
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message
from dotenv import load_dotenv

# Load connection strings from .env file
load_dotenv()

# Configuration
LOCATIONS = {
    "NAC": os.getenv("CONN_STR_NAC"),
    "FifthAve": os.getenv("CONN_STR_FIFTH"),
    "DowsLake": os.getenv("CONN_STR_DOWS")
}

def generate_telemetry(location_id):
    """Generates realistic ice and temperature data."""
    # Logic: Dows Lake usually has thicker ice than the NAC area
    base_ice = 28.0 if location_id == "DowsLake" else 22.0
    
    return {
        "location": location_id,
        "iceThickness": round(base_ice + random.uniform(-5.0, 5.0), 2),
        "surfaceTemp": round(random.uniform(-10.0, 2.0), 2),
        "externalTemp": round(random.uniform(-15.0, -2.0), 2),
        "timestamp": datetime.utcnow().isoformat()
    }

def run_simulation():
    print("--- Rideau Canal IoT Simulation Started ---")
    print("Press Ctrl+C to stop the simulation.\n")

    try:
        # Create clients for all registered devices
        clients = {}
        for loc, conn_str in LOCATIONS.items():
            if conn_str:
                clients[loc] = IoTHubDeviceClient.create_from_connection_string(conn_str)
                print(f"[System] Connected client for {loc}")
            else:
                print(f"[Warning] Missing connection string for {loc}")

        while True:
            for loc, client in clients.items():
                # Create the data payload
                data = generate_telemetry(loc)
                payload = json.dumps(data)
                
                # Create Azure IoT Message object
                message = Message(payload)
                message.content_encoding = "utf-8"
                message.content_type = "application/json"

                # Send to Azure
                print(f"[Sending] {loc} -> Ice: {data['iceThickness']}cm | Temp: {data['surfaceTemp']}°C")
                client.send_message(message)
                
            # Wait 10 seconds before the next burst of data
            time.sleep(10)

    except KeyboardInterrupt:
        print("\n[System] Simulation stopped by user.")
    except Exception as e:
        print(f"\n[Error] An unexpected error occurred: {e}")
    finally:
        print("[System] Shutting down IoT clients...")
        for client in clients.values():
            client.shutdown()

if __name__ == "__main__":
    run_simulation()
