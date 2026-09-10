#Topic: Visualizing Decision Tree Rules & Architecture using plot_tree
#Description: Training a Decision Tree classifier (max_depth=3) on oncology biomarkers (Biomarker A & B) and visually rendering the decision rules, node impurities (Gini) and class outputs via Matplotlib.
#Application: Explainable AI (XAI) in medicine, clinical decision-tree rule generation and interpretable biomarker diagnostics.
#_________________________________________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

cancer_df = pd.DataFrame({
    'Biomarker_A': [1.1, 8.2, 1.3, 9.0, 1.2, 8.5, 1.4, 9.1, 1.0, 8.8, 1.5, 8.9],
    'Biomarker_B': [0.5, 4.1, 0.6, 4.8, 0.4, 4.3, 0.7, 4.9, 0.3, 4.5, 0.8, 4.7],
    'Diagnosis': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

x = cancer_df[['Biomarker_A', 'Biomarker_B']]
y = cancer_df['Diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

model_tree = DecisionTreeClassifier(max_depth = 3, random_state = 42)
model_tree.fit(x_train, y_train)
y_pred = model_tree.predict(x_test)

plt.figure(figsize = (10,6))
plot_tree(model_tree, feature_names = ['Biomarker_A','Biomarker_B'], class_names = ['Negative','Positive'], fontsize = 15, rounded = True, filled = True)

plt.title ('Decision Tree Structure')
plt.show()

print(f'Model Acuuracy {accuracy_score(y_test, y_pred)*100:.2f}%')
