#Topic: Extracting and Visualizing Feature Importances in Decision Trees
#Description: Evaluating the Gini importance of multiple cancer panel biomarkers (Biomarker A to D) using a Decision Tree model and plotting horizontal bar charts to rank key diagnostic drivers.
#Application: Biomarker selection, feature reduction in diagnostic panels and explainable medical machine learning.
#_______________________________________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

cancer_panel = pd.DataFrame({
    'Biomarker_A': [1.1, 8.2, 1.3, 9.0, 1.2, 8.5, 1.4, 9.1],
    'Biomarker_B': [0.5, 4.1, 0.6, 4.8, 0.4, 4.3, 0.7, 4.9],
    'Biomarker_C': [12.0, 12.5, 11.9, 12.8, 12.1, 12.4, 11.8, 12.7],
    'Biomarker_D': [100, 105, 98, 102, 101, 104, 99, 103],
    'Diagnosis': [0, 1, 0, 1, 0, 1, 0, 1]
})

x = cancer_panel[['Biomarker_A','Biomarker_B','Biomarker_C','Biomarker_D']]
y = cancer_panel['Diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

model = DecisionTreeClassifier(max_depth = 2, random_state = 42)
model.fit(x_train, y_train)

importance = model.feature_importances_

importance_df = pd.DataFrame({'Features':['Biomarker_A','Biomarker_B','Biomarker_C','Biomarker_D'],"importance": importance})
print(importance_df)

plt.barh(importance_df['Features'], importance_df['importance'], color = 'skyblue', edgecolor = 'yellow')
plt.title ('Feature Importance')
plt.xlabel("Importance")
plt.ylabel("Features")
plt.show()
