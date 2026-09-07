#Topic: K-Fold Cross-Validation for Robust Classifier Evaluation
#Description: Implementing 4-Fold Cross-Validation on a K-Nearest Neighbors classifier (k=3) using standardized oncology biomarker features (Marker A and Marker B) to ensure model stability and generalization.
#Application: Oncology screening, biomarker classification and cross-validation benchmarking for small clinical datasets.
#_______________________________________________________________________________

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

cancer_df = pd.DataFrame({
    'Marker_A': [1.1, 8.2, 1.3, 9.0, 1.2, 8.5, 1.4, 9.1, 1.0, 8.8, 1.5, 8.9],
    'Marker_B': [0.5, 4.1, 0.6, 4.8, 0.4, 4.3, 0.7, 4.9, 0.3, 4.5, 0.8, 4.7],
    'Diagnosis': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

x = cancer_df[['Marker_A', 'Marker_B']]
y = cancer_df['Diagnosis']

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

model = KNeighborsClassifier(n_neighbors = 3)
scores = cross_val_score(model, x_scaled, y, cv = 4)

mean_accuracy = scores.mean()*100
print(f'Mean Accuracy is {mean_accuracy:.2f}')
