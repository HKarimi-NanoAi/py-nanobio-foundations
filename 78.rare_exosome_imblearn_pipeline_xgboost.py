#Topic: End-to-End Imbalanced-Learn Pipeline for Rare Exosomal Biomarker Screening
#Description: Encapsulating StandardScaler, SMOTEENN hybrid resampling, and XGBoost classifier into an imblearn Pipeline object to prevent data leakage and ensure standardized, bias-free clinical predictions.
#Application: Production-ready ML architecture, leak-free imbalanced diagnostics and clinical biomarker pipeline development.

#_____________________________________________________________________________

import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from imblearn.combine import SMOTEENN
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score

exosome_rare_df = pd.DataFrame({
    'Exosome_Count': [120, 130, 115, 140, 125, 135, 110, 850, 105, 118, 122, 920, 112, 128, 119, 132],
    'Flow_Rate': [1.2, 1.3, 1.1, 1.4, 1.2, 1.3, 1.0, 5.1, 1.1, 1.2, 1.1, 5.8, 1.0, 1.3, 1.2, 1.4],
    'Rare_Diagnosis': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
})

x = exosome_rare_df[['Exosome_Count','Flow_Rate']]
y = exosome_rare_df['Rare_Diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.25, random_state = 42)

pipeline = Pipeline([('Scaler', StandardScaler()),
                     ('smoteenn', SMOTEENN(smote = SMOTE(k_neighbors = 1, random_state = 42))),
                     ('model',XGBClassifier(n_estimators = 50, learning_rate = 0.1, random_state = 42))])

pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_test)
model_accuracy = accuracy_score(y_test, y_pred)*100

classif_rep = classification_report(y_test, y_pred)

print(f'Model Accuracy is {model_accuracy}')
print(f'Classification Report is \n{classif_rep}')
