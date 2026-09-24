#Topic: Multi-Biomarker Profiling & Feature Importance Evaluation via XGBoost
#Description: Evaluating a 4-biomarker array using XGBoost Classifier, calculating prediction accuracy and plotting feature importance scores using XGBoost's built-in plot_importance module.
#Application: Biomarker discovery, multiplex biosensing arrays and explainable machine learning in diagnostics.
#___________________________________________________________________________________________

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier, plot_importance
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

array_df = pd.DataFrame({
    'Biomarker_1': [12.1, 85.3, 18.2, 90.1, 14.8, 78.5, 25.5, 82.0, 19.4, 68.2, 31.0, 92.4, 15.0, 75.0, 22.0, 88.0],
    'Biomarker_2': [0.2, 3.5, 0.4, 4.1, 0.3, 3.1, 0.8, 3.8, 0.5, 2.9, 1.1, 4.5, 0.4, 3.0, 0.7, 4.2],
    'Biomarker_3': [150, 20, 135, 12, 160, 25, 110, 8, 175, 30, 85, 140, 165, 18, 125, 10],
    'Biomarker_4': [1.1, 5.5, 1.8, 8.1, 1.2, 6.2, 2.5, 7.8, 1.0, 5.0, 3.2, 8.5, 1.9, 6.0, 2.1, 8.0],
    'Therapy_Response': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

x = array_df[['Biomarker_1','Biomarker_2','Biomarker_3','Biomarker_4']]
y = array_df['Therapy_Response']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.25, random_state = 42)
model= XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

model_accuracy = accuracy_score(y_test, y_pred)*100
print(f"Model Accuracy is {model_accuracy}")

classif_rep = classification_report(y_test, y_pred)
print(f"Classification Report is\n{classif_rep}")

plot_importance(model)
plt.title('Feature Importance')
plt.show()
