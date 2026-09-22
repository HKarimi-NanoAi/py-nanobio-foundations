#Topic: SVM Hyperparameter Tuning via GridSearchCV for CRISPR Nanocarrier Delivery
#Description: Optimizing Support Vector Machine (SVC) hyperparameters (C and kernel) using 3-fold cross-validation on gold-polymer nanocarrier data (N/P ratio and Zeta potential) to predict gene editing success.
#Application: Gene delivery optimization, nanomedicine modeling and automated hyperparameter optimization using GridSearchCV.
#____________________________________________________________________________________________

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

crispr_df = pd.DataFrame({
    'N_P_Ratio': [1.2, 5.5, 2.0, 8.1, 1.8, 6.2, 2.5, 7.8, 1.1, 5.0, 3.2, 8.5, 2.1, 6.0, 4.1],
    'Zeta_Potential_mV': [-15, +22, -10, +28, -12, +18, -5, +25, -18, +15, +2, +30, -8, +20, +8],
    'Editing_Success': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] # داده پیچیده با هم‌پوشانی واقعی
})

x = crispr_df[['N_P_Ratio', 'Zeta_Potential_mV']]
y = crispr_df['Editing_Success']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3, random_state = 42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

param_grid = {'C': [0.1, 1, 10, 100], 'kernel': ['linear', 'rbf']}

grid = GridSearchCV(SVC(random_state = 42), param_grid, cv = 3)
grid.fit(x_train_scaled, y_train)

print(f"Best Parameters are {grid.best_params_}")
best_model = grid.best_estimator_

y_pred = grid.predict(x_test_scaled)
model_accuracy = accuracy_score(y_test, y_pred)*100
print(f"Model Accuracy is {model_accuracy}")

classif_report = classification_report(y_test, y_pred)
print(f'Classification Report:\n{classif_report}')
