# Topic: Feedback Loop Simulation for Hyperthermia Therapy Control
# Description: Utilizing 'while True' loop and conditional break to simulate continuous temperature monitoring and an emergency laser shutdown sequence.
# Application: Medical instrumentation for photothermal therapy (PTT) 
# P.s: maintaining the 42°C - 45°C therapeutic window
#______________________________________________________________________________________________________________________

while True:
    temperature = float(input("Enter temperature: "))
    if 42 <= temperature <= 45:
        print("STATUS: Optimal therapeutic temperature.")
    elif temperature < 42:
        print("STATUS: Temperature is low. Increasing laser power...")
    else:
        break
print('EMERGENCY: Temperature exceeded 45°C! Shutting down laser!')
