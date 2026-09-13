#Topic: Comparative Analysis: Decision Tree vs. Random Forest Classifier
#Description: Benchmarking a single Decision Tree against an Ensemble Random Forest Classifier (n_estimators=100) on oncology biomarker features to evaluate performance and stability.
#Application: Ensemble learning evaluation, clinical ML model selection and variance reduction in biomarker diagnostic classification.
#________________________________________________________________________________________________________________________________


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

cancer_df = pd.DataFrame({
    'Marker_A': [1.1, 8.2, 1.3, 9.0, 1.2, 8.5, 1.4, 9.1, 1.0, 8.8],
    'Marker_B': [0.5, 4.1, 0.6, 4.8, 0.4, 4.3, 0.7, 4.9, 0.3, 4.5],
    'Diagnosis': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

x = cancer_df[['Marker_A','Marker_B']]
y = cancer_df['Diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3, random_state = 42)

model1 = DecisionTreeClassifier(max_depth = 3, random_state = 42)
model1.fit(x_train, y_train)
y_pred1 = model1.predict(x_test)
model1_accuracy = accuracy_score(y_test, y_pred1)*100

model2 = RandomForestClassifier(n_estimators = 100, random_state = 42)
model2.fit(x_train, y_train)
y_pred2 = model2.predict(x_test)
model2_accuracy = accuracy_score(y_test, y_pred2)*100

print(f"Model Accuracy (Decision Tree):{model1_accuracy:.2f}%")
print(f"Model Accuracy (Random Forest):{model2_accuracy:.2f}%")
