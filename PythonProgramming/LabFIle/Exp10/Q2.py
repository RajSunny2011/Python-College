# Q2. Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. Also find 2nd maximum element in the array. 
import numpy as np

array = np.array([[5, 6, 3],[1, 9, 4],[7, 2, 8]])

row_sums = np.sum(array, axis=1)
column_sums = np.sum(array, axis=0)
flattened = array.flatten()
flattened.sort()
second_max = flattened[-2]

print("Array:")
print(array)
print("Sum of rows:", row_sums)
print("Sum of columns:", column_sums)
print("Second maximum element:", second_max)

