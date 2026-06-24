#Topic: Clinical database management using py Dictionaries
#Description: Demonstrating how to access, evaluate, and update key-value pairs in dictionary based on conditional thresholds.
#Application: Simulating patient health record updates (EHR) in ICU monitoring system.
#_________________________________________________________________________________________________________

#defined 
icu_patient = {
    "name": "Alex Smith",
    "spo2": 96.0,
    "temperature": 38.2,
    "heart_rate": 88
}


if icu_patient["spo2"] < 95 or icu_patient['temperature'] > 37.5:
    icu_patient["status"] = "CRITICAL"
else:
    icu_patient["status"] = "NORMAL"
        
print(f"Updated dictionary is: {icu_patient}")
