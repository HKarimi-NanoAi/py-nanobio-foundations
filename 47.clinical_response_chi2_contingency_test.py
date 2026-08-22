#Topic: Chi-Square Test of Independence for Categorical Clinical Outcomes
#Description: Evaluating statistical association between treatment arms and patient response categories (Responded vs Non-responded) using a 2x2 contingency matrix via SciPy stats.chi2_contingency.
#Application: Clinical trial responder rate evaluation, pharmacogenomic association studies and categorical bioassay validation.
#______________________________________________________
import numpy as np
from scipy import stats

#row1 = 40: responded, 10:not responded
#row2 = 20:responded, 30: not responded
clinical_responses = np.array([
    [40, 10],
    [20, 30]
])

res_chi2_con, p_value, dof, expected = stats.chi2_contingency(clinical_responses)

print(f'Chi2-contingency is {res_chi2_con:.3f} and p-value is {p_value:.3f}.')
print(f'Degrees of Freedom is {dof} and Expected Frequencies are {expected}.')

if p_value <0.05:
    print ('Statistically Significant Association Between Treatment and Response Detected')
else:
    print('Not Statistically Significant Association Between Treatment and Response Detected')
