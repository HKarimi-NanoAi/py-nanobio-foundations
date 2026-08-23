#Topic: Simple Linear Regression and Predictive Modeling for Cell Survival
#Description: Modeling cancer cell survival rate kinetics over time (treatment exposure) using SciPy stats.linregress to extract slope, intercept, R-squared and predict cell viability at extended time points (14 hours).
#Application: In vitro drug exposure kinetics, cytotoxicity time-course modeling and predictive pharmacodynamics in oncology research.

#____________________________________________

import pandas as pd
from scipy import stats

cell_data = {
    'Time_Hours': [2, 4, 6, 8, 10, 12],
    'Survival_Rate': [95.0, 82.1, 68.5, 51.2, 35.0, 18.4]
}
df_cell = pd.DataFrame(cell_data)


slope, intercept, r_value, p_value, std_err = stats.linregress(df_cell['Time_Hours'], df_cell['Survival_Rate'])

# y = ab * c
predicted_14 = slope * 14 + intercept

print(f'Slope = {slope:.3f}, r-value = {r_value:.3f}, p-value = {p_value:.3f} and standard error = {std_err:.3f} ')

print(f'Predicted Cell Survival Rate for The time 14 is {predicted_14:.3f}')
