#Topic: Frequency Distribution Analysis Using Histograms in Matplotlib
#Description: Plotting a customized histogram to evaluate the distribution and persistence of drug lifetime across a sample cohort of 20 patients.
#Application: Pharmacokinetics, half-life estimation, and pharmacodynamics data stratification in clinical trials.
#__________________________________________________________________________________________________________________

import matplotlib.pyplot as plt

drug_lifetime = [2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 8, 8, 9, 10, 11, 12, 12, 14, 15, 16]

plt.hist(drug_lifetime, bins = 6, color = 'purple', edgecolor = 'white', alpha = 0.4, rwidth = 0.98)
plt.title('Distribution of Drug Lifetime in Patients')
plt.xlabel('Drug lifetime in 20 patients')
plt.ylabel('Number of patients')
plt.grid(axis = 'y', linestyle = '-.')

plt.show()
