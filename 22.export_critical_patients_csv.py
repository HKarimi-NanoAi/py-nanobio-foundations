#Topic: Exporting Filtered Pandas DataFrames to CSV Files 
#Description: Applying multi-criteria logical masks to clinical datasets and exporting the high-priority patient records into a clean, production-ready CSV file using the .to_csv() method.
#Application: Generating real-time automated reports for hospital emergency departments and triage teams.
#__________________________________________________________________________________________________________________


import pandas as pd
icu_data = {
    'Patient_ID': ['P01', 'P02', 'P03', 'P04', 'P05', 'P06'],
    'Age': [28, 65, 32, 71, 50, 80],
    'CRP_Level': [3.2, 12.4, 1.5, 45.8, 8.9, 2.1]
}
df_icu = pd.DataFrame(icu_data)

critical_priority = (df_icu['Age'] > 60) & (df_icu['CRP_Level'] > 10)
critical_df = df_icu[critical_priority]
critical_df.to_csv('icu_emergency_patients.csv', index = False)
print('This file has been saved successfully.')
