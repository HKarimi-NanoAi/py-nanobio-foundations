#Topic: Basic Exception Handling (try-except) in Concentration Calculations
#Description: Demonstrating how to catch mathematical and value errors to prevent the program from crashing. 
#Application: Automated dilution systems where primary concentration cannot be zero.
# Useful and important for biosensors
#___________________________________________________________________________________________________

try:
    primary_concentration = float(input('Enter the primary concentration: '))   
    final_concentration = 100 / primary_concentration                     #based on a specific instruction
    print(f"Final concentration is {final_concentration:.5f}")
        
except:
    print ("Calculation Error: Division by zero or invalid input!")
