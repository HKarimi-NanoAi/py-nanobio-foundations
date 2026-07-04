#Topic: Vectorized Operations and Boolean Masking Using NumPy
#Description: Utilizing NumPy arrays for efficient element-wise conversion (Celsius to Kelvin) and data filtering.
# Application: Processing high-throughput thermal resistance or hyperthermia datasets where fast mathematical operations are required.
#___________________________________________________________________________________________________________________________

import numpy as np

saved_temperature = np.array([36.5, 42.1, 38.0, 39.4, 41.2])
convert_to_kelvin = saved_temperature + 273.15

critical_temp = convert_to_kelvin[convert_to_kelvin > 312]

critical_list = critical_temp.tolist()
critical_str = ','.join(f'{x:.2f}' for x in critical_list)
    
print(f'Critical temperatures are [{critical_str}]')
