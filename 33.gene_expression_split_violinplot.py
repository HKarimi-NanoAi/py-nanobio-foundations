#Topic: Comparative Distribution Analysis via Split Violin Plots
#Description: Visualizing differential gene expression levels across control and treatment groups, split by patient clinical status (Healthy/Sick) using Seaborn's split violinplot and custom publication typography.
#Application: Differential gene expression analysis, target validation in drug discovery and clinical cohort response profiling.
#___________________________________

import seaborn as sns
import matplotlib.pyplot as plt

treatment_method = ['Control', 'Control', 'Control', 'Control', 'Treatment', 'Treatment', 'Treatment', 'Treatment']
gene_expression = [2.1, 2.5, 2.3, 2.8, 5.4, 5.9, 6.1, 6.5]
patient_condition = ['Healthy', 'Sick', 'Healthy', 'Sick', 'Healthy', 'Sick', 'Healthy', 'Sick']

sns.set_theme(style = 'ticks', font = 'serif', font_scale = 1)
plt.figure(figsize = (6,6))
sns.violinplot(x = treatment_method, y = gene_expression, hue = patient_condition, split = True, palette = 'muted')
plt.title('Patient Conditions and Gene Expressing based on Different Treatment Methods')
plt.xlabel('Treatment Method')
plt.ylabel('Gene Expression')
plt.grid(True, linestyle = ':')

plt.show()
