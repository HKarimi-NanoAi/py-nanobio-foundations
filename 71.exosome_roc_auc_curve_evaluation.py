#Topic: ROC Curve and AUC Score Evaluation in Exosome Diagnostics
#Description: Standardizing exosome concentration and fluorescence intensity metrics, predicting diagnostic probabilities using Logistic Regression and plotting the ROC curve alongside AUC scoring.
#Application: Biosensor sensitivity validation, clinical diagnostic thresholding and performance benchmarking for biomarker assays.

#_______________________________________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve, accuracy_score
import matplotlib.pyplot as plt

exosome_df = pd.DataFrame({
    'Exosome_Concentration': [150, 920, 210, 880, 180, 790, 310, 850, 240, 690, 380, 950],
    'Fluorescence_Intensity': [12.1, 85.3, 18.2, 90.1, 14.8, 78.5, 25.5, 82.0, 19.4, 68.2, 31.0, 92.4],
    'Diagnosis': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1]
})

x = exosome_df[['Exosome_Concentration','Fluorescence_Intensity']]
y = exosome_df['Diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model_lr = LogisticRegression(random_state = 42)
model_lr.fit(x_train_scaled, y_train)

y_pred = model_lr.predict(x_test_scaled)
model_accuracy = accuracy_score(y_test, y_pred)*100

y_prob = model_lr.predict_proba(x_test_scaled)[:,1]
roc_score_eval = roc_auc_score(y_test, y_prob)

print(f"Model Accuracy is {model_accuracy}\nModel ROC AUC is {roc_score_eval}")

fpr, tpr, thresholds = roc_curve(y_test, y_prob)
plt.figure(figsize = (8,6))
plt.plot(fpr, tpr, color = 'blue', label = f'ROC Curve {roc_score_eval:.2f}')
plt.plot([0,1], [0,1], color = 'red', linestyle = '--', linewidth = 1.7)
plt.xlabel('FALSE Positive Rate')
plt.ylabel('TRUE Positive Rate')
plt.title('ROC')
plt.legend(loc='lower right')
plt.show()
