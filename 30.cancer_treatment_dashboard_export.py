#Topic: Advanced Subplots, Logarithmic Scaling and High-Res Figure Export
#Description: Creating a multi-panel oncology dashboard with scatter and log-scale bar plots, saving the publication-ready figure at 300 DPI and retrieving the execution working directory using os.
#Application: Preparing high-resolution figures for journal manuscripts and pharmacological dose-response study evaluations.

#__________________________________________

import matplotlib.pyplot as plt
drug_a_concentration = [2, 4, 6, 8]
cancer_cell_inhib = [20, 45, 70, 90]

groups = ['G1', 'G2', 'G3', 'G4']
drug_b_concentration = [15, 35, 60, 80]

plt.subplot(2,2,1)
plt.scatter(drug_a_concentration, cancer_cell_inhib, color = 'crimson', s= 70, alpha = 0.3, edgecolor = 'white', linewidth = 0.8, marker = '^', cmap = 'plasma', vmin = 20, vmax = 85)
plt.xlabel('Drug concentration')
plt.ylabel('Cancer cell inhibition (%)')
plt.title('Effect of drung concentrations\n on cancer cell inhibition')
plt.grid(True)


plt.subplot(2,2,2)
plt.bar(groups, drug_b_concentration, color = 'navy', hatch = '*', edgecolor = 'orange', linewidth = 0.98, alpha = 0.5, linestyle = ':', log=True )
plt.xlabel('Study Groups')
plt.ylabel('Concentration')
plt.title('Drug B inhibition level for 4 groups')
plt.grid(axis ='y')


plt.tight_layout()
plt.savefig('cancer_treatment_dashboard.png', dpi = 300, bbox_inches = 'tight' )
plt.show()

#working directory location
import os

print(os.getcwd())
