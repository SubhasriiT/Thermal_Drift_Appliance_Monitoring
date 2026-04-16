# Thermal Drift-Based Appliance Health Monitoring Using IoT and Machine Learning

An IoT + Machine Learning project that detects early signs of appliance failure
by monitoring temperature patterns using Arduino and an unsupervised ML model.

> Done as part of a **Final Year Project** at **[Your College Name]**

## Description

This project monitors real-time temperature data from an appliance (iron box) using
an Arduino Uno with a DHT11 sensor, and applies machine learning to detect abnormal
thermal patterns before failure occurs.

A total of **782 temperature readings** were collected. Thermal drift was simulated
by adding an artificial +5°C increase to the last 20% of data. An **Isolation Forest**
(unsupervised ML model) was used to detect anomalies — identifying **32 abnormal
instances**, most in the drift region — enabling predictive maintenance without
needing labeled data.

## Technologies Used

- **Hardware:** Arduino Uno, DHT11 Temperature & Humidity Sensor
- **Language:** Python, Arduino (C++)
- **Libraries:** pandas, numpy, matplotlib, scikit-learn
- **ML Model:** Isolation Forest (Unsupervised Anomaly Detection)
- **Environment:** Arduino IDE 2.3.6, Python

## Project Structure

```
thermal-drift-monitoring/
│
├── README.md
├── iot_project.ino               # Arduino sketch for data collection
├── iot_project_code.py           # ML analysis and alert system
├── images/
│   ├── hardware_setup.jpg        # Arduino + DHT11 + iron box
│   ├── live_simulation.jpg       # Live monitoring in Arduino IDE
│   ├── thermal_drift_graph.png   # Normal vs drifted temperature
│   └── anomaly_detection.png     # Isolation Forest anomaly plot
└── data/
    └── temperature_readings.csv  # Collected sensor data (782 readings)
```

## Hardware Setup

The DHT11 sensor is connected to the Arduino Uno and placed near the iron box
to capture real-time surface temperature readings.

![Hardware Setup](images/hardware_setup.jpg)

**Connections:**
- DHT11 VCC → Arduino 5V
- DHT11 GND → Arduino GND
- DHT11 DATA → Arduino Digital Pin 2

## Live Monitoring

The Arduino IDE Serial Monitor streams real-time temperature readings at 9600 baud.
The red LED indicates an alert trigger when thermal drift is detected.

![Live Simulation](images/live_simulation.jpg)

## Installation

To run this project locally:

1. Clone the repository:
```
   git clone https://github.com/[your-username]/thermal-drift-monitoring.git
```

2. Navigate to the project folder:
```
   cd thermal-drift-monitoring
```

3. Install required Python libraries:
```
   pip install pandas numpy matplotlib scikit-learn
```

4. Upload the Arduino sketch to your board using **Arduino IDE**:
   - Open `iot_project.ino`
   - Select **Arduino Uno** and your COM port
   - Click **Upload**

## Usage

1. Run the Arduino sketch → temperature readings stream via Serial Monitor
2. Save the readings to `data/temperature_readings.csv`
3. Run the Python script:
```
   python iot_project_code.py
```
4. The system will:
   - Plot normal vs thermally drifted temperature trends
   - Detect anomalies using Isolation Forest
   - Trigger visual, console, and **audio (1 kHz beep)** alerts

## Results

### Temperature with Simulated Thermal Drift
![Thermal Drift Graph](images/thermal_drift_graph.png)

### Isolation Forest Anomaly Detection
![Anomaly Detection](images/anomaly_detection.png)

| Metric | Value |
|---|---|
| Total Readings | 782 |
| Anomalies Detected | 32 |
| Detection Method | Isolation Forest |
| Drift Simulation | +5°C on last 20% of data |
| Alert Types | Console + Visual + Audio (1 kHz) |

### Live Simulation Status Transitions
| Time Range | Status | Description |
|---|---|---|
| 000–016 | 🔵 NORMAL | Blue thermometer, within safe range |
| 017–022 | 🟡 WARNING | Yellow, nearing alert threshold |
| 023+ | 🔴 ALERT | Red, thermal drift confirmed |

## Key Features

- Works without labeled data (unsupervised learning)
- Detects early-stage faults for predictive maintenance
- Real-time visual, console, and audio alerts
- Safe testing — no need to damage the actual appliance
- Low-cost and suitable for IoT edge deployment

## Contributing

Contributions are welcome. If you would like to improve this project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
and is intended for educational purposes.

## Contact

For any queries or suggestions, feel free to reach out:

**Name:** [Your Name]
**Email:** [your-email@gmail.com]
**GitHub:** [your-username](https://github.com/your-username)
