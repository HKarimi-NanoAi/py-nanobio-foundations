#Topic: Boolean Indexing and Sub-group Analysis in Pandas
#Description: Filtering a DataFrame using a critical clinical threshold (CRP > 10 mg/L) to isolate critical ICU patients and compute the mean age of this specific subset.
#Application: Stratifying patient cohorts based on biomarker severity to analyze demographic trends in critical care data.

#____________________________________________________________________

import pandas as pd
icu_data = {
    'Patient_ID': ['P01', 'P02', 'P03', 'P04', 'P05'],
    'Age': [28, 45, 32, 61, 50],
    'CRP_Level': [3.2, 12.4, 1.5, 45.8, 8.9]}
    
df_icu = pd.DataFrame(icu_data)
critical_patients = df_icu['CRP_Level'] > 10
filtered_patients = df_icu[critical_patients]
mean_patient_age = filtered_patients['Age'].mean()

print(f"Mean age of critical patients is {mean_patient_age}")
