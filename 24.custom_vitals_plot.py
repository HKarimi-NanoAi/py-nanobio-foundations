#Topic: Advanced Visual Customization in Matplotlib Plots
#Description: Enhancing a clinical time-series graph by customizing line thickness, marker geometries and contrasting face colors for high-impact readability.
#Application: Designing refined visual figures for medical publications and analytical laboratory research reports.

#_________________________________________________________________________________________________________________

import matplotlib.pyplot as plt

time = [0, 10, 20, 30, 40, 50, 60]
heart_rate = [72, 75, 88, 110, 95, 78, 70]

plt.plot(time, heart_rate, color = 'black', linewidth = 2, marker = 'o', markersize = 8, markerfacecolor='red')
plt.xlabel('Time')
plt.ylabel('Heart Rate')
plt.grid(True)

plt.show()
