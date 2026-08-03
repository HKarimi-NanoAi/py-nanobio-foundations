#Topic: Exploratory Multivariate Pairwise Relationships via Seaborn Pairplot
#Description: Generating a corner-triangular pairwise grid with regression fitting (kind='reg') and histograms (diag_kind='hist') across clinical metrics (Age, Blood Pressure, Glucose), segmented by treatment group (Placebo vs. Drug) using the husl palette.
#Application: Exploratory clinical data analysis (EDA), covariate pattern identification and multidimensional pharmacotherapy evaluation.

#____________________________________________________________________
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

clinical_df = pd.DataFrame({
    'Age': [25, 45, 50, 30, 60, 55, 35, 65],
    'Blood_Pressure': [110, 130, 140, 115, 150, 145, 120, 155],
    'Glucose': [85, 110, 125, 90, 140, 135, 95, 150],
    'Treatment': ['Placebo', 'Drug', 'Drug', 'Placebo', 'Drug', 'Drug', 'Placebo', 'Drug']
})

sns.pairplot(clinical_df, hue = 'Treatment', palette = 'husl', corner = True, diag_kind = 'hist', kind = 'reg')
plt.show()
