#Topic: Hyperparameter Tuning: Finding Optimal K in KNN Classifier
#Description: Evaluating the impact of different K values (1 to 6) on model accuracy using optical spectroscopy features (Absorbance Peaks) and plotting the optimization curve with Matplotlib.
#Application: Hyperparameter optimization, optical spectroscopy classification and distance-based Machine Learning tuning.

#____________________________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

spectro_df = pd.DataFrame({
    'Absorbance_Peak1': [0.11, 0.85, 0.14, 0.92, 0.12, 0.88, 0.15, 0.79, 0.10, 0.95, 0.13, 0.89, 0.16, 0.82],
    'Absorbance_Peak2': [0.22, 1.45, 0.25, 1.58, 0.21, 1.48, 0.26, 1.39, 0.19, 1.62, 0.23, 1.51, 0.27, 1.42],
    'Biomarker_Status': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

x = spectro_df[['Absorbance_Peak1','Absorbance_Peak2']]
y = spectro_df['Biomarker_Status']

scaler = StandardScaler()
scaler_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaler_x, y, test_size = 0.3, random_state  = 42)

accuracies =[]
values = range(1,7)

for i in values:
    model = KNeighborsClassifier(n_neighbors = i)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy_model = accuracy_score(y_test, y_pred) * 100
    accuracies.append(accuracy_model)

print(f"Model Accuracy in range from 1 to 6 is {accuracies}")

plt.plot(values, accuracies, marker = 'v')
plt.xlabel('Value of K')
plt.ylabel('Accuracy')
plt.title('Finding optimal K for KNN')
plt.show()
