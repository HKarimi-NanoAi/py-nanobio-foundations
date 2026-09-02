#Topic: Extracting Confusion Matrix Components in Clinical Oncology Datasets
#Description: Implementing a Logistic Regression classifier for cancer biomarker screening (Age and Antigen Level) and unpacking Confusion Matrix elements (TN, FP, FN, TP) via the .ravel() method alongside a detailed Classification Report.
#Application: Clinical cancer screening automation, diagnostic false-negative minimization and medical Machine Learning evaluation.

#__________________________________________
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

cancer_data = {
    'Age': [45, 62, 35, 70, 50, 28, 65, 58, 40, 72, 33, 55],
    'Biomarker_Level': [2.1, 8.5, 1.2, 9.1, 3.4, 0.9, 7.8, 6.2, 1.8, 9.8, 1.1, 5.9],
    'Diagnosis': [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
}
df_cancer = pd.DataFrame(cancer_data)

x = df_cancer[['Age','Biomarker_Level']]
y = df_cancer['Diagnosis']

scaler = StandardScaler()
scaler_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaler_x, y, test_size = 0.3 , random_state = 42)

model = LogisticRegression()
model.fit(x_train, y_train)
y_prediction = model.predict(x_test)

t_negative, f_positive, f_negative, t_positive = confusion_matrix(y_test, y_prediction).ravel()

print('Classification Report:')
print(classification_report(y_test, y_prediction))
