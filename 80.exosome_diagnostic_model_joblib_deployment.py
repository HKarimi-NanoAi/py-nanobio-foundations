#Topic: End-to-End Model Serialization, Joblib Deployment & Clinical Inference
#Description: Training a full imbalanced-learn pipeline (Scaler + SMOTEENN + XGBoost), serializing it using joblib, reloading the deployed artifact and performing clinical risk classification & probability inference on incoming patient samples.
#Application: Clinical ML model deployment, MLOps, pipeline serialization and automated exosome-based disease risk scoring.

#___________________________________________________________________________

import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from imblearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from imblearn.combine import SMOTEENN
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier


os.chdir(r'') #Write the file path where you want to save this Python program.

exosome_df = pd.DataFrame({
    'Exosome_Count': [120, 130, 115, 140, 125, 135, 110, 850, 105, 118, 122, 920, 112, 128, 119, 132],
    'Flow_Rate': [1.2, 1.3, 1.1, 1.4, 1.2, 1.3, 1.0, 5.1, 1.1, 1.2, 1.1, 5.8, 1.0, 1.3, 1.2, 1.4],
    'Diagnosis': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
})

x = exosome_df[['Exosome_Count','Flow_Rate']]
y = exosome_df['Diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

pipeline = Pipeline([('scaler', StandardScaler()),
                     ("smoteenn", SMOTEENN(smote = SMOTE(k_neighbors = 1, random_state = 42))),
                     ('model', XGBClassifier(n_estimators = 50, learning_rate = 0.1, random_state = 42))])

pipeline.fit(x_train, y_train)

joblib.dump(pipeline, 'exosome_diagnostic_model.joblib')
deployed_model = joblib.load('exosome_diagnostic_model.joblib')
new_data = [[125, 1.2], [890, 5.4],[130, 1.1]]  #from three patients
prediction = deployed_model.predict(new_data)
print(f"Prediction for 3 patients(0:Normal, 1:High Risk):")
for i, pred in enumerate(prediction):
    print(f"Patient {i+1}: Class{pred}")


predict_prob = deployed_model.predict_proba(new_data)*100
print(f"Class probability percentage {predict_prob}%")
