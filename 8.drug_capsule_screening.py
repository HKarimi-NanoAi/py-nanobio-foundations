#Topic: Data Filtering and Drug Screening using 'for' 
#Description: Iterating through a list of nanocapsule thermal resistance values and filtering out those that do not meet the minimum stability threshold.
#Application: High-throughput screening (HTS) of drug delivery vehicles to select candidates capable of withstanding specific thermal conditions.
#_______________________________________________________________________________________________________________________

thermal_resistance = [45, 12, 60, 85, 30, 95, 8]
approved_capsules = []

for cap_time in thermal_resistance:
    if cap_time >= 50:
        approved_capsules.append(cap_time)

print(f"Primary list was {thermal_resistance} but approved capsules are {approved_capsules}")
