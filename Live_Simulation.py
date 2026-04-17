import pandas as pd
import numpy as np
import time
import winsound

# Load & clean dataset
df = pd.read_csv("C:/Users/subha/temperature_data.csv")
df['Temperature'] = pd.to_numeric(df['Temperature'], errors='coerce')
df['Temperature'] = df['Temperature'].interpolate().bfill().ffill()

# Simulation parameters
base_temp = df['Temperature'].iloc[0]
final_temp = base_temp + 5.0
steps = 25              
bar_length = 30             
warning_step = int(steps * 0.7)
alert_step = steps - 2  

temperatures = np.linspace(base_temp, final_temp, steps)

print("\n🔴 LIVE THERMAL MONITORING STARTED...\n")

for i, temp_value in enumerate(temperatures):
    if i < warning_step:
        status = "[NORMAL]"
    elif i < alert_step:
        status = "[WARNING]"
    else:
        status = "[ALERT]"

    filled_length = int(bar_length * (i + 1) / steps)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    print(f"Time {i:03d} | Temp: {temp_value:.2f}°C {status} |{bar}|")

    if status == "[ALERT]" and i == alert_step:
        print("\n⚠ ALERT TRIGGERED ⚠")
        print("⚠ Abnormal thermal drift detected!")
        print("⚠ Appliance failure may occur soon!")
        winsound.Beep(1000, 1000)
        break
    time.sleep(0.2)
