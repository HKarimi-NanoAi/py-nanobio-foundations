#Topic: Introduction to Tabular Data Using Pandas DataFrames
#Description: Creating a structured DataFrame from raw biosensor dictionary data and computing key descriptive statistics (Mean and Max).
# Application: Standard approach for managing multi-sensor laboratory logs, calibrating outputs, and structured clinical data preprocessing.

#_______________________________________________________________________________________________________________________

import pandas as pd

biosensor_data = {'Sensor_ID': ['S1', 'S2', 'S3', 'S4', 'S5'],
                  'Voltage_mV': [120.5, 98.2, 145.0, 112.4, 85.1]}

biosensor_df = pd.DataFrame(biosensor_data)
mean_voltage = biosensor_df['Voltage_mV'].mean()
max_voltage = biosensor_df['Voltage_mV'].max()

print(f'Mean voltage of these biosensors are {mean_voltage:.4f}mV and the maximum recorded voltage is {max_voltage}mV.')
