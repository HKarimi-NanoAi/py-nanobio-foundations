# Topic: Functions Processing for Patient Screening
# Description: Defining a function to iterate through a list of Troponin concentrations and count patients exceeding the critical threshold.
# Application: Simulating high-throughput clinical screening tools
#____________________________________________________________________________________________________________________________________

def count_critical_patients(troponin_lists):
    
    high_troponin_count = 0
    
    for data in troponin_lists:
        if data >= 0.04:
            high_troponin_count = high_troponin_count + 1
    return high_troponin_count
    
user_data = input('Enter troponin concentration (separated by coma): ')
user_list = [float(x.strip()) for x in user_data.split(',')]    #separating datas to have a true list
final_data = count_critical_patients(user_list)

print(f'Total number of critical patients is: {final_data}')
