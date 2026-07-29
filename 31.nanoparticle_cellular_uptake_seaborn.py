#Topic: Categorical Scatter Plots using Seaborn (Hue Parameter)
#Description: Visualizing dose-dependent nanoparticle absorption in healthy vs. cancerous cellular models using Seaborn's scatterplot with automated group color-encoding (hue) and customized theme ticks.
#Application: Nanomedicine evaluation, targeted drug delivery efficiency and differential uptake quantification in cancer bio-analytics.

#_______________________________________________________________

import seaborn as sns
import matplotlib.pyplot as plt

dose = [10, 20, 30, 40, 10, 20, 30, 40]
absorption = [15, 30, 45, 60, 25, 55, 75, 95]
cell_type = ['Healthy', 'Healthy', 'Healthy', 'Healthy', 'Cancer', 'Cancer', 'Cancer', 'Cancer']

sns.set_theme(style = 'ticks')
sns.scatterplot(x = dose, y = absorption, hue = cell_type, s = 100)

plt.title('Nanoparticle Cellular Uptake in Healthy vs. Cancer Cells Across Dosages')
plt.xlabel('Nanoparticle Dosage (µg/mL)')
plt.ylabel('Absorption Rate (%)')
plt.grid(True, linestyle = ':')
plt.legend(title = 'Cell Type')

plt.show()
