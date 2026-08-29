#Topic: Binary Classification of Biosensor Signals via Logistic Regression
#Description: End-to-end Machine Learning pipeline: standardizing optical biosensor spectral features (Signal Intensity & Peak Wavelength), partitioning train/test sets and training a Logistic Regression classifier for target analyte detection.
#Application: Optical biosensor target classification, medical diagnostic automation and binary biomarker detection pipelines.
#________________________________________________________________
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

biosensor_data = {
    'Signal_Intensity': [10.2, 45.1, 11.5, 88.2, 12.1, 95.4, 9.8, 62.3],
    'Peak_Wavelength': [630, 680, 632, 690, 631, 695, 629, 685],
    'Target_Detected': [0, 1, 0, 1, 0, 1, 0, 1]
}
df_sensor = pd.DataFrame(biosensor_data)

x = df_sensor[['Signal_Intensity','Peak_Wavelength']]
y = df_sensor['Target_Detected']

scaler = StandardScaler()
scaled_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaled_x, y,test_size = 0.25, random_state  = 42)

model = LogisticRegression()
model.fit(x_train, y_train)
y_prediction_test = model.predict(x_test)

print (f'Model prediction:\n{y_prediction_test}\nActual Ground Truth:\n {y_test.values}')
