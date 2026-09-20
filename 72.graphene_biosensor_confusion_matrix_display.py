#Topic: Graphene Biosensor Classification & ConfusionMatrixDisplay Rendering
#Description: Standardizing electrochemical current density and impedance metrics from graphene sensors, training Logistic Regression and rendering confusion matrix using Scikit-Learn's native ConfusionMatrixDisplay class.
#Application: Graphene-based biosensing, electrochemical biomarker detection and native Scikit-Learn evaluation visualization.

#___________________________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

graphene_sensor_df = pd.DataFrame({
    'Current_Density_uA': [2.1, 15.4, 3.0, 18.2, 2.5, 14.1, 4.2, 17.5, 1.9, 12.8, 4.0, 19.1, 3.1, 16.0],
    'Impedance_kOhm': [85, 12, 78, 10, 82, 15, 65, 11, 90, 18, 70, 8, 75, 14],
    'Biomarker_Detected': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

x = graphene_sensor_df[['Current_Density_uA','Impedance_kOhm']]
y = graphene_sensor_df['Biomarker_Detected']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model_lr = LogisticRegression(random_state = 42)
model_lr.fit(x_train_scaled, y_train)

y_pred = model_lr.predict(x_test_scaled)

class_report = classification_report(y_test, y_pred)
print(f"Classification Report is {class_report}")

cm = confusion_matrix(y_test, y_pred)
print(f"Confusion Matrix is {cm}")

cm_disp = ConfusionMatrixDisplay(confusion_matrix  = cm)
cm_disp.plot(cmap = "Purples")
plt.title('Confusion Matrix')
plt.show()
