#Topic: Clinical Data Visualization Using Matplotlib
#Description: Plotting a time-series line chart to monitor a patient's heart rate variations during 60-minute surgical procedure.
#Application: Developing real-time patient monitoring dashboards, tracking physiological responses and anesthesia depth analysis.
#_____________________________________________________________________________________________

import matplotlib.pyplot as plt

time_min = [0, 10, 20, 30, 40, 50, 60]
heart_rate = [72, 75, 88, 110, 95, 78, 70]

plt.plot(time_min, heart_rate)

plt.title('Heart rate monitoring of the patient during the surgery.')
plt.xlabel('Surgery Time (min)')
plt.ylabel('Heart rate (bpm)')
plt.grid(True)

plt.show()
