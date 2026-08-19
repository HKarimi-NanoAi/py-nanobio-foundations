#Topic: Non-Parametric Multi-Group Comparison via Kruskal-Wallis H-Test
#Description: Evaluating non-normally distributed cytotoxicity levels (with outliers) across three natural herbal extracts using SciPy stats.kruskal and identifying the most potent formulation based on median values.
#Application: Phytomedicine screening, natural product bioassays and outlier-robust multi-group statistical analysis.
#_____________________________________________________

import pandas as pd
from scipy import stats

plant_extracts = {
    'Extract_1': [12.5, 14.1, 85.0, 13.2, 15.0], 
    'Extract_2': [45.2, 48.1, 46.0, 44.8, 47.5],
    'Extract_3': [88.1, 92.0, 89.5, 91.2, 87.8]
}
df_extracts = pd.DataFrame(plant_extracts)

krus, p_Value = stats.kruskal(*[df_extracts[col] for col in df_extracts.columns])

if p_Value <0.05:
    print(f'P-value is "{p_Value:.3f}". Statistically significant difference detected.')
    max_mid = df_extracts.median().idxmax()
    print(f'{max_mid} has Maximum Median')
else:
    print(f'P-value is "{p_Value:.3f}". NOT Statistically significant difference detected.')
