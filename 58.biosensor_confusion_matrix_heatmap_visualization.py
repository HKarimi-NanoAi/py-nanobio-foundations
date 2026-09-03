#Topic: Confusion Matrix Heatmap Visualization for Biosensor Diagnostics
#Description: Building a Logistic Regression classifier for disease detection using optical biosensor light intensity and antigen concentration. Visualizing classification results via a Seaborn annotated heatmap and printing the corresponding classification report.
#Application: Medical diagnostic visualization, optical biosensor performance reporting and automated binary biomarker classification.

#___________________________________________________
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

biosensor_df = pd.DataFrame({
    'Light_Intensity': [15.2, 88.1, 14.0, 92.3, 16.5, 85.0, 12.1, 90.4, 18.2, 94.1, 11.0, 89.0],
    'Antigen_Conc': [0.5, 4.2, 0.4, 4.8, 0.8, 3.9, 0.3, 4.5, 0.9, 5.1, 0.2, 4.3],
    'Diagnosis': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

x = biosensor_df[['Light_Intensity','Antigen_Conc']]
y = biosensor_df['Diagnosis']

scaler = StandardScaler()
scaler_x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(scaler_x, y, test_size = 0.33, random_state = 42 )

model_lr = LogisticRegression()
model_lr.fit(x_train, y_train)

y_predict = model_lr.predict(x_test)

confusion_mat = confusion_matrix(y_test, y_predict)

plt.figure(figsize = (10,8))
sns.heatmap(confusion_mat, fmt = 'd', cmap = 'Blues', xticklabels = ['Negative', 'Positive'], yticklabels = ['Negative', 'Positive'], annot = True)
plt.xlabel('Prediction')
plt.ylabel('Actual')
plt.title('Confusion Matrix Heatmap')
plt.show()

print('Classification Report:')
print(classification_report(y_test, y_predict))
