#Topic: Multi-Criteria Boolean Filtering in Pandas (Complex Conditions)
#Description: Combining multiple logical conditions (Age > 60 AND CRP > 10) using the bitwise '&' operator to screen high-risk patient cohorts.
#Application: Clinical decision support systems (CDSS) for automated triage and prioritizing vulnerable patient care in ICUs.
#_______________________________________________________________________________________________________________________________________

import pandas as pd
icu_data = {
    'Patient_ID': ['P01', 'P02', 'P03', 'P04', 'P05', 'P06'],
    'Age': [28, 65, 32, 71, 50, 80],
    'CRP_Level': [3.2, 12.4, 1.5, 45.8, 8.9, 2.1],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F']}

df_patients = pd.DataFrame(icu_data)

critical_situation = (df_patients['Age'] > 60) & (df_patients['CRP_Level'] > 10)

filtered_patients = df_patients[critical_situation]
patients_id = list(filtered_patients['Patient_ID'])

print(f'Patients with critical situations:\n {patients_id}')
