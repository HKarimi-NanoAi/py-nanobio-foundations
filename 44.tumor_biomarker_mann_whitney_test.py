#Topic: Non-Parametric Two-Sample Analysis via Mann-Whitney U Test
#Description: Evaluating non-normally distributed oncology biomarker levels between healthy control tissue and tumor samples using SciPy stats.mannwhitneyu for robust non-parametric inference.
#Application: Clinical biomarker discovery, non-parametric bioassay screening and outlier-resistant comparative oncology data analysis.
#_________________________________________________________________________________________

from scipy import stats

healthy = [10.2, 11.5, 12.1, 9.8, 10.9]
tumor = [45.1, 88.2, 12.0, 95.4, 62.3]

mannwhi, p_value = stats.mannwhitneyu(healthy, tumor)

if p_value < 0.05:
    print(f'P-value is "{p_value:.3f}". Statistically significant difference detected.')
else:
    print(f'P-value is "{p_value:.3f}". NOT Statistically significant difference detected.')
