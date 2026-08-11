#Topic: Multi-Omics Data Integration via Left Join and Mean Imputation
#Description: Merging clinical patient demographics with genomic profiling data (TP53 expression) using Pandas left merge, followed by imputing missing expression values for unmeasured control subjects.
#Application: Multi-omics integration pipelines, clinical trial metadata consolidation, and biomarker feature engineering.
#________________________________________________________________________
import pandas as pd


df_clinical = pd.DataFrame({'Patient_ID': ['PT-01', 'PT-02', 'PT-03', 'PT-04'],'Age': [45, 52, 39, 61],'Condition': ['Control', 'Case', 'Case', 'Control']})


df_genomics = pd.DataFrame({'Patient_ID': ['PT-01', 'PT-02', 'PT-03'],'TP53_Expression': [2.4, 8.1, 7.5]})                      

merged_data = pd.merge (df_clinical, df_genomics, on = 'Patient_ID', how ='left')
print(merged_data)
print('============= NaN data filled with mean ====================')
merged_data['TP53_Expression'] = merged_data['TP53_Expression'].fillna(merged_data['TP53_Expression'].mean())
print(merged_data)
