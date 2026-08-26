#Topic: Range Normalization via Scikit-Learn MinMaxScaler (0 to 1 Scaling)
#Description: Normalizing optical fiber biosensor spectral data features (Wavelength in nm and Signal Intensity in a.u.) to a fixed [0, 1] range using sklearn.preprocessing.MinMaxScaler.
#Application: Optical biosensor signal processing, bio-photonic feature scaling and neural network preprocessing for spectral classification.
#________________________________________________--

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

sensor_data = {
    'Wavelength_nm': [632.8, 650.0, 780.0, 850.5],
    'Intensity_au': [0.12, 0.85, 0.45, 0.99]
}
df_sensor = pd.DataFrame(sensor_data)

mmscaler = MinMaxScaler()
mm_scaler_array = mmscaler.fit_transform(df_sensor)
mm_scaler_df = pd.DataFrame(mm_scaler_array, columns = df_sensor.columns)
print("Normalized Biosensor Spectral Features (Scaled to [0, 1]):")
print(mm_scaler_df)
