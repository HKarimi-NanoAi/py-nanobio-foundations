#Topic: Robust User Input Loops Using Exception Handling
#Description: Combining 'while True' loop with 'try-except' to force the program to keep asking for input until a valid float is entered.
#Application: Lab equipment control panels to guarantee stable, non-breaking user interactions.
#_____________________________________________________________________________________________________________________

def get_secure_temperature():
    while True:
        try:
            temperature = float(input('Enter Incubator temperature: ')) 
            return temperature
        except:
            print('Invalid input! Try again...')

final_temperature = get_secure_temperature()
print(f"Incubator temperature is: {final_temperature}")
