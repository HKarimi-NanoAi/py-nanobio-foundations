#Topic: Microfluidic Biomarker Response Prediction & Probability Estimation
#Description: Standardizing exosome count and flow rate metrics in microfluidic channels and applying Logistic Regression with predict_proba to output classification probability confidence for therapy response.
#Application: Lab-on-a-chip diagnostics, exosome-based biomarker profiling and probabilistic clinical decision support.
#________________________________________________________________________________


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

microfluidics_df = pd.DataFrame({
    'Exosome_Count': [120, 850, 310, 920, 150, 780, 410, 890, 200, 650, 340, 910],
    'Flow_Rate': [1.2, 5.1, 2.0, 5.8, 1.1, 4.9, 2.5, 5.5, 1.4, 4.2, 2.1, 5.9],
    'Therapy_Response': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1]
})

x = microfluidics_df[['Exosome_Count','Flow_Rate']]
y = microfluidics_df['Therapy_Response']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model_log_reg = LogisticRegression(random_state = 42)
model_log_reg.fit(x_train_scaled, y_train)
y_pred = model_log_reg.predict(x_test_scaled)

probability = model_log_reg.predict_proba(x_test_scaled)
prob_class_0 = probability[0][0]*100
prob_class_1 = probability[0][1]*100

print(f"Probability Array (Class0 and Class1): \n{probability}")
print(f"Probability of being Positive is {prob_class_1:.2f}%")
print(f"Probability of being Negative is {prob_class_0:.2f}%")
print(f"Classification Report is\n{classification_report(y_test, y_pred)}")
