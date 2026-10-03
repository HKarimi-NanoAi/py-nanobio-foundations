#Topic: Rare Exosomal Biomarker Screening via SMOTEENN Resampling & XGBoost
#Description: Handling extreme class imbalance in clinical exosome screening by integrating Hybrid Resampling (SMOTE oversampling + ENN noise cleanup) with XGBoost gradient boosting classifier to eliminate majority class bias.
#Application: Rare disease biomarker discovery, imbalanced clinical diagnostics and robust hybrid resampling pipelines in bio-data science.

#______________________________________________________________________________________

import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.combine import SMOTEENN
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score

exosome_rare_df = pd.DataFrame({
    'Exosome_Count': [120, 130, 115, 140, 125, 135, 110, 850, 105, 118, 122, 920, 112, 128, 119, 132],
    'Flow_Rate': [1.2, 1.3, 1.1, 1.4, 1.2, 1.3, 1.0, 5.1, 1.1, 1.2, 1.1, 5.8, 1.0, 1.3, 1.2, 1.4],
    'Rare_Diagnosis': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0] #1 is too rare
})


x = exosome_rare_df[['Exosome_Count','Flow_Rate']]
y = exosome_rare_df['Rare_Diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)
print("Original dataset shape:", Counter(y_train))

model_xgb = XGBClassifier(n_estimators = 50, learning_rate = 0.1, random_state = 42)
smoteenn = SMOTEENN(random_state= 42, smote = SMOTE(k_neighbors = 1))
x_train_res, y_train_res = smoteenn.fit_resample(x_train, y_train)
model_xgb.fit(x_train_res, y_train_res)
print("Resampled data shape:", Counter(y_train_res))
y_pred = model_xgb.predict(x_test)

classif_rep = classification_report(y_test, y_pred)
print(f"Classification report is \n {classif_rep}")
