#Topic: Feature Scaling via Scikit-Learn StandardScaler (Z-score Normalization)
#Description: Standardizing clinical numerical features (Age and Blood Pressure) to zero mean and unit variance using sklearn.preprocessing.StandardScaler to prepare tabular biomedical data for Machine Learning models.
#Application: Machine learning feature preprocessing (KNN, SVM, Logistic Regression, PCA), biomedical feature normalization and pipeline scaling.
#____________________________________________________________________________________
import pandas as pd
from sklearn.preprocessing import StandardScaler

patient_data = {'Age': [22, 58, 40], 'Blood_Pressure': [110, 150, 130]}

df_data = pd.DataFrame(patient_data)

scaler_data = StandardScaler()

scale_data_array = scaler_data.fit_transform(df_data)

scale_data_df = pd.DataFrame(scale_data_array, columns = df_data.columns)
print("Scaled Clinical Features (Zero Mean, Unit Variance):")
print(scale_data_df)
