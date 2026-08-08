#Topic: Clinical Trial Data Wrangling, Conditional Filtering and Group Aggregation
#Description: Processing oncology trial metrics (tumor reduction percentage), applying multi-condition patient eligibility filters and calculating treatment group efficacy using Pandas DataFrames.
#Application: Clinical trial data pipelines, drug efficacy screening and cohort demographic segmentation.

#______________

import pandas as pd

clinical_trial_data = {
    'Patient_ID': ['PT-101', 'PT-102', 'PT-103', 'PT-104', 'PT-105', 'PT-106', 'PT-107', 'PT-108'],
    'Group': ['Drug_A', 'Drug_A', 'Placebo', 'Drug_B', 'Drug_B', 'Placebo', 'Drug_A', 'Drug_B'],
    'Age': [45, 62, 58, 34, 71, 50, 29, 65],
    'Tumor_Size_Before': [12.5, 15.0, 11.0, 14.2, 18.0, 10.5, 13.0, 16.5], # mm
    'Tumor_Size_After': [4.2, 11.5, 10.8, 3.5, 8.0, 10.1, 2.1, 7.8],    # mm
    'Side_Effects': [True, False, False, True, True, False, False, True]
}


df_trial = pd.DataFrame(clinical_trial_data)

df_trial['Reduction_Percentage'] = ((df_trial['Tumor_Size_Before'] - df_trial['Tumor_Size_After']) / df_trial['Tumor_Size_Before']) * 100

print('Primary Clinical Trial Data is:')
print(df_trial)

df_trial['Eligible'] = (df_trial['Age'] < 60) & (df_trial['Reduction_Percentage'] > 50)
filtered_df = df_trial[df_trial['Eligible'] == True]

print('Filtered Data :')
print(filtered_df)

group_mean = df_trial.groupby('Group')['Reduction_Percentage'].mean()
print(f'Drug Efficacy Based on Mean Tumor Reduction Percentage: \n {group_mean}')
