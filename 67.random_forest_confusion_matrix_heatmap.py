#Topic: Confusion Matrix Visualization via Seaborn Heatmap
#Description: Training a Random Forest Classifier on oncology biomarkers and visually presenting true vs. predicted classifications using an annotated Seaborn heatmap.
#Application: Model evaluation, diagnostic accuracy visualization and clinical performance presentation.

#__________________________________________________________________________________________________________

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

cancer_df = pd.DataFrame({
    'Marker_A': [1.1, 8.2, 1.3, 9.0, 1.2, 8.5, 1.4, 9.1, 1.0, 8.8],
    'Marker_B': [0.5, 4.1, 0.6, 4.8, 0.4, 4.3, 0.7, 4.9, 0.3, 4.5],
    'Diagnosis': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

x = cancer_df[['Marker_A','Marker_B']]
y= cancer_df['Diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3 , random_state = 42)
model = RandomForestClassifier(n_estimators = 100, random_state = 42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

model_accuracy = accuracy_score(y_test, y_pred)* 100
print(f'Model Accuracy is {model_accuracy:.2f}%')

cm = confusion_matrix(y_test, y_pred)


plt.figure(figsize = (10,8))
sns.heatmap(cm, annot = True, fmt = 'd', cmap = 'Greens', xticklabels = ['Healthy', 'Cancer'], yticklabels = ['Healthy', 'Cancer'])
plt.xlabel('Markers')
plt.ylabel('Diagnosis')
plt.title('Cancer Diagnosis')
plt.show()
