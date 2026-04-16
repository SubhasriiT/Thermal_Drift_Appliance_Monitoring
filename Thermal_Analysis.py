# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Load Dataset
df = pd.read_csv("C:/Users/subha/temperature_data.csv")  # <-- your CSV path
print(df.head())
print(df.info())
if 'Timestamp' not in df.columns:
    df['Timestamp'] = df.index


# Clean Data
df['Temperature'] = pd.to_numeric(df['Temperature'], errors='coerce')
df['Temperature'] = df['Temperature'].interpolate(method='linear')
df['Temperature'] = df['Temperature'].bfill().ffill()
df['Timestamp'] = pd.to_datetime(df['Timestamp'])



# Simulate Thermal Drift
n = len(df)
drift_start = int(n * 0.8)
drift_max = 5
df['Temperature_drifted'] = df['Temperature'].copy()
df.loc[drift_start:, 'Temperature_drifted'] += np.linspace(0, drift_max, n - drift_start)
plt.figure(figsize=(10,4))
plt.plot(df['Timestamp'], df['Temperature'], label='Normal Temp')
plt.plot(df['Timestamp'], df['Temperature_drifted'], label='Drifted Temp', color='orange')
plt.title("Temperature with Simulated Thermal Drift")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.legend()
plt.show()

# Train Isolation Forest
X_train = df.loc[:drift_start-1, ['Temperature_drifted']]
X_full = df[['Temperature_drifted']]

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X_train)

# Detect Anomalies
df['anomaly'] = model.predict(X_full)
df['anomaly_flag'] = df['anomaly'].apply(lambda x: 1 if x==-1 else 0)

# Plot Anomalies
plt.figure(figsize=(12,5))
plt.plot(df['Timestamp'], df['Temperature_drifted'], label='Temperature')
plt.scatter(df['Timestamp'][df['anomaly_flag']==1], 
            df['Temperature_drifted'][df['anomaly_flag']==1], 
            color='red', label='Anomaly')
plt.title("Isolation Forest Detected Anomalies")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.legend()
plt.show()

# Rolling Mean Visualization
window_size = 20
df['Rolling_Mean_Temp'] = df['Temperature_drifted'].rolling(window=window_size).mean()

plt.figure(figsize=(12,5))
plt.plot(df['Rolling_Mean_Temp'], label='Rolling Mean Temperature')
plt.plot(df['Temperature_drifted'], label='Drifted Temperature', alpha=0.4)
plt.xlabel('Time Index')
plt.ylabel('Temperature')
plt.title('Rolling Mean Trend Showing Thermal Drift')
plt.legend()
plt.show()


# Check Anomaly Summary
print("Total anomalies detected:", df['anomaly_flag'].sum())
print(df[['Timestamp','Temperature_drifted','anomaly_flag']].tail(20))


# ALERT MECHANISM
for i in range(len(df)):
    if df.loc[i, 'anomaly_flag'] == 1:
        print("⚠ ALERT: Abnormal thermal drift detected!")
        print("⚠ Appliance may fail soon. Preventive action recommended.")
        break



# SOUND ALERT 
import winsound
for i in range(len(df)):
    if df.loc[i, 'anomaly_flag'] == 1:
        print("⚠ ALERT: Abnormal thermal drift detected!")
        print("⚠ Appliance may fail soon. Preventive action recommended.")
        winsound.Beep(1000, 1000)  # frequency, duration
        break


# SHOWING ALERT ON PLOT
plt.figure(figsize=(12,5))
plt.plot(df['Temperature_drifted'], label='Temperature')

alert_index = df[df['anomaly_flag']==1].index[0]
plt.axvline(alert_index, color='red', linestyle='--', label='ALERT TRIGGER POINT')

plt.title("Thermal Drift Detection with Alert Trigger")
plt.xlabel("Time Index")
plt.ylabel("Temperature")
plt.legend()
plt.show()
