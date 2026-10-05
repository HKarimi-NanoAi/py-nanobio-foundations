#Topic: Cross-Validated Imbalanced Pipeline Evaluation via ROC-AUC Metric
#Description: Evaluating a complete biosensor classification pipeline (StandardScaler + SMOTEENN + XGBoost) using 5-fold cross-validation and ROC-AUC scoring metric to ensure generalization on graphene sensor data.
#Application: Robust clinical cross-validation, leak-free pipeline validation and ROC-AUC biomarker assessment.
#__________________________________________________________

import pandas as pd
from sklearn.model_selection import cross_val_score
from imblearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from imblearn.combine import SMOTEENN
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier

graphene_sensor_df = pd.DataFrame({
    'Current_Density_uA': [2.1, 15.4, 3.0, 18.2, 2.5, 14.1, 4.2, 17.5, 1.9, 12.8, 4.0, 19.1, 3.1, 16.0, 2.8, 14.5, 3.5, 17.0, 2.2, 13.0],
    'Impedance_kOhm': [85, 12, 78, 10, 82, 15, 65, 11, 90, 18, 70, 8, 75, 14, 80, 13, 68, 9, 88, 16],
    'Biomarker_Detected': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

x = graphene_sensor_df[['Current_Density_uA','Impedance_kOhm']]
y = graphene_sensor_df['Biomarker_Detected']

pipeline = Pipeline([('scaler', StandardScaler()),
                     ('smoteenn', SMOTEENN(smote = SMOTE(k_neighbors = 1, random_state = 42))),
                     ('model', XGBClassifier(n_estimators = 50, learning_rate = 0.1, random_state = 42))])

scores = cross_val_score(pipeline, x, y, cv = 5, scoring = 'roc_auc')

print(f"All Fold Scores {scores}")
print(f"Mean ROC-AUC score: {scores.mean()*100:.2f}%")
