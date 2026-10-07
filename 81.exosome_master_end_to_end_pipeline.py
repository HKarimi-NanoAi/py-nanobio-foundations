#Topic: End-to-End Exosome Biomarker Screening Master Pipeline
#Description: Integrated clinical pipeline incorporating StandardScaler, SMOTEENN hybrid resampling, XGBoost classifier, 3-fold cross-validation (ROC-AUC), confusion matrix visualization and Joblib serialization.
#Application: Production-grade clinical AI, master diagnostic pipelines and robust end-to-end medical machine learning workflows.
#____________________________________________________________________________


import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from imblearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from imblearn.combine import SMOTEENN
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier, plot_importance
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, accuracy_score

exosome_full_df = pd.DataFrame({
    'Exosome_Count': [120, 130, 115, 140, 125, 135, 110, 850, 105, 118, 122, 920, 112, 128, 119, 132, 890, 950, 121, 131],
    'Flow_Rate': [1.2, 1.3, 1.1, 1.4, 1.2, 1.3, 1.0, 5.1, 1.1, 1.2, 1.1, 5.8, 1.0, 1.3, 1.2, 1.4, 5.3, 6.0, 1.2, 1.3],
    'Fluorescence_Signal': [10, 12, 11, 15, 9, 13, 8, 85, 10, 14, 11, 92, 9, 13, 10, 12, 88, 96, 11, 13],
    'Diagnosis': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0]
})

x = exosome_full_df[['Exosome_Count','Flow_Rate','Fluorescence_Signal']]
y = exosome_full_df['Diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)

pipeline = Pipeline([('scaler', StandardScaler()),
                     ('smoteenn', SMOTEENN(smote = SMOTE(k_neighbors = 1, random_state = 42))),
                     ('model', XGBClassifier(n_estimators = 50, learning_rate = 0.1, random_state = 42))])

scores = cross_val_score(pipeline, x, y, cv = 3, scoring = 'roc_auc')

print(f'All Fold Scores: {scores}')
print(f'Mean Accuracy: {scores.mean()*100:.3f}%')

pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_test)
classif_rep = classification_report(y_test, y_pred)

print(f'Classification report\n {classif_rep}')

cm = confusion_matrix(y_test, y_pred)
print(f"Confusion Matrix:\n{cm}")

cm_disp = ConfusionMatrixDisplay(confusion_matrix = cm)
cm_disp.plot(cmap ='Blues')
plt.title('COnfusion Matrix')
plt.show()

joblib.dump(pipeline, 'exosome_master_pipeline.joblib')
