#Topic: Matrix Initialization and Array Broadcasting in NumPy
#Description: Creating a 2D matrix of zeros, inspecting its structural dimensions (shape), and applying a scalar addition across all elements simultaneously using NumPy's broadcasting feature.
#Application: Preparing initial weight matrices or baseline feature arrays for machine learning models and multidimensional sensor grids.
#__________________________________________________________________________________________________________________________

import numpy as np

empty_array = np.zeros((5,4))
print('Dimensions of this array are', empty_array.shape)

filled_array = empty_array + 37.0
print(filled_array)
