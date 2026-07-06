#Topic: Adaptive Data Filtering and Boolean Masking Based on Dataset Mean
#Description: Computing the mean of a fasting blood sugar (FBS) dataset and using it as a dynamic threshold to filter out upper values.
#Application: Clinical screening to identify patients with glucose levels above the cohort average.
#________________________________________________________________________________________________________________
import numpy as np

fblood_sugar_dataset = [95, 120, 88, 140, 105, 110, 92, 130, 85, 115]
dataset_numpy = np.array(fblood_sugar_dataset)

dataset_mean = np.mean(dataset_numpy)
filtering = dataset_numpy[dataset_numpy > dataset_mean]
convert_to_list = filtering.tolist()
fbs_filtering_str = ','.join(f'{x:.2f}' for x in convert_to_list)

print(f'Patient values higher than mean: {fbs_filtering_str}')
