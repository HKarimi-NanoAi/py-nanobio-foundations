#Topic: Optical Sensor Biomarker Binding Classification using KNN
#Description: Implementing a K-Nearest Neighbors (KNN) classifier (k=3) on optical sensor data (Refractive Index and Peak Shift) to predict target biological binding events with standardized features.
#Application: Optical biosensor signal processing, Surface Plasmon Resonance (SPR) data analysis and distance-based Machine Learning.
#___________________________________________________________


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

sensor_df = pd.DataFrame({
    'Refractive_Index': [1.33, 1.45, 1.34, 1.48, 1.32, 1.46, 1.35, 1.49, 1.31, 1.47],
    'Shift_Peak': [2.1, 8.4, 2.3, 9.1, 1.9, 8.8, 2.5, 9.5, 1.8, 8.9],
    'Target_Binding': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})


x = sensor_df[['Refractive_Index','Shift_Peak']]
y = sensor_df['Target_Binding']

scaler = StandardScaler()
scaler_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test =train_test_split(scaler_x, y, test_size = 0.3, random_state = 42)

model = KNeighborsClassifier(n_neighbors = 3)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
model_knn_accuracy = accuracy_score(y_test, y_pred)*100
print(f'Acuuracy of this model is {model_knn_accuracy:2f}%')
print('Classification Report:')
print(classification_report(y_test, y_pred))
