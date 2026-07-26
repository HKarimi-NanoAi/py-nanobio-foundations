#Topic: Multivariate Scatter Plots (Bubble Charts) in Matplotlib
#Description: Visualizing 3-dimensional environmental/chemical data by mapping two continuous variables to X-Y axes and encoding the 3rd variable (intensity) into dynamic marker sizes.
#Application: Environmental monitoring, eco-toxicology, and tracking multi-pollutant synergistic interactions in bio-sensing.
#_____________________________________________________________________________________

import matplotlib.pyplot as plt

pollutant_a = [1, 2, 3, 4, 5, 6, 7, 8]
pollutant_b = [10, 15, 12, 25, 20, 35, 30, 42]
pollutant_intensity = [30, 60, 90, 120, 150, 200, 250, 300]

plt.scatter(pollutant_a, pollutant_b, s = pollutant_intensity, color = 'mediumseagreen', alpha=0.6, edgecolors='black', marker = 'D' )
plt.title('Intensity of Pollutant A and B')
plt.xlabel('Pollutant A concentration')
plt.ylabel('Pollutant B concentration')
plt.grid(True, linestyle = '-.')

plt.show()
