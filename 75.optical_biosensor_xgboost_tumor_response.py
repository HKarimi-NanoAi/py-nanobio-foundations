#Topic: Optical Biosensor Tumor Response Prediction via XGBoost Classifier
#Description: Evaluating fluorescence intensity and wavelength shift metrics from optical biosensors to predict tumor response to nanotherapy using Gradient Boosted Decision Trees (XGBoost) and visualising performance via ConfusionMatrixDisplay with YlGnBu colormap.
#Application: Optical biosensing, nanotheranostics and gradient boosting classification for oncology treatment monitoring.

#__________________________________________
import pandas as pd

from sklearn.model_selection import train_test_split

from xgboost import XGBClassifier

from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

import matplotlib.pyplot as plt



optical_sensor_df = pd.DataFrame({

    'Fluorescence_Intensity': [12.1, 85.3, 18.2, 90.1, 14.8, 78.5, 25.5, 82.0, 19.4, 68.2, 31.0, 92.4, 15.0, 75.0, 22.0],

    'Wavelength_Shift_nm': [0.2, 3.5, 0.4, 4.1, 0.3, 3.1, 0.8, 3.8, 0.5, 2.9, 1.1, 4.5, 0.4, 3.0, 0.7],

    'Tumor_Response': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] # داده دارای پیچیدگی و نویز مرزی

})



x = optical_sensor_df[['Fluorescence_Intensity','Wavelength_Shift_nm']]

y = optical_sensor_df['Tumor_Response']



x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3, random_state = 42)

model_xgb = XGBClassifier(n_estimators = 100, learning_rate = 0.05, max_depth = 3, random_state = 42)

model_xgb.fit(x_train, y_train)

y_pred = model_xgb.predict(x_test)



classif_rep = classification_report(y_test, y_pred)

print(f"Classification Report is {classif_rep}")



cm = confusion_matrix(y_test, y_pred)

print(f'Confusion Matrix is\n{cm}')



cm_disp = ConfusionMatrixDisplay(confusion_matrix = cm)

cm_disp.plot(cmap = 'YlGnBu')

plt.title("Confusion Matrix")

plt.show()
