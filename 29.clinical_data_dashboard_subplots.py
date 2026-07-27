#Topic: Multi-Panel Visualizations Using Matplotlib Subplots
#Description: Creating a 2x2 grid dashboard incorporating line plot, bar chart, histogram and scatter plot to simultaneously report multi-parametric clinical and pharmacological metrics.
#Application: Medical dashboards, automated diagnostic reporting and multi-panel figure compilation for high-impact journal publications.
#_______________________________________________________________________________________________________________

time_b = [1, 2, 3, 4]
drug_concentration_b = [10, 25, 50, 80]

patient_b = ['A', 'B', 'C']
healing_percentage = [60, 82, 95]

patient_age = [20, 22, 25, 28, 30, 35, 40, 42, 45, 50, 55, 60]

dosage = [5, 10, 15, 20]
heart_rate = [70, 75, 85, 95]



plt.subplot(2,2,1)
plt.plot(time_b, drug_concentration_b, color = 'purple', linewidth = 0.7, marker = 'v')
plt.title('Drug Concentration over Time')
plt.xlabel('Time')
plt.ylabel('Drug concentration')
plt.grid(True)

plt.subplot(2,2,2)
plt.bar(patient_b, healing_percentage, color = 'seagreen', hatch = '-', width = 0.8, alpha = 0.3)
plt.title('Patients healing across group')
plt.xlabel('Patients')
plt.ylabel('Percentage of healing')
plt.grid(axis = 'y')


plt.subplot(2,2,3)
plt.hist(patient_age, bins = 4, color = 'darkorange', edgecolor = 'white')
plt.title('Patient Age Distribution')
plt.xlabel('Patient age')
plt.ylabel('Frequency')
plt.grid(True)

plt.subplot(2,2,4)
plt.scatter(dosage, heart_rate, color = 'red', edgecolors = 'white', s = 60)
plt.title('Dosage vs. Heart Rate Response')
plt.xlabel('Dosage')
plt.ylabel('Heart Rate')
plt.grid(True)

plt.tight_layout()
plt.show()
