#__________________________________________________________________________________________________________________________
#Topic: Compound Boolean Logic for Clinical Emergency Screening
#Description: Evaluating patient safety metrics by combining vital signs. Also, using complex logical operators (and, or, not).
#Application: Early warning systems in clinical diagnostics to alert medical staff of critical patient deterioration or MI risks.
#_____________________________________________________________________________________________________________________________


body_temperature = float(input("Enter the patient's body temperature: "))
blood_spo2 = float(input("Enter the patient's SpO2: "))
cardiac_troponin_concentration = float(input("Enter patient's Cardiac Troponin concentration: "))

warning_situation = (not 36.5 <= body_temperature <= 37.5 ) or (blood_spo2 < 95 and cardiac_troponin_concentration >= 0.04)
print(warning_situation)
