#Topic: Missing Data Handling, Quality Filtering and Mean Imputation
#Description: Preprocessing genomic expression profile matrices using Pandas: identifying NaN values, filtering low-quality sample runs (Quality_Pass control) and performing mean imputation on missing gene expression features.
#Application: Bioinformatics pipeline quality control (QC), microarray/RNA-seq data curation and missing feature imputation prior to ML modeling.
#__________________________________________________________________________________________________________
import pandas as pd
import numpy as np

gene_data = {
    'Sample_ID': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8'],
    'Tissue_Type': ['Liver', 'Liver', 'Kidney', 'Kidney', 'Liver', 'Kidney', 'Liver', 'Kidney'],
    'Gene_A_Exp': [12.4, np.nan, 15.1, 8.9, np.nan, 10.2, 14.0, 9.5],
    'Gene_B_Exp': [100.5, 110.2, np.nan, 95.0, 105.8, 98.2, 115.0, np.nan],
    'Quality_Pass': [True, True, False, True, True, False, True, True]
}



df_data = pd.DataFrame(gene_data)

df_copy = df_data.copy()

null_data = df_copy.isnull().sum()

print(f'sum of null data is\n{null_data}')

df_filtered = df_copy[df_copy['Quality_Pass'] == True].copy()


df_filtered['Gene_A_Exp'] = df_filtered['Gene_A_Exp'].fillna(df_filtered['Gene_A_Exp'].mean())
df_filtered['Gene_B_Exp'] = df_filtered['Gene_B_Exp'].fillna(df_filtered['Gene_B_Exp'].mean())

print(df_filtered)
