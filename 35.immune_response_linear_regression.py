#Topic: Linear Regression Modeling and Visualization via Seaborn lmplot
#Description: Integrating Pandas DataFrames with Seaborn's lmplot to analyze dose-response dynamics (Immune Response vs Concentration) including 95% confidence interval estimation and custom markers.
#Application: Immunological dose-response fitting, bioassay quantification and predictive pharmacodynamics.
#_________________________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_1 = pd.DataFrame({'Concentration': [1, 2, 3, 4, 5, 6, 7, 8], 'Immune_Response': [12, 22, 35, 41, 52, 68, 73, 89]})

sns.lmplot(x = 'Concentration', y = 'Immune_Response', data = data_1, line_kws = {'color': 'red'}, markers ='D')
plt.title('Dose-Dependent Immune Response Regression Analysis', y=1.02)
plt.grid(True, linestyle = ':')
plt.show()
