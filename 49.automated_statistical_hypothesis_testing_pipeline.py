#Topic: Automated Statistical Testing Pipeline via Normality Verification
#Description: Building an automated decision pipeline: evaluates dataset normality using Shapiro-Wilk test (scipy.stats.shapiro), dynamically routing to Student's T-Test (parametric) if normal or Mann-Whitney U Test (non-parametric) if skewed/non-normal.
#Application: Automated bioinformatic pipelines, high-throughput assay curation and adaptive hypothesis testing in clinical data science.
#_______________________________________________________________________________

import pandas as pd
from scipy import stats

data = {
    'Group_A': [10.2, 11.5, 12.1, 9.8, 10.9],
    'Group_B': [45.1, 88.2, 12.0, 95.4, 62.3]
}
df = pd.DataFrame(data)


stat_a, p_value_a = stats.shapiro(df['Group_A'])
stat_b, p_value_b = stats.shapiro(df['Group_B'])

if p_value_a > 0.05 and p_value_b > 0.05:
    print("[PIPELINE SELECTION]: Parametric Assumptions Met (Both Groups Normal).")
    stat_ttest, p_value_t = stats.ttest_ind(df['Group_A'], df['Group_B'])
    print(f'Executed Independent T-Test | Statistic: {stat_ttest:.3f}')
elif p_value_a < 0.05 or p_value_b < 0.05:
    if p_value_a < 0.05:
        print('[PIPELINE SELECTION]: Non-Parametric Fallback (Non-Normality Detected).(GroupA)')
        stat_mann, p_value_mann = stats.mannwhitneyu(df['Group_A'], df['Group_B'])
        print(f'Its Mannwhitney test is {stat_mann}')
    elif p_value_b < 0.05:
        print('[PIPELINE SELECTION]: Non-Parametric Fallback (Non-Normality Detected).(GroupB)')
        stat_mann, p_value_mann = stats.mannwhitneyu(df['Group_A'], df['Group_B'])
        print(f'Its Mannwhitney test is {stat_mann}')
