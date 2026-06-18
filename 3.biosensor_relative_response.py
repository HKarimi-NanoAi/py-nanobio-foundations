#________________________________________________________________________________________________________________________________
#Topic: Biosensor Relative Response (RR%) Calculation
# Description: Handling dynamic user input (float) to calculate the RR% against a fixed baseline signal.
# Application: Standard signal processing step in electrochemical or optical nanobiosensors to normalize data.
#__________________________________________________________________________________________________________________________________

baseline_signal = 15.5
current_signal = float(input("Enter the current signal : "))
print(f"The Relative Response (RR%) is {(current_signal/baseline_signal)*100}%")
