#Topic: Classifier Benchmarking: Logistic Regression vs Decision Tree
#Description: Comparative evaluation of Logistic Regression and Decision Tree classifiers on optical spectroscopy data (Absorbance at 630nm and Fluorescence Intensity) for target biomarker detection.
#Application: Optical spectroscopy classification, ML model selection and comparative diagnostic algorithm evaluation.
#___________________________________

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = {
    'Absorbance_630nm': [0.15, 0.82, 0.18, 0.95, 0.12, 0.89, 0.22, 0.78, 0.11, 0.91],
    'Fluorescence_Intensity': [120, 850, 140, 920, 110, 880, 160, 790, 105, 940],
    'Biomarker_Present': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}
df_bio = pd.DataFrame(data)

x = df_bio[['Absorbance_630nm','Fluorescence_Intensity']]
y = df_bio['Biomarker_Present']

scaler = StandardScaler()
scaler_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaler_x, y, test_size = 0.3, random_state = 42)

model_lr = LogisticRegression()
model_lr.fit(x_train, y_train)
y_predict_lr = model_lr.predict(x_test)

accuracy_lr = accuracy_score(y_test, y_predict_lr)


model_dt = DecisionTreeClassifier(random_state  = 42)
model_dt.fit(x_train, y_train)
y_pred_dt = model_dt.predict(x_test)

accuracy_dt = accuracy_score(y_test, y_pred_dt)

print(f'Model Accuracy based on Logistic Regression is {accuracy_lr} and based on Decision Tree is {accuracy_dt}')
