# MQTT-Sensor-Simulation-using-ESP32

This project demonstrates how to use the ESP32 to simulate an IoT system using the MQTT protocol.  
Two sensors — **LDR (Light Dependent Resistor)** and an **Analog Temperature Sensor (NTC)** — send data to a public MQTT broker. Two LEDs are controlled automatically based on sensor readings (Auto Mode only).

---

## Working
1. ESP32 connects to Wi-Fi and MQTT broker.  
2. LDR and LM35 sensors are read periodically.  
3. ESP32 automatically controls LEDs:
   - If **temperature > 30°C**, **Red LED** turns **ON**.  
   - If **light < 500** (low light), **Green LED** turns **ON**.  
4. Sensor readings and LED states are published every **5 seconds**.

---
Open a terminal and run:

```bash
# Subscribe to sensor topic (test broker)
mosquitto_sub -h test.mosquitto.org -t "mqtt-demo/sensors" -v
```

## Output example:
<img width="727" height="446" alt="image" src="https://github.com/user-attachments/assets/c8935944-af63-4f8b-96f0-765b9de7cb86" />

## Screenshots:
<img width="940" height="626" alt="image" src="https://github.com/user-attachments/assets/6f323af9-7dcd-4946-b18d-f3c056b7e5f6" />
<img width="940" height="464" alt="image" src="https://github.com/user-attachments/assets/37e6c663-7b03-4dfe-ae2b-f29cf4bc199d" />
<img width="940" height="564" alt="image" src="https://github.com/user-attachments/assets/2b3c9f0a-eeee-4b02-8b9d-6e5894eab21c" />







