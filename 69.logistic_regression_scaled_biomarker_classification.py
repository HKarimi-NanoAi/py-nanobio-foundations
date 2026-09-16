#Topic: Cancer Biomarker Classification via Logistic Regression
#Description: Standardizing clinical biomarker features using StandardScaler and fitting a Logistic Regression model to classify healthy vs. positive oncology samples.
#Application: Clinical baseline modeling, probability estimation and linear decision boundary classification for biomarkers.

#__________________________________________________________________________________

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

cancer_df = pd.DataFrame({
    'Marker_A': [1.1, 8.2, 1.3, 9.0, 1.2, 8.5, 1.4, 9.1, 1.0, 8.8],
    'Marker_B': [0.5, 4.1, 0.6, 4.8, 0.4, 4.3, 0.7, 4.9, 0.3, 4.5],
    'Diagnosis': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

x = cancer_df[['Marker_A','Marker_B']]
y = cancer_df['Diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model_log_re = LogisticRegression(random_state = 42)
model_log_re.fit(x_train_scaled, y_train)
y_pred = model_log_re.predict(x_test_scaled)

model_accuracy = model_log_re.score(x_test_scaled, y_test)*100

print(f"Model Accuracy is {model_accuracy:.2f}%")
print(f"Classification report is \n{classification_report(y_test, y_pred)} ")
