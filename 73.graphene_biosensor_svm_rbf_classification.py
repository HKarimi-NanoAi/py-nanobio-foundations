#Topic: Non-Linear Graphene Biosensor Classification via RBF Kernel SVM
#Description: Standardizing electrochemical current density and impedance metrics, fitting a Support Vector Classifier (SVC) with an RBF kernel (C=10) and evaluating detection performance using ConfusionMatrixDisplay with the Viridis colormap.
#Application: Electrochemical biosensing, support vector machine diagnostics and non-linear biomarker detection.
#_____________________________________________________________


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

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

model_svm = SVC(kernel = "rbf", C = 10, random_state = 42)
model_svm.fit(x_train_scaled, y_train)

y_pred = model_svm.predict(x_test_scaled)

classif_rep = classification_report(y_test, y_pred)
print(f"CLassification Report is:\n{classif_rep}")

cm = confusion_matrix(y_test, y_pred)
print(f"Confusion Matrix is\n{cm}")

cm_disp = ConfusionMatrixDisplay(confusion_matrix = cm)
cm_disp.plot(cmap = 'viridis')
plt.title('Confusion Matrix')
plt.show()
