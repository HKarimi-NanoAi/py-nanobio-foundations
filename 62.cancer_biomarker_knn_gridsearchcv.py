#Topic: Hyperparameter Optimization via GridSearchCV for KNN Classifier
#Description: Automated hyperparameter tuning (n_neighbors and weights) using 3-Fold Cross-Validation on standardized oncology biomarker data (Marker A and Marker B) to identify optimal model settings.
# Application: Clinical ML model optimization, automated hyperparameter search and precision disease classification benchmarking.
#______________________________________________________________________________________________

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

cancer_data = pd.DataFrame({
    'Marker_A': [1.1, 8.2, 1.3, 9.0, 1.2, 8.5, 1.4, 9.1, 1.0, 8.8, 1.5, 8.9],
    'Marker_B': [0.5, 4.1, 0.6, 4.8, 0.4, 4.3, 0.7, 4.9, 0.3, 4.5, 0.8, 4.7],
    'Diagnosis': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

x = cancer_data[['Marker_A','Marker_B']]
y = cancer_data['Diagnosis']

scaler = StandardScaler()
scaler_x = scaler.fit_transform(x)

param_grid = {'n_neighbors': [1, 3, 5] , 'weights': ['uniform', 'distance']}

grid_search = GridSearchCV((KNeighborsClassifier()), param_grid, cv = 3)
grid_search.fit(scaler_x, y)

print(f"Best Parameters are:{grid_search.best_params_}")
print(f"Best Accuracy is {grid_search.best_score_*100:.2f}%")
