#Topic: Clinical Preprocessing: Feature Scaling and Train/Test Partitioning
#Description: Preprocessing diabetes risk factors (Age, Glucose) by separating features and target labels, applying StandardScaler and partitioning dataset into training (75%) and testing (25%)  subsets using sklearn.model_selection.train_test_split.
#Application: Predictive healthcare modeling, diabetes diagnosis pipelines and supervised classification dataset preparation.

#__________________________________________
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

clinical_data = {
    'Age': [25, 45, 60, 35, 52, 23, 40, 58],
    'Glucose': [85, 140, 180, 95, 160, 90, 130, 175],
    'Outcome': [0, 1, 1, 0, 1, 0, 0, 1]
}
df_clinical = pd.DataFrame(clinical_data)


x = df_clinical[['Age','Glucose']]
y = df_clinical['Outcome']

scaler_x =StandardScaler()
scaler_array_x = scaler_x.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaler_array_x, y, test_size = 0.25, random_state = 42)

print(f'Shape of:\nx-train is {x_train.shape}\ny-train is {y_train.shape}\nx-test is {x_test.shape}\ny-test is {y_test.shape}')
