#Topic: Z-Score Standardization and Feature Scaling via NumPy
#Description: Standardizing proteomics data distributions (mean = 0, std = 1) using vector arithmetic and demonstrating floating-point precision in numeric computations.
#Application: Feature scaling for machine learning pipelines (PCA, SVM, KNN), proteomics quantification normalization and biomarker scaling.
#________________________________________________________________

import numpy as np

protein_levels = [120.5, 340.2, 210.8, 180.0, 520.1, 290.4]

protein_np = np.array(protein_levels)
protein_mean = np.mean(protein_np)
protein_std = np.std(protein_np)

protein_z = (protein_np -protein_mean)/ protein_std
new_protein_mean = np.mean(protein_z)

print(f'Standardization of data :\n{protein_z}')
print(f'Mean of proteins:{new_protein_mean:.20f}')
