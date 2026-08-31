#Topic: Comprehensive Model Evaluation Metrics for Biosensor Diagnostics
#Description: Evaluating a Logistic Regression classifier on optical biosensor spectral features using Accuracy Score, Confusion Matrix and Classification Report (Precision, Recall, F1-Score).
#Application: Biomedical classifier performance assessment, bio-signal validation and diagnostic model evaluation pipelines.

#_____________________________________________________
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

sensor_data = {
    'Intensity': [12.1, 45.3, 11.2, 89.1, 13.0, 92.4, 10.1, 65.3, 14.2, 88.0],
    'Wavelength': [620, 680, 622, 690, 625, 695, 619, 685, 628, 689],
    'Target': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(sensor_data)


x = df[['Intensity','Wavelength']]
y = df['Target']

scaler = StandardScaler()
scaler_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaler_x, y, test_size = 0.3, random_state = 42)

model = LogisticRegression()
model.fit(x_train, y_train)
y_pred_model = model.predict(x_test)


model_accuracy1 = accuracy_score(y_test, y_pred_model)*100
model_confusion_matrix1 = confusion_matrix(y_test, y_pred_model)

print(f'Accuracy of the model is {model_accuracy1:.2f}% and Confusion matrix is {model_confusion_matrix1}')

print (classification_report(y_test, y_pred_model))
