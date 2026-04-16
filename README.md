# Thermal Drift-Based Appliance Health Monitoring Using IoT and Machine Learning

An IoT + Machine Learning project that detects early signs of appliance failure
by monitoring temperature patterns using Arduino and an unsupervised ML model.


## Description

This project monitors real-time temperature data from an appliance (iron box) using
an Arduino with a DHT11 sensor, and applies machine learning to detect abnormal
thermal patterns before failure occurs.

A total of **782 temperature readings** were collected. Thermal drift was simulated
by adding an artificial +5°C increase to the last 20% of data. An **Isolation Forest**
(unsupervised ML model) was used to detect anomalies — identifying **32 abnormal
instances**, most of them in the drift region — enabling predictive maintenance
without needing labeled data.

## Technologies Used

- **Hardware:** Arduino, DHT11 Temperature & Humidity Sensor
- **Language:** Python, Arduino (C++)
- **Libraries:** pandas, numpy, matplotlib, scikit-learn
- **ML Model:** Isolation Forest (Unsupervised Anomaly Detection)
- **Environment:** [e.g., VS Code / Jupyter Notebook]

## Hardware Setup

Refer to the wiring diagram below for connecting the DHT11 sensor to the Arduino:

![Arduino Connections](images/arduino_connections.png)

## Installation

To run this project locally:

1. Clone the repository:
git clone https://github.com/SubhasriiT/thermal-drift-monitoring.git

2. Navigate to the project folder:
cd thermal-drift-monitoring

3. Install required Python libraries:
pip install pandas numpy matplotlib scikit-learn

4. Upload the Arduino sketch to your board using the **Arduino IDE**:
   - Open `arduino/thermal_monitor.ino`
   - Select your board and COM port
   - Click **Upload**

## Usage

1. Run the Arduino sketch to begin collecting temperature readings via Serial Monitor
2. Save the readings to `data/temperature_readings.csv`
3. Run the Python analysis script:
python python/analysis.py
4. The system will:
   - Plot rolling mean temperature trends
   - Highlight detected anomalies
   - Trigger visual, console, and audio alerts for abnormal readings

## Results

![Live Simulation](images/live_simulation.png)

| Metric | Value |
|---|---|
| Total Readings | 782 |
| Anomalies Detected | 32 |
| Detection Method | Isolation Forest |
| Drift Simulation | +5°C on last 20% of data |

> Most anomalies were detected in the thermal drift region, confirming successful
> early fault detection before actual appliance failure.

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

**Name:** Subhasri  
**Email:** ktsubhasri2005@gmail.com  
**GitHub:** [SubhasriiT](https://github.com/SubhasriiT)
