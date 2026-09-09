#Topic: Cancer Biomarker Classification using Decision Tree Classifier
#Description: Building a interpretable Decision Tree model (max_depth=3) to classify oncology markers (Marker A and Marker B). Decision trees do not require feature scaling and offer clear rule-based medical decision logic.
#Application: Medical diagnostic decision trees, rule-based clinical scoring and non-linear biomarker threshold modeling.
#_______________________________________________________________________

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

cancer_df = pd.DataFrame({
    'Marker_A': [1.1, 8.2, 1.3, 9.0, 1.2, 8.5, 1.4, 9.1, 1.0, 8.8, 1.5, 8.9],
    'Marker_B': [0.5, 4.1, 0.6, 4.8, 0.4, 4.3, 0.7, 4.9, 0.3, 4.5, 0.8, 4.7],
    'Diagnosis': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

x = cancer_df[['Marker_A','Marker_B']]
y = cancer_df['Diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

model_tree = DecisionTreeClassifier(max_depth = 3, random_state = 42)
model_tree.fit(x_train, y_train)

y_prediction = model_tree.predict(x_test)
model_accuracy = accuracy_score(y_test, y_prediction)*100

model_confusion_matrix = confusion_matrix(y_test, y_prediction)
print('Classification report')
print(classification_report(y_test, y_prediction))
print(f'Model Accuracy is {model_accuracy}%')
print(f'Confusion Matrix is {model_confusion_matrix}')
