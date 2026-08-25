#Topic: Advanced Hypothesis Testing Pipeline: Normality & Homogeneity Audit
#Description: Evaluating nanoparticle synthesis batch sizes using a two-tier statistical decision framework: Shapiro-Wilk for normality, Levene's test for equal variance, dynamically routing to standard Student's T-test, Welch's T-test (unequal variance) or Mann-Whitney U.
#Application: Nanomaterial synthesis reproducibility evaluation, biophysical characterization quality control and adaptive experimental statistics.
#_____________________________________________________

import pandas as pd
from scipy import stats

np_data = {
    'Method_A': [25.1, 24.8, 25.3, 24.9, 25.0],
    'Method_B': [30.2, 18.5, 35.1, 22.0, 28.4]
}
df_np = pd.DataFrame(np_data)

stat_a, p_value_a = stats.shapiro(df_np['Method_A'])
stat_b, p_value_b = stats.shapiro(df_np['Method_B'])

if p_value_a > 0.05 and p_value_b > 0.05:
    print('Parametric Assumptions Met (Both Groups Normal).')
    stat_lev, p_value_lev = stats.levene(df_np['Method_A'], df_np['Method_B'])
    
    if p_value_lev > 0.05:
        print(f'Equal Variances. p-value = {p_value_lev:.3f}')
        stat_tt, p_value_tt = stats.ttest_ind(df_np['Method_A'], df_np['Method_B'], equal_var = True)
        print(f"T-statistic is {stat_tt:.3f} and p-value is {p_value_tt:.3f}")
      
    else:
        print(f'Unequal Variances. p-value = {p_value_lev:.3f}')
        stat_we, p_value_we = stats.ttest_ind(df_np['Method_A'], df_np['Method_B'], equal_var = False)
        print(f"T-statistic is {stat_we:.3f} and p-value is {p_value_we:.3f}")
      
else:
    print('Non-Parametric Fallback (Non-Normality Detected)')
    stat_mw, p_value_mw = stats.mannwhitneyu(df_np['Method_A'], df_np['Method_B'])
    print(f"U-statistic is {stat_mw:.3f} and p-value is {p_value_mw:.3f}")
