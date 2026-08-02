#Topic: Correlation Matrix Heatmaps and Covariate Analysis via Seaborn
#Description: Visualizing pairwise correlation coefficients among key clinical factors (Age, BMI, Blood Pressure, Glucose) using a divergent color map (vlag) with numerical annotations and grid separation.
#Application: Clinical feature selection, biomarker discovery and exploratory data analysis (EDA) for predictive medical modeling.

#____________________________________________________________________________

import matplotlib.pyplot as plt
import seaborn as sns

clinical_factor = ['Age', 'BMI', 'Blood Pressure', 'Glucose']
corr_matrix = [
    [ 1.00,  0.45,  0.62,  0.30],
    [ 0.45,  1.00,  0.50,  0.78],
    [ 0.62,  0.50,  1.00,  0.40],
    [ 0.30,  0.78,  0.40,  1.00]
]

sns.set_theme (style = 'darkgrid')
plt.figure(figsize = (8,8))

sns.heatmap(corr_matrix, annot = True, xticklabels = clinical_factor, yticklabels = clinical_factor, cmap ='vlag', fmt = '.2f', vmin = -1, vmax =  1, linecolor='white', linewidths = 1,  )
plt.title('Clinical Correlation Matrix Heatmap')

plt.show()
