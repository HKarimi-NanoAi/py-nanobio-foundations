#Topic: 2D Array Slicing and Feature Extraction in NumPy
#Description: Demonstrating how to slice a specific column (feature) from a 2D patients dataset matrix and find its maximum value.
#Application: Extracting specific vital signs (e.g., Temperature) from a multi-parametric clinical electronic health record (EHR) dataset.
#_______________________________________________________________________________________
import numpy as np

#Rows = patiants
#Column 1 = Body temperature
#Column 2 = Blood sugar
#Column 3 = Heart rate

patients_dataset = np.array([[36.6, 120, 72],
                             [37.2, 135, 80],
                             [38.5, 145, 95],
                            [36.1, 115, 68]])

temperature = patients_dataset[:, 0]
temp_max = np.max(temperature)
print(f'Maximum temperature is {temp_max}.')
