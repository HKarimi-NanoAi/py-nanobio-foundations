#Topic: One-Way ANOVA for Multi-Group Nanoparticle Cytotoxicity Screening
#Description: Conducting One-Way Analysis of Variance across four novel nanocarrier formulations (A, B, C, D) to detect statistically significant variance in cell cytotoxicity profiles and identify the safest formulation (minimum mean toxicity).
#Application: High-throughput nanocarrier biocompatibility screening, formulation optimization and statistical bioassay evaluation.

#_____________________________________________

import pandas as pd
from scipy import stats

nano_toxicity = {
    'Formulation_A': [85.2, 88.1, 84.0, 86.5],
    'Formulation_B': [70.1, 72.5, 68.9, 71.0],
    'Formulation_C': [45.0, 48.2, 42.1, 46.8],
    'Formulation_D': [83.9, 87.0, 85.1, 84.8]
}
df_tox = pd.DataFrame(nano_toxicity)

f_test, p_value = stats.f_oneway(*[df_tox[col] for col in df_tox.columns])


if p_value < 0.05:
    print(f'Statistically Significant Difference Detected (p-value = {p_value:.3f}).')
    min_toxicity = df_tox.mean().idxmin()
    print(f'{min_toxicity} has MINIMUM mean toxicity.')
else:
    print(f'NOT Statistically Significant Difference Detected (p-value = {p_value:.3f}).')
