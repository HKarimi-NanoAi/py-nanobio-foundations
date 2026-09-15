#Topic: Comparative Benchmarking of Machine Learning Classifiers
#Description: Evaluating and ranking multiple algorithms (KNN, Decision Tree and Random Forest) using a clean dictionary-driven loop pipeline on oncology biomarker features.
#Application: Model selection, diagnostic benchmark comparison and automated pipeline architecture for clinical ML tasks.
#_________________________________________________________________________________

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
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

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)
  
models = {"knn":KNeighborsClassifier(n_neighbors = 3),
          "Random Forest": RandomForestClassifier(n_estimators = 100, random_state = 42),
          "Decision Tree":DecisionTreeClassifier(max_depth = 5, random_state = 42)}

names = []
accuracy = []

for name, model in models.items():
    model.fit(x_train, y_train)
    model_accuracy = accuracy_score(y_test, model.predict(x_test))*100
    
    names.append(name)
    accuracy.append(model_accuracy)
    print(f'{name} Accuracy is {model_accuracy:.2f}%')
    
model_df = pd.DataFrame({"Models' Name":names, "Model Accuracy":accuracy}).sort_values (by = "Model Accuracy", ascending = False)
print(model_df)   
                       
